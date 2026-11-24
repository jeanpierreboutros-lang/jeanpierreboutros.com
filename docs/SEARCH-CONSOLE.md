# Search registration and production verification

Documentation reconciled **24 November 2026**. Current content release is `04a1d8a`, with 41 live sitemap URLs and 30 project pages. The RY X page is published; its ingestion/indexing has not been checked in the search accounts. See [current live evidence](ry-x-qatar-philharmonic-live-verification-2026-11-24.json) and [session closeout](SESSION-CLOSEOUT-2026-11-24.md).

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
preserved. No remaining account sign-in or verification step is required.
Reports were processing when inspected on 16 November. They were not reopened during the RY X publication session; discovered URLs and accepted requests do not prove that every page is indexed or that a new version has been recrawled.

## Published release and future deployment checks

Canonical origin: https://www.jeanpierreboutros.com. HostGator’s Last Deployed SHA is `04a1d8a45c1a07b848330a511c640224243b9ed8`, observed at **24 November 2026, 00:06:42 (Asia/Qatar)**. All 41 pages and 196 referenced resources matched the reviewed release bytes. The three tested canonical redirect destinations and four 404 checks passed. See [the release report](RELEASE-2026-11-24.md). Documentation-only commits do not require deployment.

The 41 sitemap URLs comprise home, six services, 30 projects and four directories. The 51 studio release entries share one directory page. For the next search-account review, inspect `/projects/ry-x-qatar-philharmonic-doha/`, check the existing sitemap’s latest processed inventory and selected canonicals, and record actual observations. No new Google/Bing inspection, indexing request, sitemap-processing result or IndexNow submission was performed for RY X.

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
5. Confirm all 41 current sitemap URLs return 200 (update this inventory after later releases), and the live HTML/PDF/assets match
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

Also check that `studiojpb.com`, which shares the document root, has not acquired
the portfolio's domain redirects and that existing access restrictions still
work. Every redirect is conditional on this portfolio's two hostnames.

## Google Search Console maintenance

Ownership and submission are complete. These steps describe future properties,
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

Ownership and submission are complete using manual DNS verification. These steps
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
6. Consider IndexNow for future substantive changes after ownership is
   established. No IndexNow key was generated and no submission is claimed here.

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
The policy update was deployed in `c9521aa`; [27 focused live checks](ai-search-verification-2026-11-16.json) passed on 16 November. The RY X release retains that policy; `check_site.py` passed its robots access assertions across all 41 current sitemap URLs.
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

The 16 November release passed 4,980 local Schema.org property/domain/range checks across its 40 pages; that total was not rerun or extrapolated to the 41-page RY X release. The predeployment Apache fixture passed 59 HTTP/TLS checks,
including cache and shared-host isolation. Public byte checks and Google/Bing
live fetches are now recorded in the release evidence. The published Shareet
URL passed Schema.org with zero errors/warnings and Google's Rich Results Test
with four valid supported items and noncritical optional-field notices. The
later snippet refinement passed local checks and Bing's final live test with no
SEO/GEO issues. A new full mobile/keyboard interaction matrix and field Core Web
Vitals measurement were not performed after deployment; earlier local checks
retain their original scope. See [the release report](RELEASE-2026-11-16.md).


## Prepared local audit candidate — 24 November 2026

The new [audit report](SEO-AUDIT-2026-11-24.md) describes an unpublished 42-page
candidate. Keep the existing verified Google/Bing properties and DNS records.
After an authorized deployment, inspect `/audio-software-developer/`, refresh the
existing sitemap, verify selected canonicals and retry public PageSpeed tests.
The `studiojpb.com` alias currently serves portfolio pages with a www portfolio
canonical; inspect selected canonicals before deciding on that separate domain.

`indexnow-key.txt` is prepared public ownership proof, and `indexnow.py` defaults
to offline preparation. The deployment manifest includes the key. No IndexNow
submission has occurred. After the exact candidate is live, use `--url` for
changed canonical URLs and explicitly add `--submit`. The tool verifies the live
key and exact selected page bytes before sending; stale HTML stops submission.
See [the prepared payload](indexnow-prepared-2026-11-24.json). This does not submit
to Google or prove indexing. Existing registration instructions above remain
valid; no new fabricated verification meta tags were introduced.
