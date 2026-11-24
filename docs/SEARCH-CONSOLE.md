# Search registration and production verification

**Latest domain consolidation, 24 November 2026:** content commit `252b41f` is
live with 480 passing migration checks. The retired StudioJPB web hosts now
redirect to the primary origin while DNS/mail stay unchanged. Old-domain
Google/Bing ownership and Google Change of Address remain manual steps in the
[migration report](DOMAIN-MIGRATION-2026-11-24.md); no migration filing is claimed.

Documentation reconciled **24 November 2026**. The final deployed runtime is
`252b41f`; the final recheck repeats 480 migration and 243 primary HTTP requests
without unexpected failures. Google/Bing primary sitemaps show Success with 42
discovered URLs. Google manual-action and security reports show no issues.
Its aggregate indexing view is dated 16 November: its 42 indexed count does not
establish indexing of every current URL; its three exclusions are the intended
HTTP/non-www homepage redirects. See the [final recheck](domain-migration-recheck-2026-11-24.json)
and [session closeout](SESSION-CLOSEOUT-2026-11-24.md). Earlier SEO indexing
requests and the 42-URL IndexNow HTTP 202 receipt retain their publication scope.

Registration was completed **16 November 2026** for release `239f127`. The table below records that dated account observation.
See [the release report](RELEASE-2026-11-16.md) and
[verification evidence](portfolio-release-verification-2026-11-16.json).

| Platform | Result observed on 16 November 2026 |
| --- | --- |
| Google Search Console | Domain `jeanpierreboutros.com` verified by DNS TXT; sitemap processed successfully, 40 discovered pages |
| Bing Webmaster Tools | Canonical HTTPS www property verified by DNS CNAME; sitemap Success, 40 URLs, zero sitemap errors/warnings |
| Priority URLs | Home and Shareet indexing requests accepted by both platforms; Google live tests passed; final Bing Shareet live test can be indexed with no SEO/GEO issues |

The sitemap is `https://www.jeanpierreboutros.com/sitemap.xml`. Retain the
verification DNS records; the existing SPF, mail and other DNS records were
preserved. Primary-domain verification is complete; old-domain Google/Bing
ownership and Google Change of Address remain open.
Reports were processing when inspected on 16 November. They were not reopened during the RY X publication session; discovered URLs and accepted requests do not prove that every page is indexed or that a new version has been recrawled.

## Published release and future deployment checks

Canonical origin: https://www.jeanpierreboutros.com. HostGator's Last Deployed SHA is `252b41f3414f03f202db2e5b55626369730d8002`, displayed at **24 November 2026, 13:22:10 (Asia/Qatar)**. The final recheck confirms 42 primary pages, 162 referenced resources and three discovery files match, plus 480 successful migration checks. See the [migration report](DOMAIN-MIGRATION-2026-11-24.md) and [recheck](domain-migration-recheck-2026-11-24.json). Documentation-only commits do not require another deployment.

The current inventory is home, six service pages, 30 project pages, four directories
and one software page. The 51 studio release entries share one directory page.
Google and Bing both show sitemap Success with 42 URLs. Google accepted requests
for home, the software page and RY X; Bing accepted the software page. The final
Bing live test reports no SEO/GEO issues. Existing DNS ownership verification is
retained. Search accounts may still show older indexed versions until recrawling.

For future website changes:

1. Run `python3 build.py`, `python3 check_site.py`, `node --check main.js`,
   `sh -n hosting/install-seo.sh` and `git diff --check`.
2. Review the homepage, a service page, a project page, the studio-credit directory and the mobile navigation.
   Test a homepage card, its photo viewer, Escape, a direct legacy project hash,
   the full project link, service links and the three profile downloads.
3. Push the reviewed release to `main`. In the existing HostGator cPanel Git
   repository, use **Update from Remote**, confirm the intended HEAD, then
   **Deploy HEAD Commit**. Confirm the Last Deployed SHA.
4. The existing `.cpanel.yml` copies new assets and pages first. Its installer
   prepends the domain-scoped JPB redirects while retaining the other .htaccess
   rules. Backups are private under the repository's `.deployment-backups/`.
   An invalid existing managed block or symlinked .htaccess stops installation.
