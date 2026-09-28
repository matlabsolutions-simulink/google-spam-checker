# Site Reputation Abuse ("Parasite SEO") & Regional Enforcement Guide

Google's **Site Reputation Policy** targets the practice commonly known in SEO as "Parasite SEO" — where third parties publish low-quality, commercial, or affiliate content on high-authority host domains primarily to exploit the host site's established ranking signals.

---

## 1. Core Definition & Principle

* **Third-Party Content**: Content created by an entity separate from the host site (e.g., white-label services, affiliate syndication networks, commercial sponsors, freelancers without editorial supervision).
* **The Violation**: Third-party content published on a host site **mainly because of that host's already-established ranking signals**, to rank better than it could on its own.
* **Presumption of Site-Wide Quality**: Google generally applies a presumption that individual pages (including new sections) match the overall quality of other pages on the domain. Site reputation abuse exploits this presumption.

---

## 2. The 4 Objective Evaluation Factors

When Google's systems or human reviewers assess whether content constitutes site reputation abuse, they examine whether the content was created with **sufficient input, editorial oversight, or contribution from the host site**:

| Factor | Critical Evaluation Question | Compliant Standard | Violation Indicator |
| :--- | :--- | :--- | :--- |
| **1. Presentation & UX** | Are design, typography, layout, and UX consistent with the main domain? | Uses identical typography, site navigation, header/footer, and responsive styling. | Disconnected template, missing site headers, different CMS styling, or isolated orphan subfolder. |
| **2. Quality Parity** | Does the content meet the editorial and factual quality standards of the host? | Thoroughly edited, fact-checked, meets journalistic or brand standards. | Shallow affiliate copy, automated text, exaggerated claims, or off-topic product reviews. |
| **3. Authorship & Responsibility** | Is there explicit acknowledgment of ownership and editorial responsibility? | Byline with named staff/editors, clear commercial disclosure, accessible customer support. | Anonymous bylines ("Staff", "Admin"), hidden commercial disclaimers, no editorial contact info. |
| **4. Multi-Site Duplication** | Does identical or near-identical content appear across multiple unrelated authority domains? | Unique, bespoke content commissioned exclusively for the host site. | Syndicated affiliate article or coupon feed identical to dozens of other newspapers/magazines. |

---

## 3. Clear Examples: Allowed vs. Prohibited

### Compliant / Safe Practices:
1. **Integrated Coupons & Deals Section**:
   * A publisher partners with a third-party coupon aggregator.
   * The subfolder is integrated into the site's main navigation and cross-referenced in related editorial articles/newsletters.
   * Clear commercial disclosure: *"Curated in partnership with X; editorially reviewed by our shopping team."*
   * Working feedback/report link managed under host's editorial contact standards.
2. **Specialist Freelancers with Editorial Oversight**:
   * A news site launches a recipe section using a third-party freelancer who also writes for other outlets.
   * The content is tailored specifically to the host publication, features real interviews, has an author bio, and follows site editorial guidelines.
3. **Syndicated News & Wire Services**:
   * Reuters, AP, or syndicated articles published with clear attribution.
4. **Legitimate Sponsored Content / Advertorials**:
   * Native advertising promoted directly to on-site readers (with `rel="sponsored"` on outbound links) rather than engineered to capture search queries on unrelated topics.
5. **Standard User-Generated Content**:
   * Moderated forum threads, product reviews, and comment sections.

### Prohibited / Abusive Practices:
1. **Unauthored Unrelated Affiliate Pages**:
   * A major business news site hosting an isolated guide on *"Best Online Casinos in the UK"* or *"Where to Buy CBD Oil"*.
   * The page is not linked from any category menu, has no named author or responsible editor, lacks commercial disclaimers, and copies text from an affiliate marketplace.
2. **Syndicated Payday Loan / Financial Reviews**:
   * An educational university subdomain or regional newspaper hosting syndicated reviews for high-interest loans created by a third-party marketing agency.
3. **Off-Topic Parasite Subdirectories**:
   * An established tech blog renting out `/coupons/` or `/diet-pills/` to an affiliate broker with zero tech editorial involvement.

---

## 4. Regional Enforcement: EEA vs. Non-EEA

Following regulatory review under European competition frameworks, Google maintains distinct enforcement mechanisms depending on where searchers are located:

### Outside the European Economic Area (Non-EEA):
* **Penalty**: If found in violation, pages are subject to **manual actions** or algorithmic demotions.
* **Impact**: The offending pages or entire sections may drop precipitously in rankings or be omitted from Google Search results globally (outside the EEA).
* **Notification**: Warning delivered via Google Search Console Manual Actions report.

### Within the European Economic Area (EEA):
* **Independent Categorization**: Violating sections are **categorized as separate from the main domain** rather than receiving a punitive manual action demotion.
* **Rank on Own Merits**: The presumption that the section inherits the domain's sitewide authority is removed. The section ranks strictly on its own merits against peers (e.g., casino section ranks against standalone casino sites).
* **No Contagion**: Manual action taken outside the EEA does not automatically count as a ranking penalty inside the EEA.
* **Dispute Resolution**: EEA webmasters have access to expedited reconsideration and alternative dispute resolution / mediation.

---

## 5. Audit Recommendations for Publishers

1. **Conduct an Inventory of All Subdomains & Subfolders**: Identify any sections operated by white-label partners, third-party content agencies, or affiliate syndicators.
2. **Enforce Unified Design & Navigation**: Ensure third-party sections share the main site's navigation, header/footer, and CSS styling.
3. **Mandate Editorial Review**: Every commercial article must be assigned to an in-house editor and reviewed before publication.
4. **Disclose Commercial Relationships**: Add prominent disclaimers explaining partnerships and vetting processes.
5. **Qualify Links**: Ensure all monetization links use `rel="sponsored"`.
6. **Exclude from Indexing if Oversight is Impossible**: If your team cannot provide active editorial governance over partner content, apply `noindex` or block via `robots.txt`.
