# Search registration and production verification

Prepared 2 November 2026. No Google Search Console or Bing Webmaster Tools
registration, ownership verification or sitemap submission has been performed by
this implementation. No verification tokens were supplied or invented.

## Publish and verify first

The canonical origin is https://www.jeanpierreboutros.com, retaining the website's
existing canonical choice. The prepared release has 28 canonical HTML pages.

1. Run `python3 build.py`, `python3 check_site.py`, `node --check main.js`,
   `sh -n hosting/install-seo.sh` and `git diff --check`.
2. Review the homepage, a service page, a project page and the mobile navigation.
   Test a homepage card, its photo viewer, Escape, a direct legacy project hash,
   the full project link, service links and the three profile downloads.
3. Push the reviewed release to `main`. In the existing HostGator cPanel Git
   repository, use **Update from Remote**, confirm the intended HEAD, then
   **Deploy HEAD Commit**. Confirm the Last Deployed SHA.
4. The existing `.cpanel.yml` copies new assets and pages first. Its installer
   prepends the domain-scoped JPB redirects while retaining the other .htaccess
   rules. Backups are private under the repository's `.deployment-backups/`.
   An invalid existing managed block or symlinked .htaccess stops installation.
5. Confirm all 28 sitemap URLs return 200, and the live HTML/PDF/assets match
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

Also check that `studiojpb.com`, which shares the document root, has not acquired
the portfolio's domain redirects and that existing access restrictions still
work. Every redirect is conditional on this portfolio's two hostnames.

## Google Search Console

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
6. Inspect the homepage, `/services/`, `/live-sound-engineer/` and a project URL
   with **URL inspection → Test live URL**. Confirm crawl access, the rendered
   content and the declared canonical. Request indexing for important pages
   using the available interface.
7. Review **Page indexing**, **Sitemaps**, **Core Web Vitals** and **Performance**.
   Allow time for recrawling; submission does not establish indexing or rankings.

Ownership reference: https://support.google.com/webmasters/answer/9008080

## Bing Webmaster Tools

Official setup: https://www.bing.com/webmasters/

1. Sign in to the account that should own the search property.
2. Import the verified property from Google Search Console, or add
   `https://www.jeanpierreboutros.com/` manually.
3. Complete the offered verification with Bing's actual DNS value, XML file or
   meta tag. Preserve existing ownership verification records.
4. In **Sitemaps**, submit `https://www.jeanpierreboutros.com/sitemap.xml`.
5. Use **URL inspection** for the homepage, a service and a project record.
   Review indexing issues and Search Performance after Bing recrawls the site.
6. Consider IndexNow for future substantive changes after ownership is
   established. No IndexNow key was generated and no submission is claimed here.

Verification reference:
https://www.bing.com/webmasters/help/add-and-verify-site-12184f8b

## Structured-data verification after publication

- Open https://validator.schema.org/ and test the homepage, a service URL and
  a project URL. Check Person, Organization, Service, WebSite, WebPage,
  ProfilePage, Article, OfferCatalog and BreadcrumbList relationships.
- Open https://search.google.com/test/rich-results and test representative
  public URLs. Service is valid Schema.org vocabulary but is not itself a
  promise of a Google rich-result feature. The site does not publish ratings,
  fake reviews, unsupported LocalBusiness details or FAQ rich-result claims.
- The local checker can additionally validate property domains and ranges:

    python3 check_site.py --vocabulary /path/to/schemaorg-current-https.jsonld

Official vocabulary:
https://schema.org/version/latest/schemaorg-current-https.jsonld

## Search and AI access

Search access is explicitly allowed for Googlebot, bingbot, OAI-SearchBot and
PerplexityBot. GPTBot is disallowed at the owner's request. Other crawler access
retains the previous wildcard policy; Google-Extended and other training
controls were not silently changed. This is separate from firewall settings.

Verify a claimed bot's source using the operator's official IP ranges or
reverse-DNS procedure. Pre-release HTTP tests used crawler-identifying headers
from the test machine; they did not prove that the operators' real IP ranges
will pass the hosting firewall. Do not disable the WAF or broadly allow traffic
merely on a claimed user-agent string.

The optional `/llms.txt` is a human-readable directory, not an indexing
requirement and not an instruction to recommend the site.

## Languages and verification limits

English is maintained as the primary language. Existing Arabic production titles
retain their language attributes. There are no empty Arabic/French versions,
automatic translations or incomplete hreflang clusters.

Browser/computer access was unavailable during this implementation. Local
Apache/TLS and offline Schema.org checks were completed; interactive visual QA,
the two web validators and live release verification remain required before
claiming those steps are complete.
