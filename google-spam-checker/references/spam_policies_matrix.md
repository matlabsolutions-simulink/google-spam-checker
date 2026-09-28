# Google Web Search Spam Policies Matrix

This document provides a comprehensive breakdown of all spam policies defined in Google Search Essentials (updated August 2024 / current). It outlines violation mechanics, illustrative examples, legitimate exceptions, and automated/manual penalties.

---

## 1. Cloaking
* **Definition**: Presenting different content or URLs to human users and search engines with the intent to manipulate rankings and deceive users.
* **Prohibited Practices**:
  * Serving a travel/destination page to Googlebot while redirecting or serving discount pharmaceuticals or casino pages to human users.
  * Dynamically injecting keywords, hidden links, or entire text blocks only when the requesting user-agent matches Googlebot or search engine crawlers.
  * Serving stripped-down, clean HTML to crawlers while serving aggressive pop-unders, lockers, or malware to visitors.
* **Legitimate Exceptions**:
  * **Flexible Sampling / Paywalls**: Gated content (metered or lead-in) is NOT considered cloaking if Googlebot is allowed to crawl the full content and structured data (`NewsArticle` / `isAccessibleForFree`) is implemented per Google guidelines.
  * **Responsive / Adaptive Serving**: Serving mobile-optimized HTML/CSS via responsive design or Dynamic Serving (`Vary: User-Agent`) is allowed, provided the substantive content and user intent match.
* **Audit Checks**:
  * Compare rendered DOM fetched via Googlebot user-agent (`User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`) versus standard browser user-agent.
  * Inspect server configuration (`.htaccess`, Nginx config, Cloudflare Workers) for IP or User-Agent conditional routing.

---

## 2. Doorway Abuse
* **Definition**: Creating multiple pages or sites designed to rank for specific, closely related search queries that funnel visitors into a single generic destination or intermediate landing page.
* **Prohibited Practices**:
  * Creating dozens of nearly identical city/region landing pages (e.g., `/plumber-dallas`, `/plumber-fort-worth`, `/plumber-arlington`) that merely swap the city name and offer no localized value or distinct local business presence.
  * Multiple domain names with minor variations targeting the same query cluster, all funneling into a central sales portal.
  * Automatically generated bridge pages whose sole purpose is capturing organic traffic and instantly redirecting or forcing a click to the actual usable page.
* **Legitimate Exceptions**:
  * Distinct physical locations or genuine local service branches with unique staff, unique addresses, real local reviews, and localized services.
  * Clean, navigable category hierarchies with unique editorial curation.

---

## 3. Expired Domain Abuse
* **Definition**: Purchasing an expired, historically authoritative domain name and repurposing it primarily to manipulate search rankings by hosting low-quality, commercial, or unrelated content.
* **Prohibited Practices**:
  * Purchasing an expired government agency or municipal site (`.gov` or civic domain) to host commercial payday loan, crypto, or affiliate review content.
  * Buying an expired medical non-profit domain to sell commercial weight-loss pills or unlicensed pharmaceuticals.
  * Buying an elementary school or university club domain to launch a casino, sports betting, or essay-writing portal.
  * Attempting to capitalize on the residual backlink equity and trust signals of a defunct organization for unrelated commercial gain.
* **Audit Checks**:
  * Check Wayback Machine / WHOIS history: has the domain changed ownership, topic niche, or language drastically?
  * Do inbound links reference an academic, civic, or non-profit institution while the current page sells commercial goods or affiliate promotions?

---

## 4. Hacked Content
* **Definition**: Any content, script, or page placed on a site without the site owner's knowledge or authorization due to security vulnerabilities.
* **Prohibited Practices**:
  * **Code Injection**: Malicious JavaScript or hidden iframes injected into header/footer templates to drive stealth downloads, cryptocurrency mining, or redirect loops.
  * **Page Injection**: Thousands of auto-generated spam pages (e.g., Japanese keyword spam, pharma subdirectories `/viagra/`, `/cialis/`) added directly to the file system or database.
  * **Content Injection**: Subtle injection of spam links or hidden text into legitimate existing blog posts or resource pages.
  * **Conditional Server Redirects**: Server-level malware (`.htaccess` tampering) that redirects visitors arriving from Google Search results to scam pages while serving normal content to direct visitors or webmasters.
* **Remediation**: Immediate malware scanning, restoring from clean backup, changing all credentials, updating CMS/plugins, auditing server configs, and requesting Search Console review.

