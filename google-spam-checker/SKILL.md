---
name: google-spam-checker
description: Comprehensive audit and diagnostic tool for Google Web Search Spam Policies (Google Search Essentials). Detects, analyzes, and remediates violations across all 17+ official policy categories including cloaking, doorway abuse, expired domain abuse, hacked content, hidden text and link abuse, keyword stuffing, link spam (unqualified affiliate/paid links), machine-generated traffic, malicious practices (back-button hijacking, malware), misleading functionality, scaled content abuse (AI mass generation, scraping, spinning), site reputation abuse (parasite SEO; EEA vs Non-EEA rules), sneaky redirects, thin affiliation, user-generated spam, and scam/fraud/circumvention. Use PROACTIVELY whenever auditing content, URLs, or HTML source for Google spam risks, algorithmic updates, manual actions, backlink penalties, affiliate monetization compliance, or content quality checks.
---

# Google Spam Policies Checker

An authoritative skill for evaluating web pages, raw HTML source, content drafts, and site architectures against official **Google Search Essentials Spam Policies**.

---

## Quick Reference & Resources

This skill employs progressive disclosure. Use bundled tools and references as needed:

* **Automated Scanner Script**:
  `scripts/check_spam_signals.py` — Scans local HTML files, URLs, or text snippets for programmatic red flags (CSS hidden text, zero-opacity, micro-anchors, unqualified affiliate links, redirect scripts, keyword stuffing density, and AI boilerplate artifacts).
* **Complete Policy Matrix**:
  `references/spam_policies_matrix.md` — In-depth definitions, mechanics, compliant exceptions, and audit criteria for all 17+ spam policies.
* **Site Reputation ("Parasite SEO") & EEA Guide**:
  `references/site_reputation_and_eea.md` — The 4 objective evaluation factors, publisher integration requirements, and regional EEA vs. Non-EEA enforcement rules.
* **Manual Actions & Remediation Playbook**:
  `references/manual_actions_remediation.md` — Diagnosing penalties in Google Search Console, step-by-step cleanup protocols, and submission templates for reconsideration requests.
* **Audit Checklist**:
  `references/audit_checklist.md` — 6-phase systematic checklist covering architecture, technical rendering, DOM, content substance, links, and site trust.

---

## Core Audit Workflow

When auditing any target for Google spam compliance, follow this 4-step process:

```
[Input: URL / HTML / Draft]
         │
         ▼
[Step 1: Automated Scan] ────────► Run scripts/check_spam_signals.py
         │
         ▼
[Step 2: Deep Qualitative Review] ─► Evaluate against 17+ Google Spam Policies
         │
         ▼
[Step 3: Regional & Context Check] ─► EEA vs Global rules, UX exceptions
         │
         ▼
[Step 4: Report Generation] ──────► Actionable Report with Severity & Fixes
```

---

### Step 1: Run Programmatic Scan

For raw HTML, local files, or live URLs, execute the scanner script:

```bash
# Analyze a local HTML or text file
python scripts/check_spam_signals.py --file path/to/page.html --domain example.com

# Analyze a live URL
python scripts/check_spam_signals.py --url "https://example.com/page"

# Analyze raw text / snippet
python scripts/check_spam_signals.py --text "Sample content to check..."
```

The script outputs flagged items categorized by severity (`HIGH`, `MEDIUM`, `LOW`) along with extracted snippets.

---

### Step 2: Conduct Deep Qualitative Policy Review

Automated tools catch syntax and DOM patterns, but Google's spam updates increasingly target semantic and intent abuse. Evaluate the target against the primary risk areas:

#### 1. Scaled Content Abuse & Scraping
* **Test**: Does the content exhibit evidence of automated mass production (unassisted LLM generation, database spinning, or feed aggregation) targeting long-tail queries without unique value?
* **Verification**: Look for first-hand research, proprietary data, expert quotes, original photography, or real testing benchmarks. If absent, flag as **Scaled Content Abuse**.

