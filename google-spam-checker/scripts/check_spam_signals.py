#!/usr/bin/env python3
"""
check_spam_signals.py - Programmatic heuristic scanner for Google Web Search Spam Policies.
Analyzes local HTML files, raw text drafts, or live URLs for technical & content spam signals.

Checked Categories:
1. Hidden text and link abuse (CSS offscreen, font-size 0, opacity 0, micro-links)
2. Keyword stuffing & unnatural repetition (n-gram density, excessive repetitive phrases)
3. Link spam & thin affiliation signals (unqualified affiliate/monetization links, excessive outbound links)
4. Sneaky redirects & deceptive scripts (meta refresh, window.location redirection, back-button hijacking)
5. Misleading functionality & fake generator patterns
6. Scaled content / scraping markers (low lexical diversity, high boilerplate patterns)
"""

import sys
import os
import re
import json
import argparse
from urllib.parse import urlparse
from html.parser import HTMLParser
from collections import Counter


class HTMLSpamAnalyzer(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text_tokens = []
        self.raw_text_parts = []
        self.links = []
        self.meta_tags = []
        self.scripts = []
        self.styles = []
        self.inline_styles = []
        
        self.current_tag = None
        self.in_script = False
        self.in_style = False
        self.current_script_content = []
        self.current_style_content = []
        
        # Tracking micro links / hidden links
        self.current_link_tag = None
        self.current_link_text = []

    def handle_starttag(self, tag, attrs):
        self.current_tag = tag
        attr_dict = dict(attrs)

        # Style tag
        if tag == "style":
            self.in_style = True
            self.current_style_content = []

        # Script tag
        if tag == "script":
            self.in_script = True
            self.current_script_content = []

        # Meta tag
        if tag == "meta":
            self.meta_tags.append(attr_dict)

        # Inline style
        if "style" in attr_dict:
            self.inline_styles.append({
                "tag": tag,
                "style": attr_dict["style"],
                "attrs": attr_dict
            })

        # Link tag
        if tag == "a":
            href = attr_dict.get("href", "")
            rel = attr_dict.get("rel", "")
            self.current_link_tag = {
                "href": href,
                "rel": rel,
                "attrs": attr_dict,
                "text": ""
            }
            self.current_link_text = []

    def handle_endtag(self, tag):
        if tag == "style":
            self.in_style = False
            self.styles.append("".join(self.current_style_content))
            self.current_style_content = []
        elif tag == "script":
            self.in_script = False
            self.scripts.append("".join(self.current_script_content))
            self.current_script_content = []
        elif tag == "a" and self.current_link_tag:
            self.current_link_tag["text"] = "".join(self.current_link_text).strip()
            self.links.append(self.current_link_tag)
            self.current_link_tag = None
            self.current_link_text = []
        self.current_tag = None

    def handle_data(self, data):
        if self.in_style:
            self.current_style_content.append(data)
        elif self.in_script:
            self.current_script_content.append(data)
        else:
            self.raw_text_parts.append(data)
            if self.current_link_tag is not None:
                self.current_link_text.append(data)


def extract_words(text):
    return re.findall(r"\b[a-zA-Z0-9_\-\$]{2,}\b", text.lower())


def analyze_hidden_elements(analyzer):
    findings = []
    
    # 1. Check inline styles for stealth tricks
    suspicious_patterns = [
        (r"display\s*:\s*none", "display: none"),
        (r"visibility\s*:\s*hidden", "visibility: hidden"),
        (r"opacity\s*:\s*0(?![.\d])", "opacity: 0"),
        (r"font-size\s*:\s*0(?:px|pt|em|rem)?", "font-size: 0"),
        (r"text-indent\s*:\s*-[0-9]{3,}(?:px|em)", "extreme negative text-indent"),
        (r"position\s*:\s*absolute.*?left\s*:\s*-[0-9]{3,}(?:px|em)", "off-screen absolute positioning"),
        (r"color\s*:\s*(#fff(?:fff)?|white)\b.*?background(?:-color)?\s*:\s*(#fff(?:fff)?|white)\b", "white text on white background"),
        (r"color\s*:\s*(#000(?:000)?|black)\b.*?background(?:-color)?\s*:\s*(#000(?:000)?|black)\b", "black text on black background")
    ]

    for item in analyzer.inline_styles:
        s = item["style"].lower()
        for pattern, label in suspicious_patterns:
            if re.search(pattern, s):
                findings.append({
                    "policy": "Hidden text and link abuse",
                    "severity": "HIGH",
                    "detail": f"Suspicious inline style ({label}) found on <{item['tag']}>: '{item['style']}'",
                    "snippet": str(item["attrs"])
                })

    # 2. Check CSS style blocks for extreme offsets
    for css in analyzer.styles:
        css_lower = css.lower()
        for pattern, label in suspicious_patterns:
            matches = re.finditer(pattern, css_lower)
            for m in matches:
                # Get small context window
                start = max(0, m.start() - 30)
                end = min(len(css), m.end() + 30)
                snippet = css[start:end].strip().replace("\n", " ")
                findings.append({
                    "policy": "Hidden text and link abuse",
                    "severity": "MEDIUM",
                    "detail": f"CSS stylesheet block contains {label}",
                    "snippet": snippet
                })

    # 3. Check micro-links / punctuation anchor links
    for link in analyzer.links:
        href = link.get("href", "")
        text = link.get("text", "")
        # Only check outbound/non-empty href
        if href and not href.startswith("#") and not href.startswith("javascript:"):
            # Single punctuation or single character anchor
            if len(text) == 1 and text in ".-_,;*•~^":
                findings.append({
                    "policy": "Hidden text and link abuse",
                    "severity": "HIGH",
                    "detail": f"Micro-anchor link detected using single punctuation character '{text}'",
                    "snippet": f'<a href="{href}">{text}</a>'
                })
            elif len(text) == 0 and not link.get("attrs", {}).get("aria-label") and not link.get("attrs", {}).get("title"):
                # Empty anchor text without accessible label
                findings.append({
                    "policy": "Hidden text and link abuse",
                    "severity": "LOW",
                    "detail": "Empty anchor tag with no visible text, image alt, or aria-label",
                    "snippet": f'<a href="{href}"></a>'
                })

    return findings


def analyze_keyword_stuffing(text):
    findings = []
    words = extract_words(text)
    total_words = len(words)
    if total_words < 50:
        return findings

    # Stopwords filter
    stopwords = {
        "the", "and", "for", "that", "this", "with", "from", "your", "have", "more",
        "will", "about", "what", "which", "when", "there", "their", "they", "been",
        "were", "other", "some", "into", "than", "then", "them", "these", "only"
    }

    filtered_words = [w for w in words if w not in stopwords and len(w) > 3]
    if not filtered_words:
        return findings

    # Unigram density
    word_counts = Counter(filtered_words)
    for word, count in word_counts.most_common(5):
        density = (count / total_words) * 100
        if density > 4.5 and count >= 5:
            findings.append({
                "policy": "Keyword stuffing",
                "severity": "HIGH" if density > 7.0 else "MEDIUM",
                "detail": f"Excessive keyword density for '{word}': {density:.1f}% ({count} occurrences across {total_words} words)",
                "snippet": f"Term: '{word}', Count: {count}, Total Words: {total_words}"
            })

    # Bigram density
    bigrams = [f"{filtered_words[i]} {filtered_words[i+1]}" for i in range(len(filtered_words) - 1)]
    bigram_counts = Counter(bigrams)
    for bigram, count in bigram_counts.most_common(3):
        density = (count / (total_words / 2)) * 100
        if count >= 4 and density > 3.0:
            findings.append({
                "policy": "Keyword stuffing",
                "severity": "MEDIUM",
                "detail": f"Unnatural repetition of 2-word phrase '{bigram}': {count} occurrences",
                "snippet": f"Phrase: '{bigram}', Frequency: {count}"
            })

    # Repetitive phone numbers or postal codes
    phone_matches = re.findall(r"\b(?:\+?\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}\b", text)
    if len(phone_matches) >= 5 and len(set(phone_matches)) < 3:
        findings.append({
            "policy": "Keyword stuffing",
            "severity": "MEDIUM",
            "detail": f"Repetitive phone number block detected ({len(phone_matches)} instances)",
            "snippet": f"Phone count: {len(phone_matches)}"
        })

    return findings


def analyze_link_spam(analyzer, host_domain=None):
    findings = []
    
    # Common affiliate / tracking domains or parameters
    affiliate_indicators = [
        "amazon.", "amzn.to", "shareasale.com", "cj.com", "clickbank.net",
        "impact.com", "rakuten.com", "awin1.com", "tradedoubler.com",
        "affiliate", "partner", "ref=", "tag=", "aff_id=", "subid="
    ]

    outbound_links = []
    unqualified_commercial_links = []
    
    for link in analyzer.links:
        href = link.get("href", "")
        rel = (link.get("rel") or "").lower()
        text = link.get("text", "")
        
        parsed = urlparse(href)
        if parsed.scheme in ["http", "https"]:
            domain = parsed.netloc.lower()
            if host_domain and domain == host_domain.lower():
                continue  # internal link
            
            outbound_links.append(link)
            
            # Check if likely commercial/affiliate
            is_commercial = any(ind in href.lower() for ind in affiliate_indicators)
            has_no_follow = "nofollow" in rel or "sponsored" in rel
            
            if is_commercial and not has_no_follow:
                unqualified_commercial_links.append(link)

    if unqualified_commercial_links:
        sample = unqualified_commercial_links[:3]
        samples_str = ", ".join([f"<{l['href'][:50]}...>" for l in sample])
        findings.append({
            "policy": "Link spam & Thin affiliation",
            "severity": "HIGH",
            "detail": f"Found {len(unqualified_commercial_links)} affiliate/commercial link(s) missing required rel='sponsored' or rel='nofollow' attribute",
            "snippet": f"Sample URLs: {samples_str}"
        })

    # Excessive outbound link ratio
    if len(outbound_links) > 50:
        findings.append({
            "policy": "Link spam",
            "severity": "MEDIUM",
            "detail": f"Unusually high volume of outbound links ({len(outbound_links)} links)",
            "snippet": f"Total outbound links: {len(outbound_links)}"
        })

    return findings


def analyze_redirects_and_scripts(analyzer):
    findings = []

    # Meta refresh
    for meta in analyzer.meta_tags:
        http_equiv = meta.get("http-equiv", "").lower()
        if http_equiv == "refresh":
            content = meta.get("content", "")
            findings.append({
                "policy": "Sneaky redirects",
                "severity": "HIGH" if "url=" in content.lower() else "LOW",
                "detail": f"Meta refresh tag detected: content='{content}'",
                "snippet": str(meta)
            })

    # Script inspection for sneaky redirects or back button hijacking
    script_text = "\n".join(analyzer.scripts).lower()
    
    if "history.pushstate" in script_text and ("window.onpopstate" in script_text or "popstate" in script_text):
        if "location.replace" in script_text or "location.href" in script_text:
            findings.append({
                "policy": "Malicious practices (Back button hijacking)",
                "severity": "HIGH",
                "detail": "Detected history.pushState paired with popstate redirect, characteristic of back-button hijacking",
                "snippet": "history.pushState / popstate redirect loop detected in script"
            })

    # Device or referrer conditional redirects
    if re.search(r"navigator\.useragent.*?(?:location\.replace|location\.href)", script_text, re.DOTALL):
        findings.append({
            "policy": "Sneaky redirects / Cloaking",
            "severity": "HIGH",
            "detail": "User-Agent sniffing redirect logic detected in client script",
            "snippet": "navigator.userAgent conditional redirection pattern"
        })

    if re.search(r"document\.referrer.*?(?:google|bing|yahoo).*?(?:location\.replace|location\.href)", script_text, re.DOTALL):
        findings.append({
            "policy": "Sneaky redirects / Cloaking",
            "severity": "HIGH",
            "detail": "Search engine referrer conditional redirection pattern detected",
            "snippet": "document.referrer conditional redirection pattern"
        })

    return findings


def analyze_misleading_functionality(text):
    findings = []
    text_lower = text.lower()

    misleading_patterns = [
        (r"\b(?:free|unlimited)\s+(?:app\s+store|google\s+play|v-bucks|robux|steam)\s+(?:credit|code|card|gift\s+card)\s+generator\b", "Fake Credit / Currency Generator"),
        (r"\bdownload\s+will\s+start\s+(?:after|once\s+you\s+complete)\s+(?:a\s+survey|an\s+offer|verification)\b", "Deceptive Content Locker / Survey Wall"),
        (r"\bclick\s+here\s+to\s+verify\s+you\s+are\s+human\s+to\s+unlock\s+download\b", "Faux Human Verification Trap"),
        (r"\b(?:crack|keygen|serial\s+number)\s+(?:generator|download|free)\b", "Unwanted Software / Keygen Claim")
    ]

    for pattern, label in misleading_patterns:
        m = re.search(pattern, text_lower)
        if m:
            findings.append({
                "policy": "Misleading functionality & Scam/Fraud",
                "severity": "HIGH",
                "detail": f"Deceptive functionality pattern detected: {label}",
                "snippet": text[max(0, m.start()-20):min(len(text), m.end()+20)].strip()
            })

    return findings


def analyze_scaled_content(text):
    findings = []
    words = extract_words(text)
    total_words = len(words)
    if total_words < 100:
        return findings

    # Lexical Diversity (Type-Token Ratio)
    unique_words = set(words)
    ttr = len(unique_words) / total_words

    # If document is lengthy but has extremely poor lexical diversity
    if total_words > 300 and ttr < 0.22:
        findings.append({
            "policy": "Scaled content abuse",
            "severity": "MEDIUM",
            "detail": f"Unusually low lexical diversity (TTR: {ttr:.2f}). Repetitive boilerplate or low-entropy generated text.",
            "snippet": f"Total words: {total_words}, Unique words: {len(unique_words)}"
        })

    # Check for obvious AI prompt echoes or unedited outputs
    ai_echoes = [
        "as an ai language model",
        "in conclusion, it is important to remember",
        "here is a rewrite of the article",
        "certainly! here is an article about",
        "i cannot fulfill this request as"
    ]
    for echo in ai_echoes:
        if echo in text.lower():
            findings.append({
                "policy": "Scaled content abuse",
                "severity": "HIGH",
                "detail": f"Detected raw AI generator remnant string: '{echo}'",
                "snippet": f"Exact phrase found: '{echo}'"
            })

    return findings


def run_full_audit(html_or_text, host_domain=None):
    analyzer = HTMLSpamAnalyzer()
    analyzer.feed(html_or_text)
    
    body_text = " ".join(analyzer.raw_text_parts)
    if not body_text.strip():
        body_text = html_or_text

    findings = []
    findings.extend(analyze_hidden_elements(analyzer))
    findings.extend(analyze_keyword_stuffing(body_text))
    findings.extend(analyze_link_spam(analyzer, host_domain))
    findings.extend(analyze_redirects_and_scripts(analyzer))
    findings.extend(analyze_misleading_functionality(body_text))
    findings.extend(analyze_scaled_content(body_text))

    # Summary calculation
    high_count = sum(1 for f in findings if f["severity"] == "HIGH")
    med_count = sum(1 for f in findings if f["severity"] == "MEDIUM")
    low_count = sum(1 for f in findings if f["severity"] == "LOW")
    
    if high_count > 0:
        overall_status = "CRITICAL RISK - HIGH LIKELIHOOD OF POLICY VIOLATION"
    elif med_count > 0:
        overall_status = "WARNING - SUSPICIOUS SIGNALS DETECTED"
    elif low_count > 0:
        overall_status = "MINOR CONCERNS - REVIEW RECOMMENDED"
    else:
        overall_status = "CLEAN - NO AUTOMATED SPAM SIGNALS DETECTED"

    return {
        "status": overall_status,
        "counts": {
            "high": high_count,
            "medium": med_count,
            "low": low_count,
            "total": len(findings)
        },
        "findings": findings,
        "metrics": {
            "total_words": len(extract_words(body_text)),
            "total_links": len(analyzer.links),
            "total_scripts": len(analyzer.scripts),
            "total_styles": len(analyzer.styles) + len(analyzer.inline_styles)
        }
    }


def main():
    parser = argparse.ArgumentParser(description="Google Search Spam Policies Signal Scanner")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--file", "-f", help="Path to local HTML or text file")
    group.add_argument("--text", "-t", help="Raw text string to analyze")
    group.add_argument("--url", "-u", help="URL to fetch and analyze")
    
    parser.add_argument("--domain", "-d", help="Host domain for internal vs outbound link categorization")
    parser.add_argument("--json", "-j", action="store_true", help="Output results in JSON format")

    args = parser.parse_args()

    content = ""
    domain = args.domain

    if args.file:
        with open(args.file, "r", encoding="utf-8", errors="ignore") as f:
            content = f.read()
    elif args.text:
        content = args.text
    elif args.url:
        import urllib.request
        req = urllib.request.Request(args.url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        try:
            with urllib.request.urlopen(req) as resp:
                content = resp.read().decode("utf-8", errors="ignore")
                if not domain:
                    domain = urlparse(args.url).netloc
        except Exception as e:
            sys.stderr.write(f"Error fetching URL: {e}\n")
            sys.exit(1)

    result = run_full_audit(content, host_domain=domain)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print("\n" + "=" * 60)
        print(f" GOOGLE SPAM POLICIES AUDIT RESULT: {result['status']}")
        print("=" * 60)
        print(f"Total Findings: {result['counts']['total']} | High: {result['counts']['high']} | Medium: {result['counts']['medium']} | Low: {result['counts']['low']}")
        print(f"Metrics: {result['metrics']['total_words']} words, {result['metrics']['total_links']} links analyzed.\n")
        
        if not result["findings"]:
            print("No programmatic spam signals detected.")
        else:
            for i, f in enumerate(result["findings"], 1):
                print(f"[{i}] [{f['severity']}] {f['policy']}")
                print(f"    Issue: {f['detail']}")
                if f.get("snippet"):
                    print(f"    Snippet: {f['snippet'][:120]}")
                print()


if __name__ == "__main__":
    main()