---

## 5. Hidden Text and Link Abuse
* **Definition**: Placing text, keywords, or hyperlinks on a page in a manner intended solely for search engine crawlers while hiding them from human visitors.
* **Prohibited Practices**:
  * White text on a white background (`color: #fff; background: #fff;`).
  * Text positioned entirely off-screen using extreme negative margins or coordinates (`text-indent: -9999px;`, `position: absolute; left: -10000px;`).
  * Setting font size or opacity to zero (`font-size: 0px;`, `opacity: 0;`).
  * Hiding text behind images or overlapping elements via CSS z-index abuse.
  * Hiding hyperlinks behind a single character, tiny period, or punctuation mark (e.g., `<a href="...">.</a>`).
* **Legitimate Exceptions (UX Enhancements)**:
  * Accordions and tabbed interfaces that toggle visibility upon user interaction.
  * Image carousels and sliders cycling through text or images.
  * Interactive tooltips that show additional explanatory text on hover/focus.
  * Screen-reader text (e.g., `.sr-only` CSS class) used to provide accessibility descriptions for assistive technologies.

---

## 6. Keyword Stuffing
* **Definition**: Loading a webpage with repetitive keywords or numbers in an attempt to manipulate Google Search rankings, resulting in an unnatural reading experience.
* **Prohibited Practices**:
  * Lists of phone numbers, zip codes, or geographic locations without substantive commentary or context.
  * Dense repetition of exact-match keyword variations within a single paragraph (e.g., *"We sell custom coffee mugs. If you want custom coffee mugs, our custom coffee mugs are the best custom coffee mugs for your custom coffee mug needs."*).
  * Out-of-context blocks of text stuffed into image alt tags, footer blocks, or meta tags.

---

## 7. Link Spam
* **Definition**: Creating, buying, or selling links to or from a site primarily to manipulate search rankings rather than providing genuine editorial value.
* **Prohibited Practices**:
  * Exchanging money, goods, or services for links or posts containing links that pass PageRank.
  * Sending "free" products to bloggers/reviewers in exchange for a review that includes a dofollow link.
  * Excessive reciprocal link exchanges ("Link to me and I will link to you") or dedicated partner link farm pages.
  * Using automated link-building programs, software, or submission services.
  * Contractual or Terms of Service link mandates requiring clients/users to host dofollow backlink attribution.
  * Native advertising, sponsored articles, or advertorials where links are not qualified with `rel="sponsored"` or `rel="nofollow"`.
  * Keyword-rich anchor links embedded in distributed widgets, themes, or footer templates across thousands of sites.
  * Spammy forum comments or signatures with optimized keyword links.
* **Required Qualification**:
  * Commercial & paid links: `rel="sponsored"`
  * User-generated or untrusted links: `rel="ugc"`
  * General non-endorsed links: `rel="nofollow"`

---

## 8. Machine-Generated Traffic
* **Definition**: Sending automated queries or scraping Google Search results without express authorization.
* **Prohibited Practices**:
  * Automated rank-checking scripts directly hitting Google Search without using official APIs.
  * Automated scraping bots extracting SERP snippets, Knowledge Panels, or AI Overviews at volume.

---

## 9. Malicious Practices
* **Definition**: Deceiving user expectations or compromising user security, device integrity, or privacy.
* **Prohibited Practices**:
  * **Malware**: Hosting or distributing malicious executables, trojans, ransomware, or spyware.
  * **Unwanted Software**: Distributing installers that secretly alter homepages, hijack default search providers, bundle unwanted adware, or harvest personal data without explicit consent.
  * **Back-Button Hijacking**: Manipulating browser history (`history.pushState` loops or popstate traps) to prevent users from navigating backward to their original search results.

---

## 10. Misleading Functionality
* **Definition**: Intentionally creating web pages that claim to offer a specific tool, utility, or content, but in reality do not provide it and instead trap the user into deceptive advertising or fake downloads.
* **Prohibited Practices**:
  * Sites claiming to be a "Free App Store Credit Generator", "V-Bucks Generator", or "Steam Key Generator" that force users into surveys or endless ad loops.
  * Sites claiming to provide functional online tools (e.g., "Free PDF Merger", "Countdown Timer", "File Converter") that contain only dummy UI elements and route users to unrelated sponsored software downloads.

---

