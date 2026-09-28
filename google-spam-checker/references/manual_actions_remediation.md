# Google Manual Actions & Spam Remediation Playbook

This playbook outlines how to diagnose, remediate, and submit reconsideration requests for manual actions triggered under Google Web Search Spam Policies.

---

## 1. Diagnosing Spam Penalties

### Step 1: Check Google Search Console (GSC)
* Navigate to **Security & Manual Actions** > **Manual Actions**.
* If a manual action is active, GSC displays:
  * **Reason**: Specific spam policy cited (e.g., *Site reputation abuse*, *Unnatural links to your site*, *Pure spam*, *Spammy structured markup*).
  * **Scope**: Whether the action applies to **Site-wide** or is restricted to **Partial matches** (specific URLs, subdirectories, or subdomains).

### Step 2: Algorithmic Spam Demotion vs. Manual Action
* **Manual Action**: Logged explicitly in GSC with a notification email. Requires a formal Reconsideration Request to clear.
* **Algorithmic Spam Update**: No entry in GSC Manual Actions. Traffic drops correlate with announced Google Search Spam Updates (e.g., March 2024 Core/Spam Update, August 2024 Spam Update). Does NOT require a reconsideration request; recovery occurs automatically when Googlebot recrawls and reevaluates the cleansed site.

---

## 2. Policy-by-Policy Remediation Checklist

### A. Scaled Content Abuse & Scraping
1. **Content Audit**: Identify all auto-generated, scraped, spun, or template-generated pages targeting keyword variations.
2. **Purge or Consolidate**: Delete thin pages and return `410 Gone` (preferred) or `404 Not Found`. Consolidate fragmented pages into high-value comprehensive resources.
3. **Inject Original Human Value**: Add first-hand testing, proprietary research, custom data, photography, or expert commentary.
4. **Prevent Future Generation**: Halt automated AI publishing workflows lacking human editorial gatekeeping.

### B. Link Spam (Outbound & Inbound)
1. **Outbound Links**:
   * Inspect all affiliate links, sponsored posts, paid guest articles, or partner links.
   * Add `rel="sponsored"` or `rel="nofollow"` to all commercial/affiliate links without exception.
2. **Inbound Links (Unnatural links to your site)**:
   * Perform a backlink audit using GSC Search Analytics and backlink data.
   * Contact webmasters of spammy link farms, PBNs, or low-quality directories requesting link removal.
   * Compile remaining toxic/unremovable domains into a Google Disavow text file (`domain:example.com`) and submit via the Google Disavow Links tool.

### C. Hidden Text & Link Abuse
1. Scan CSS files and template code for:
   * `display: none` or `visibility: hidden` containing keyword-stuffed copy.
   * Negative coordinate positioning (`left: -9999px`).
   * Zero font size or zero opacity.
   * Single-character micro-links (e.g., `<a href="...">.</a>`).
2. Remove deceptive CSS blocks or replace with compliant UI patterns (HTML5 `<details>`/`<summary>`, tabs, or tooltips).

### D. Hacked Content
1. Take site offline temporarily if actively serving malware or phishing.
2. Identify infection vector: outdated CMS core, vulnerable plugins, compromised FTP/SSH credentials, or database injection.
3. Restore code and database from a clean verified backup prior to infection date.
4. Update all software, themes, and plugins to latest patched versions.
5. In GSC, use URL Inspection to verify Googlebot fetches clean content, then request review.

### E. Site Reputation Abuse ("Parasite SEO")
1. **Unlink or Noindex Rogue Sections**: Immediately apply `noindex` meta tags or block crawling of third-party commercial content that lacks direct in-house editorial supervision.
2. **Bring Content In-House**: If retaining partner content, establish rigorous editorial control:
   * Restyle page templates to match site branding.
   * Assign named in-house staff editors.
   * Provide explicit commercial disclosures.
   * Ensure products/offers are vetted according to company standards.

### F. Sneaky Redirects & Cloaking
1. Remove IP/User-Agent detection logic from server configurations (`.htaccess`, Nginx configurations, edge workers).
2. Eliminate client-side conditional JavaScript redirects targeting Googlebot or mobile users.
3. Ensure Googlebot receives the identical content and DOM tree delivered to ordinary users.

---

## 3. Formulating a Reconsideration Request

When submitting a reconsideration request in Google Search Console, Google's webspam team requires transparency, humility, and documented evidence of remediation.

### The 4-Part Submission Structure:
1. **Direct Acknowledgment**: Clearly state what caused the violation and admit the breach of specific spam policies. Avoid making excuses or blaming third parties without accepting ultimate site ownership responsibility.
2. **Detailed Remediation Actions**:
   * Enumerate exact changes made (e.g., *"Removed 1,420 auto-generated doorway pages (HTTP 410); added rel='sponsored' to all 350 outbound affiliate links across 85 articles."*).
   * Provide a public link (e.g., Google Sheets or cloud document) documenting deleted URLs, modified pages, or backlink outreach efforts.
3. **Structural Governance & Prevention**:
   * Explain what editorial or technical guardrails have been implemented to ensure the violation cannot reoccur (e.g., new editorial review checklists, CMS plugins enforcing `rel="sponsored"`, automated malware monitoring).
4. **Closing & Verification**:
   * State that the site is now fully compliant with Google Search Essentials spam policies and respectfully request review.

### Sample Request Template:
```text
Dear Google Search Quality Team,

We are writing to request reconsideration for [domain.com] following a manual action for [Specific Policy, e.g., Unnatural Outbound Links / Scaled Content Abuse].

1. Root Cause Identification:
Upon thorough review, we identified that [describe exact issue, e.g., our editorial team published sponsored product features without properly enforcing rel="sponsored" attributes on affiliate links].

2. Steps Taken to Resolve the Issue:
- Conducted a full sitewide audit of all external links.
- Updated 128 published articles to add rel="sponsored" to all 412 commercial and affiliate links.
- Deleted 45 low-quality thin posts that did not meet our editorial standards (returning HTTP 410).
- Full audit log with before/after URLs is available here: [Link to Shared Document].

3. Prevention of Future Violations:
- Implemented a mandatory pre-publishing checklist in our CMS that automatically flags unlabelled commercial links.
- Conducted training for all contributing writers regarding Google Search Essentials spam policies.

We have thoroughly verified our site against all Google spam policies and are committed to maintaining strict quality standards going forward. We respectfully request that the manual action be lifted.

Sincerely,
[Name / Webmaster Team]
[Domain.com]
```