5. Confirm all 42 current sitemap URLs return 200 (update this inventory after later releases), and the live HTML/PDF/assets match
   the release. Verify these examples:

| Request | Expected result |
| --- | --- |
| `http://jeanpierreboutros.com/` | 301 to `https://www.jeanpierreboutros.com/` |
| `http://www.jeanpierreboutros.com/` | 301 to the same HTTPS canonical |
| `https://jeanpierreboutros.com/` | 301 to the HTTPS www canonical |
| `https://www.jeanpierreboutros.com/` | 200, self-canonical |
| `/live-sound-engineer` | 301 to `/live-sound-engineer/` |
| `/projects/nancy-ajram-olympia/index.html` | 301 to `/projects/nancy-ajram-olympia/` |
| An unknown URL | Actual 404 |
| A fingerprinted `.woff2` asset | 200, `font/woff2`, immutable cache header |
| `/styles.css?v=<current 12-character build hash>` | 200, immutable cache header |

The separate [domain migration](DOMAIN-MIGRATION-2026-11-24.md) now authorizes
consolidating the retired `studiojpb.com` website on the same document root.
Verify its reviewed page mappings and operational exceptions, and keep existing
access restrictions, email hosts and all other hosted domains intact.

## Google Search Console maintenance

Primary-domain ownership and submission are complete. Old-domain migration steps
are in the [migration report](DOMAIN-MIGRATION-2026-11-24.md). The steps below describe future properties,
verification recovery and routine review; reuse the existing verified property.

Official setup: https://search.google.com/search-console

1. Sign in with the account that should own the website's search property.
2. If the property already exists, use it and retain its current verification.
   Otherwise choose **Add property → Domain** and enter `jeanpierreboutros.com`.
3. Google supplies a unique DNS TXT value. Add that exact value at the domain's
   authoritative DNS provider, using the host/name Google specifies. Do not
   replace unrelated TXT records. Wait for propagation and choose **Verify**.
4. For a URL-prefix property instead, use `https://www.jeanpierreboutros.com/`
   and complete one of Google's offered verification methods with the real
   token or file. The site currently emits no fabricated verification tag.
5. After the release is public, open **Sitemaps** and submit
   `https://www.jeanpierreboutros.com/sitemap.xml`.
6. Inspect the homepage, `/services/`, `/studio-credits/`, `/live-sound-engineer/` and a project URL
   with **URL inspection → Test live URL**. Confirm crawl access, the rendered
   content and the declared canonical. Request indexing for important pages
   using the available interface.
7. Review **Page indexing**, **Sitemaps**, **Core Web Vitals** and **Performance**.
   Allow time for recrawling; submission does not establish indexing or rankings.

Ownership reference: https://support.google.com/webmasters/answer/9008080

## Bing Webmaster Tools maintenance

Primary-domain ownership and submission are complete using manual DNS verification. These steps
describe future properties or verification recovery; reuse the existing site.

Official setup: https://www.bing.com/webmasters/

1. Sign in to the account that should own the search property.
2. Import the verified property from Google Search Console, or add
   `https://www.jeanpierreboutros.com/` manually.
3. Complete the offered verification with Bing's actual DNS value, XML file or
   meta tag. Preserve existing ownership verification records.
4. In **Sitemaps**, submit `https://www.jeanpierreboutros.com/sitemap.xml`.
5. Use **URL inspection** for the homepage, studio directory, a service and a project record.
   Review indexing issues and Search Performance after Bing recrawls the site.
   When available, review **AI Performance** for supported Microsoft/partner
   citation and grounding-query reports. These are not counts for every AI assistant.
6. IndexNow is now prepared and its initial 42-URL notification returned HTTP 202.
   For future substantive changes, use the explicit submission tool after publication.
   A receipt does not establish indexing.

Verification reference:
https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b

## Structured-data verification after publication

- Open https://validator.schema.org/ and test the homepage, studio-credit directory, a service URL and
  a project URL. Check Person, Organization, Service, WebSite, WebPage,
  ProfilePage, Article, ItemList, OfferCatalog and BreadcrumbList relationships.
- Open https://search.google.com/test/rich-results and test representative
  public URLs. Service is valid Schema.org vocabulary but is not itself a
  promise of a Google rich-result feature. The site does not publish ratings,
  fake reviews, unsupported LocalBusiness details or FAQ rich-result claims.
