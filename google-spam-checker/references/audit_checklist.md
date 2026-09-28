# Google Spam Policies Audit Checklist

Use this structured 6-phase checklist when conducting a manual or assisted SEO spam audit on any page, URL, or domain.

---

## Phase 1: Domain Architecture & History
- [ ] **Expired Domain Exploitation Check**:
  - Review historical WHOIS registration and Wayback Machine snapshots.
  - Has the domain shifted from a public/civic/educational/medical non-profit to a commercial affiliate, casino, or loan site?
  - Do legacy backlink anchors mismatch the current topic?
- [ ] **Doorway & Network Architecture**:
  - Are there dozens of repetitive regional landing pages (e.g., `/service-in-[city]`) without genuine local business presence?
  - Does the site deploy multiple similar domain names funneling traffic to a single destination?
- [ ] **Subdomain & Parasite Isolation**:
  - Are third-party commercial subdomains or subdirectories (e.g., `/coupons/`, `/reviews/`, `shop.*`) isolated from the main site's editorial team?

---

## Phase 2: Technical Crawling & Rendering
- [ ] **Cloaking Verification**:
  - Fetch page as Googlebot (`User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)`) and compare HTML against normal browser fetch.
  - Verify that no IP/User-Agent based redirection or dynamic text swapping occurs.
  - If content is paywalled, verify Google Flexible Sampling compliance and `isAccessibleForFree` schema markup.
- [ ] **Sneaky Redirection & Mobile Traps**:
  - Inspect for `<meta http-equiv="refresh">` tags with external target URLs.
  - Emulate mobile user-agents to confirm mobile visitors are not routed to unexpected ad networks or paywall traps.
  - Inspect JavaScript for `window.location.replace` or `navigator.userAgent` sniffing.
- [ ] **Back-Button Integrity**:
  - Test browser back-button behavior: does clicking back return directly to the search engine or trap the user in history loops (`history.pushState`)?

---

## Phase 3: DOM, CSS & On-Page Elements
- [ ] **Hidden Text Scan**:
  - Search CSS for `display: none` or `visibility: hidden` containing non-UI keyword text.
  - Check for extreme negative margins/indents (`text-indent: -9999px; left: -9999px`).
  - Check for font size 0 (`font-size: 0px`) or opacity 0 (`opacity: 0`).
  - Check for matched text and background colors (`#ffffff` on `#ffffff`, `#000000` on `#000000`).
  - *Distinguish from legitimate UI*: confirm that hidden elements are not standard accordions, tabs, tooltips, or `.sr-only` accessibility helpers.
- [ ] **Micro-Link / Stealth Anchor Scan**:
  - Inspect hyperlinks with 1-character anchors (periods, hyphens, commas).
  - Inspect empty `<a>` tags with external target URLs.
- [ ] **Keyword Density & Repetition**:
  - Analyze unigram and bigram frequency. Are key commercial queries repeated at >4-5% density?
  - Are there blocks of out-of-context postal codes, phone numbers, or city lists?

---

## Phase 4: Content Substance & Generation Integrity
- [ ] **Scaled Content & AI Fingerprinting**:
  - Does the page exhibit low lexical diversity (Type-Token Ratio < 0.22) and repetitive boilerplate phrasing?
  - Are there visible AI artifact phrases (e.g., *"As an AI language model...", "In conclusion, it is important to remember..."*)?
  - Does the content provide primary human insights, proprietary research, custom photography, or empirical test data?
- [ ] **Scraping & Syndication Audit**:
  - Does the text verbatim match earlier published third-party articles without substantial original analysis or commentary?
  - Is content feed-generated or synthesized via superficial automated synonym replacement?
- [ ] **Misleading Functionality / Fake Tools**:
  - Does the page promise a utility (PDF merge, keygen, app credit generator) that fails to deliver and instead gates behind survey/offer lockers?

---

## Phase 5: Outbound & Monetization Links
- [ ] **Affiliate Link Qualification**:
  - Are all affiliate links, Amazon associates links, and tracking parameters explicitly qualified with `rel="sponsored"` or `rel="nofollow"`?
- [ ] **Sponsored & Paid Links**:
  - Are paid editorial features, advertorials, or guest posts flagged with `rel="sponsored"` on external target links?
- [ ] **Link Scheme Participation**:
  - Are there sitewide reciprocal footer link exchanges or distributed theme/widget backlinks passing ranking credit?

---

## Phase 6: Trust, Transparency & Safety
- [ ] **Site Reputation Abuse (Parasite SEO)**:
  - If content is third-party or affiliate, is it fully integrated into the publication's design, hierarchy, and editorial standards?
  - Is there a clear named author or editor responsible for the content?
  - Are commercial disclosures clearly displayed?
- [ ] **Malicious Software & Security**:
  - Ensure zero unauthorized executables, deceptive installers, or browser-hijacking scripts.
  - Verify that SSL/TLS certificates are valid and no malware warnings appear in GSC Security Issues.
- [ ] **User-Generated Content Oversight**:
  - Are public forums and comment sections protected against bot spam via CAPTCHA or moderation?
  - Are user-submitted links configured with `rel="ugc"` or `rel="nofollow"`?