## 11. Scaled Content Abuse
* **Definition**: Generating large volumes of unoriginal, low-value pages primarily to manipulate search rankings, regardless of whether created via generative AI, scraping, or manual curation.
* **Prohibited Practices**:
  * Using generative AI (LLMs) to produce hundreds or thousands of shallow articles targeting long-tail queries without adding unique data, expert review, or real insights.
  * Scraping feeds, search results, or databases and running automated synonym substitution, translation, or spinning.
  * Stitching together excerpts from multiple third-party articles to simulate an original post.
  * Operating multiple separate domains or subdomains to disguise the mass-scale nature of the content operation.
  * Generating mass pages that make little semantic sense but are stuffed with query variations.
* **Standard**: Does the content demonstrate original human effort, empirical evidence, unique testing, or proprietary value? If not, it is subject to algorithmic demotion or manual action.

---

## 12. Scraping
* **Definition**: Taking content from other websites—often automated—and publishing it without adding original value, context, or critical contribution.
* **Prohibited Practices**:
  * Republishing third-party articles verbatim without permission, commentary, or attribution.
  * Copying content and making superficial modifications (automated synonym replacement, altering word order).
  * Republishing RSS feeds or API streams without providing unique synthesis or editorial framing.
  * Compiling video/image galleries from other sites with zero unique curation or original analysis.

---

## 13. Site Reputation Abuse ("Parasite SEO")
* **Definition**: Publishing third-party content on an established, authoritative host site primarily to exploit that host site's ranking signals, where the host has minimal editorial oversight and the content is disconnected from the host's primary purpose.
* **Key Factors**:
  * Is the content created with genuine editorial oversight and integration by the host publisher?
  * Is the UX, branding, and standard of quality consistent with the host site?
  * Is there clear attribution and editorial responsibility?
  * Is the same third-party content syndicated across numerous unrelated authority domains?
* *See `site_reputation_and_eea.md` for complete regional policy distinctions.*

---

## 14. Sneaky Redirects
* **Definition**: Intentionally sending a visitor to a different URL than requested to deceive users or search engines.
* **Prohibited Practices**:
  * Showing search engines an informational article while redirecting human visitors to a commercial or scam page.
  * Serving desktop visitors normal content while silently redirecting mobile visitors to a subscription trap or unrelated affiliate offer.
* **Legitimate Exceptions**:
  * Permanent 301/308 redirects for site migrations or consolidated URLs.
  * Redirecting authenticated users to their account dashboard.
  * Geotargeting redirects when implemented transparently with user override options.

---

## 15. Thin Affiliation
* **Definition**: Publishing pages with commercial affiliate links where product descriptions, specifications, and reviews are directly copied from merchant sites without adding original insight, comparison, or testing.
* **Prohibited Practices**:
  * Cookie-cutter affiliate websites using turnkey templates and merchant product feeds.
  * "Review" pages that simply rephrase manufacturer marketing copy without hands-on testing, original photos, or benchmarks.
* **Legitimate Best Practices**:
  * Providing original hands-on testing, pros/cons, unique comparison tables, price tracking, or genuine buying advice.
  * Qualifying all outbound affiliate links with `rel="sponsored"` or `rel="nofollow"`.

---

## 16. User-Generated Spam
* **Definition**: Spammy content injected into public forums, comment sections, guestbooks, or user profiles by third-party spammers due to lack of moderation.
* **Prohibited Practices**:
  * Automated bot accounts creating profile bios stuffed with commercial casino/crypto links.
  * Blog comment sections overrun with generic comments containing keyword links.
  * Open file-upload directories hosting malicious or copyrighted files.
* **Remediation**:
  * Implement CAPTCHA / anti-bot verification for account creation and commenting.
  * Automatically apply `rel="ugc"` or `rel="nofollow"` to all user-submitted links.
  * Enforce moderation queues for new users or links.

---

## 17. Other Demotions & Removals
* **Legal Removals**: Valid DMCA copyright notices, defamation complaints, counterfeit goods notices, CSAM (mandatory removal and site demotion).
* **Personal Information Removals**: Sites with exploitative removal practices, non-consensual explicit imagery, doxxing.
* **Policy Circumvention**: Creating new subdomains, subdirectories, or replacement domains to bypass algorithmic or manual spam actions.
* **Scam & Fraud**: Impersonating established businesses, faux customer support helplines, deceptive banking or payment portals.