- The local checker can additionally validate property domains and ranges:

    python3 check_site.py --vocabulary /path/to/schemaorg-current-https.jsonld

Official vocabulary:
https://schema.org/version/latest/schemaorg-current-https.jsonld

## Search and AI access

Search access is explicitly allowed for Googlebot, bingbot, OAI-SearchBot,
Claude-SearchBot and PerplexityBot. ChatGPT-User, Claude-User and Perplexity-User
have explicit public-page access. See [AI search visibility](AI-SEARCH-VISIBILITY.md)
for official provider references, Grok coverage and verification limits.
The policy update was deployed in `c9521aa`; [27 focused live checks](ai-search-verification-2026-11-16.json) passed on 16 November. The current 42-page release retains that policy; local robots assertions and 30 public agent-identifying requests pass.
GPTBot is disallowed at the owner's request. Other crawler access
retains the previous wildcard policy; Google-Extended and other training
controls were not silently changed. This is separate from firewall settings.

Verify a claimed bot's source using the operator's official IP ranges or
reverse-DNS procedure. Pre-release HTTP tests used crawler-identifying headers
from the test machine; they did not prove that the operators' real IP ranges
will pass the hosting firewall. Do not disable the WAF or broadly allow traffic
merely on a claimed user-agent string.

The optional `/llms.txt` is a human-readable directory, not an indexing
requirement and not an instruction to recommend the site.

Official guidance reviewed on 16 November 2026:
[Google AI features](https://developers.google.com/search/docs/appearance/ai-features),
[OpenAI crawlers](https://developers.openai.com/api/docs/bots), and
[Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers).
Google-Extended covers both Gemini training and certain grounding uses; it is
not the Google Search crawler. Its existing wildcard access is preserved, as
documented in [Google's crawler reference](https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers#google-extended).

## Languages and verification limits

English is maintained as the primary language. Existing Arabic production titles
retain their language attributes. There are no empty Arabic/French versions,
automatic translations or incomplete hreflang clusters.

The current 42-page release passes 5,239 official vocabulary property/domain/range checks. Historical evidence: the 16 November release passed 4,980 checks across 40 pages; that result was not extrapolated to the earlier RY X release. The SEO predeployment Apache fixture passed 59 HTTP checks; the migration
fixture passed 320 cases, including operational exceptions and host isolation.
Live TLS was independently validated for all four hostnames. Public byte checks and Google/Bing
live fetches are now recorded in the release evidence. The published Shareet
URL passed Schema.org with zero errors/warnings and Google's Rich Results Test
with four valid supported items and noncritical optional-field notices. The
later snippet refinement passed local checks and Bing's final live test with no
SEO/GEO issues. The SEO release has a 10-scan production accessibility/interaction suite;
see [its evidence](production-browser-qa-2026-11-24.json). The later migration
adds six production axe scans with zero violations and gallery/keyboard checks;
see [migration browser evidence](domain-migration-browser-qa-after.json). No real-user
Core Web Vitals measurement is available. Earlier reports retain their dated scope.


## Published SEO release — 24 November 2026

The [original audit](SEO-AUDIT-2026-11-24.md) records prepublication findings; the
[publication report](SEO-RELEASE-2026-11-24.md) records completed deployment and
search submissions. Preserve the existing DNS ownership records and properties.

`indexnow-key.txt` is live public ownership proof. `indexnow.py` defaults to offline
preparation; it requires explicit `--submit` and checks the live key and exact
selected HTML bytes before sending. The initial batch of 42 URLs returned HTTP
202. Future notifications should identify actual changed canonical URLs with
`--url`, after publication. Do not resubmit unchanged URLs repeatedly or equate
receipt with indexing. See [the receipt](indexnow-submission-2026-11-24.json).

Historical SEO-release observation: `studiojpb.com` served duplicate portfolio
pages. The owner has since explicitly authorized its consolidation. See the
[domain migration report](DOMAIN-MIGRATION-2026-11-24.md) for current redirect
validation and the prepared Google Change of Address procedure. In the inspected
Google account only the new domain property is currently available; no old-domain
ownership or submitted Change of Address is claimed. DNS and email records remain
unchanged.