#### 2. Site Reputation Abuse ("Parasite SEO")
* **Test**: Is this third-party commercial content hosted on an established authority domain primarily to borrow that domain's ranking signals?
* **Check the 4 Objective Factors**:
  1. *Presentation & UX*: Does the design, typography, and layout match the host site?
  2. *Quality Parity*: Does the content meet the editorial standards of the host?
  3. *Authorship & Responsibility*: Is there a named in-house author/editor and clear commercial disclosure?
  4. *Multi-Site Duplication*: Is the same syndicated review or coupon feed distributed across multiple unrelated news/educational domains?

#### 3. Thin Affiliation & Link Spam
* **Test**: Are affiliate links present? If yes:
  * Are outbound links qualified with `rel="sponsored"` or `rel="nofollow"`? (Missing attribute is a direct violation).
  * Does the page merely reproduce merchant descriptions and stock images without unique reviews, pros/cons, or comparative testing?

#### 4. Cloaking & Sneaky Redirects
* **Test**: Does the page alter content or destination based on user-agent, IP, device, or referrer?
* **Paywall Rule**: Metered or paywalled content is NOT cloaking if Googlebot can crawl the full text and proper schema markup (`isAccessibleForFree`) is implemented.

#### 5. Hidden Content vs. Legitimate UX
* **Distinction**:
  * *Prohibited*: `display:none`, `visibility:hidden`, `opacity:0`, `font-size:0`, or `text-indent: -9999px` applied to keyword blocks or unviewable links. Micro-punctuation links (`<a href="...">.</a>`).
  * *Allowed*: Accordions, tabs, tooltips, sliders, and `.sr-only` screen-reader helper classes designed for user experience and accessibility.

---

### Step 3: Assess Regional Enforcement (EEA vs. Non-EEA)

If auditing content related to **Site Reputation Abuse**:
* **Outside the EEA**: Violations trigger manual actions, demotions, or complete de-indexing in Google Search results.
* **Within the EEA**: Violations cause the section to be categorized as an **independent entity** detached from the host domain's sitewide authority (ranking on its own merits), rather than receiving a punitive manual action demotion.

---

### Step 4: Generate the Audit Report

Always format your audit deliverable using this structured markdown template:

```markdown
# Google Search Spam Policies Audit Report

**Target**: [URL / File / Content Title]
**Audit Date**: [Date]
**Overall Risk Status**: [CRITICAL RISK / WARNING / MINOR CONCERNS / CLEAN]

---

## 1. Executive Summary
Brief 2-3 sentence overview of compliance status, primary exposure points, and whether the content risks manual action or algorithmic demotion under Google Search Essentials.

## 2. Policy-by-Policy Findings

| Policy Category | Status | Risk Level | Key Finding / Evidence |
| :--- | :--- | :--- | :--- |
| **Scaled Content Abuse** | [Violated / Compliant] | [High/Med/Low/None] | [Summary of findings] |
| **Site Reputation Abuse** | [Violated / Compliant] | [High/Med/Low/None] | [Summary of findings] |
| **Link Spam & Thin Affiliation**| [Violated / Compliant] | [High/Med/Low/None] | [Summary of findings] |
| **Hidden Text & Micro-Links** | [Violated / Compliant] | [High/Med/Low/None] | [Summary of findings] |
| **Cloaking & Sneaky Redirects** | [Violated / Compliant] | [High/Med/Low/None] | [Summary of findings] |
| **Keyword Stuffing** | [Violated / Compliant] | [High/Med/Low/None] | [Summary of findings] |
| **Malicious / Misleading Functionality**| [Violated / Compliant] | [High/Med/Low/None] | [Summary of findings] |
| **Other Policies (Hacked, UGC, Expired)**| [Violated / Compliant] | [High/Med/Low/None] | [Summary of findings] |

## 3. Detailed Issue Breakdown
### Issue #1: [Policy Name]
* **Severity**: [High / Medium / Low]
* **Exact Code / Content Snippet**:
  ```html
  <!-- Offending snippet here -->
  ```
* **Official Policy Citation**: [Direct citation from Google Search Essentials]
* **Risk Explanation**: Why Google's automated systems or human reviewers flag this.
* **Remediation Action**: Exact code or editorial change required to resolve.

## 4. Prioritized Action Plan
1. **Critical Immediate Fixes (P0)**: Required to prevent or lift manual actions.
2. **Recommended Best Practices (P1)**: Quality enhancements to survive algorithmic core/spam updates.
```
