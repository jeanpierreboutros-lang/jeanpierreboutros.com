# StudioJPB domain consolidation — 24 November 2026

Final read-only recheck completed at **13:37:12 Asia/Qatar** on 24 November:
723 live HTTP requests, zero unexpected failures, 76 direct authoritative-DNS
queries with no record changes, and four valid HTTPS hostnames. Both hosting
and cPanel Email Basic expire **1 December 2026**, with auto-renew **off**.
See the [recheck evidence](domain-migration-recheck-2026-11-24.json) and
[final session closeout](SESSION-CLOSEOUT-2026-11-24.md).

Published and live-verified. cPanel deployed content commit
`252b41f3414f03f202db2e5b55626369730d8002` at **24 November 2026, 1:22:10 PM**;
the displayed Last Deployed SHA matched. All 480 migration checks passed.
Google Change of Address submission and old-domain search ownership remain
manual follow-ups; they are not represented as completed.

Destination: **https://www.jeanpierreboutros.com**. The owner explicitly authorized
consolidation of the retired studiojpb.com website. Domain registration, DNS,
email, certificate services and the other websites on the account are retained.

## Infrastructure audit before changes

| Area | Observed configuration |
| --- | --- |
| Registrar | GoDaddy.com, LLC for both domains, from authoritative Verisign RDAP |
| Old-domain registration expiration | 30 June 2027 |
| Primary-domain registration expiration | 24 February 2027 |
| Authoritative DNS | ns8001.hostgator.com and ns8002.hostgator.com for both domains |
| Web addressing | Both apex A records are 192.185.16.224; www is a CNAME to its own apex; no AAAA answer observed |
| Hosting | HostGator Business Plan; cPanel shows both domains on the same /public_html document root |
| Server / CDN | Apache response headers, gzip; no separate CDN or proxy identified from public DNS/headers. No CDN settings are changed |
| HTTPS | Certificate chain and hostname validation pass for all four hostnames; Let's Encrypt YR2, expiry 29 January 2027 |
| Before: old website | All four HTTP/HTTPS apex/www homepage variants return 200 duplicate portfolio HTML |
| Before: primary website | HTTPS www is direct 200; its other three homepage variants use one 301 to it |
| Before: old legacy pages | Six archived iWeb HTML pages now return 404 |
| Active references | All 42 pages already use primary-domain canonicals, structured-data URLs and sharing URLs; no old-domain reference in their HTML |
| Search ownership | The inspected Google account has the new domain property only; old-domain ownership and Change of Address have not been completed |

Both domains have valid TLS already, so no certificate replacement or insecure
bypass is needed. cPanel's built-in Force HTTPS switch on the old primary hosting
domain is off. The reviewed server rules send old HTTP directly to the new HTTPS
destination, avoiding an intermediate old-domain HTTPS redirect.

Mail preservation is critical: the old domain's MX points to studiojpb.com itself,
and its SPF includes `a mx include:websitewelcome.com`. Changing its apex A record
for a redirect service could therefore affect mail. This implementation changes
only web-server rewrite rules. It does not change nameservers, A/CNAME, MX, TXT,
SPF, the observed default DKIM selector, mail routing, mailboxes or forwarders.
DMARC TXT records were not present in the queried DNS before this work; no new
DMARC policy is introduced as part of a website migration.

Evidence: `domain-migration-dns-before.json`, `domain-migration-tls-before.json`,
`domain-migration-registration-before.json`, `domain-migration-http-before.json`.

## URL discovery and mappings

The Internet Archive CDX response contains 34 distinct archived resources,
including six legacy content pages and two hosting login entry points. The six
content snapshots were retrieved and reviewed, including meaningful image alt
text from the old iWeb site. Archive presence is evidence of former URLs and
content, not proof that those pages are currently indexed or have backlinks.
Search queries did not yield a complete current old-domain index. No backlink
count, domain-authority score or complete historical index inventory is claimed.

| Old path on either old host | New destination | Basis |
| --- | --- | --- |
| / | / | Same professional identity; new homepage retains StudioJPB context |
| /studiojpb.com/Home.html | / | Former studio homepage |
| /studiojpb.com/About_Us.html | /projects/studio-jpb/ | Dedicated current studio practice description |
| /studiojpb.com/Clients.html | /studio-credits/ | Current named studio credits; archived Clients page had placeholders |
| /studiojpb.com/Services.html | /services/ | Current service directory, including recording, mixing and mastering |
| /studiojpb.com/Gallery.html | /#gallery | Current gallery |
| /studiojpb.com/Contact_Us.html | /#contact | Current professional contact section |
| All 42 current canonical paths | Identical path on primary origin | Existing shared-root content, verified by body hashes |
| Current asset/discovery URLs | Identical path on primary origin | Keep image/PDF links and sitemap discovery working |
| Unmatched or retired resources | Same path on primary origin, ending in a real 404 | No invented relevance or homepage fallback |

The exact six-page map and rationale are maintained in
`hosting/domain-migration.json`. Query strings are preserved, including repeated
parameters and encoded characters. For gallery/contact redirects the query is
placed **before** the fragment. Old index.html and missing-slash requests go
directly to the final canonical path. Encoded unknown paths retain their escaped
bytes. Incoming fragments are browser-side and never reach the server; existing
homepage anchors remain available on the destination.

Old robots.txt stays a direct 200 with the current primary sitemap reference
and existing AI search/training policy. The following operational paths are also
excluded from website migration: ACME/PKI certificate validation, cPanel/webmail/
WHM/webdisk entry points, autodiscover/autoconfig, and Google/Bing ownership proof
files. These exceptions preserve operational services and do not serve duplicate
portfolio content. Mail subdomains and every other hosted domain are outside
the hostname scope. Existing access-control rules still execute for exceptions.

Legacy artwork, CSS/JS, construction.png and the obsolete gallery RSS feed have
no verified matching replacement. They are not redirected to unrelated new
photographs or the homepage. Unknown destinations retain genuine missing-page
responses. Additional verified historic URLs discovered in webmaster exports or
logs should be added individually to this map.

## Implementation and pre-deployment validation

Only `hosting/seo.htaccess` changes runtime behavior. The existing installer
atomically replaces the marked managed block, privately backs up the previous
.htaccess, preserves all other rules, and rejects symlinks or malformed markers.
The existing cPanel deployment workflow installs the fragment; no separate
registrar forwarding or cPanel wildcard redirect should be added on top of it.

- Production generation and all 42-page SEO checks pass, including 5,239 official
  Schema.org vocabulary checks. No canonical/sitemap/content rewrite is needed.
- 320 real Apache fixture checks pass for page mappings, one-step normalization,
  queries, escaped paths, case/port variants, operational exceptions, existing
  denied-file restrictions and isolation from other hosts.
- Installer reruns preserve the remainder and are idempotent. Apache syntax and
  Python/JavaScript checks pass; consent/analytics tests pass.
- 420 existing content/asset files, plus robots.txt, sitemap.xml and llms.txt,
  are byte-identical. This includes the design, images, fonts, animations and
  gallery implementation. No frontend payload or dependency is added.

Evidence: `domain-migration-apache-validation.json`; repeatable checks are in
`check_domain_migration_apache.py` and `audit_domain_migration.py`.

Rollback triggers are any redirect loop, unexpected chain, failed canonical
page/resource, incorrect mapped destination, changed mail/DNS record or broken
hosting/mail entry point. Before the release, privately retain the prior managed
fragment and .htaccess. Revert only this release's fragment and redeploy, preserving
unrelated rules. Do not change DNS or delete domains as a rollback action.

## Google Search Console: exact remaining procedure

The requested Change of Address preparation is complete; submission is a manual
follow-up. The old domain is not verified in the inspected account. The current
[Google Change of Address instructions](https://support.google.com/webmasters/answer/9370220)
require ownership of both source and destination and working redirects first.

1. In the same Google account, open Search Console → property selector → Add
   property → Domain → `studiojpb.com`. Copy Google's actual verification TXT.
2. HostGator portal → Hosting → cPanel → Zone Editor → Manage `studiojpb.com` →
   Add Record → TXT. Use the apex name `studiojpb.com.` and the exact supplied
   value. Add a separate TXT record; retain the existing SPF and all mail/DNS
   records. Save, then Verify in Google. Do not add this at GoDaddy while the
   authoritative nameservers remain HostGator's.
3. Add/verify URL-prefix properties for `https://studiojpb.com/`,
   `https://www.studiojpb.com/` and `https://www.jeanpierreboutros.com/` as needed;
   verified Domain ownership can verify the corresponding prefixes.
4. Export the old property's Performance → Pages, Page indexing, Links → Top
   linked pages and Sitemaps. Review historic landing pages and access-log 404s;
   add any additional relevant mappings before declaring the inventory exhaustive.
5. After the live checks in this report pass, open each old hostname's property →
   Settings → Change of Address → choose `https://www.jeanpierreboutros.com/`.
   Run the tool's checks and submit. Follow the current interface for both www
   and apex; do not assume an apex-only request covers www. The tool covers the
   protocols of its source; this is a domain move, not a separate HTTP→HTTPS move.
6. Confirm the migration notice and monitor both properties. The primary
   sitemap remains `https://www.jeanpierreboutros.com/sitemap.xml` with 42 URLs.
   Retain verification records and source properties.

Keep redirects, old-domain registration, DNS and HTTPS for at least a year,
preferably indefinitely for visitors and backlinks, following Google's
[site-move guidance](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes).
Google's Change of Address notice runs for 180 days; it is not a reason to turn
off working redirects or mail after that period. No indexing, ranking or full
authority-transfer guarantee is made.

## Bing and AI discoverability

The inspected Bing account contains only the verified primary website. Its
HTTPS sitemap is Success with 42 URLs. No Site Move control appeared in the
inspected Configuration or Tools & Enhancements menus.

Bing's current [webmaster guidelines](https://www.bing.com/webmasters/help/bing-webmaster-guidelines-30fba23a)
call for 301s for permanent moves, crawlable relevant destinations and consistent
canonical URLs. These are the migration mechanisms implemented here. Do not rely
on an old tutorial implying that a particular Site Move menu is mandatory.

1. Retain the existing verified primary Bing property and its successful sitemap.
2. Add and verify both old website hosts in Bing Webmaster Tools, or import
   verified Google properties after the Google ownership step above. Preserve
   existing DNS verification and email records.
3. Export old Site Explorer/Links/Performance URLs and reconcile the mapping.
4. Use URL Inspection → Live URL on an old homepage and a legacy page. Bing's
   [live tool](https://www.bing.com/webmasters/help/url-inspection-55a30305)
   reports the redirect; use Inspect redirect destination to check the target.
5. Notify changed old URLs via the verified old property's URL submission
   facility if available. Bing documents support for submitting redirect URLs
   in its [URL-submission guidance](https://www.bing.com/webmasters/help/url-submission-62f2860b).
   The existing new-domain IndexNow helper intentionally does not claim authority
   to submit old-host URLs. Do not reuse a cross-host redirected key as proof.

Search and AI user agents receive the same server redirects as visitors. Existing
Googlebot, Bingbot, OAI-SearchBot, Claude/Perplexity search and user-fetch access
remains; GPTBot's separate training exclusion remains. User-agent header probes
can test HTTP delivery but do not prove access from a provider's real IP ranges
or an AI citation. Google's [AI-search guidance](https://developers.google.com/search/docs/appearance/ai-features)
uses the ordinary SEO foundation; no hidden content or artificial AI schema is
added. Update owned social/profile website links to the primary domain and
request updates from important referring sites when independently authorized;
no outreach messages are sent in this work.

## Hosting / registrar / CDN maintenance instructions

The server-rule deployment can be completed in the already accessible HostGator
account; no registrar or CDN reconfiguration is required. For future maintenance:

1. HostGator → Hosting → cPanel → Git Version Control → Manage the existing
   `jeanpierreboutros.com` repository → Pull or Deploy → Update from Remote.
   Confirm the reviewed SHA, then Deploy HEAD Commit and confirm Last Deployed SHA.
2. Keep both domains assigned to the existing shared document root. Do not use
   registrar forwarding, masked forwarding, a new apex CNAME or an extra HTTPS
   redirect before the migration rules. Any future CDN needs equivalent one-hop
   rules and certificate coverage before its traffic switch.
3. cPanel → SSL/TLS Certificates → inspect coverage for all four hostnames and
   retain automatic renewal. Keep the ACME/PKI paths accessible. A private key
   must not be copied into this repository or report.
4. GoDaddy → My Products → Domains → Domain settings: retain ownership and renew
   both domains before their RDAP expiration dates. Keep the existing HostGator
   nameservers. No purchase, billing or registration setting is changed here.
5. HostGator → Billing → Renewal Center shows **Business Plan** and
   **cPanel Email Basic** both expiring **1 December 2026**, with auto-renew
   **off** for each. Renew both through the owner-controlled billing flow.
   No renewal, payment or billing setting was changed. Domain registration
   expiration does not cover these hosting/email subscriptions.

## Production results

The deployed rules are verified against live domains, using normal TLS
certificate checks and actual GET/HEAD response headers.

| Live homepage HEAD request | First response | Location |
| --- | --- | --- |
| http://studiojpb.com/ | 301 | https://www.jeanpierreboutros.com/ |
| https://studiojpb.com/ | 301 | https://www.jeanpierreboutros.com/ |
| http://www.studiojpb.com/ | 301 | https://www.jeanpierreboutros.com/ |
| https://www.studiojpb.com/ | 301 | https://www.jeanpierreboutros.com/ |
| http://jeanpierreboutros.com/ | 301 | https://www.jeanpierreboutros.com/ |
| https://jeanpierreboutros.com/ | 301 | https://www.jeanpierreboutros.com/ |
| http://www.jeanpierreboutros.com/ | 301 | https://www.jeanpierreboutros.com/ |
| https://www.jeanpierreboutros.com/ | 200 | None |

The seven noncanonical origins reach the primary homepage in one hop. Across
all 42 canonical paths and eight origins, the 336 page-matrix requests finish
with direct primary-domain 200 content matching the local release. No loop or
extra redirect hop was observed on migrated content.

| Additional live migration checks | Result |
| --- | --- |
| Six legacy pages × four old origins, with queries | 24/24 correct single 301s to relevant destinations |
| Six legacy pages × four old origins, without queries | 24/24 correct clean destinations |
| index.html and directory normalization | 12/12 direct final-path redirects |
| Unmatched/retired URLs and encoded paths | 16/16 retain their paths and finish as genuine 404s |
| Old robots.txt | 4/4 direct 200, exact current policy bytes |
| cPanel/webmail entry points | 8/8 remain available on old origin |
| Missing ACME/PKI probe paths | 8/8 remain on old origin with genuine 404s; no migration redirect |
| sitemap.xml and llms.txt | 8/8 one 301, exact current primary file bytes |
| Ten search/AI user agents × four old origins | 40/40 receive one 301 to the accessible matching page |
| **Migration total** | **480/480 pass; zero active metadata errors** |
| Separate primary delivery audit | 243 requests; 207 page/resource/discovery body hashes match; its one intentional missing-page 404 is expected |
| DNS before/after | 38 repeated queries; zero record-value changes, ignoring resolver TTL countdown |
| TLS after deployment | 4/4 hostname/chain validations pass; certificates retained |
| Production browser/accessibility | Six axe scans, zero violations; mobile/desktop gallery controls, keyboard/focus and no-JavaScript access pass |

The primary audit retains live response headers for compression and versioned
immutable caching. Its 42 canonical pages, 162 referenced resources and three
discovery files match the reviewed release. No DNS, mail, certificate, domain
assignment, primary content or frontend asset change was made. No rollback
trigger occurred. SMTP/IMAP message delivery was not tested with a real message
or mailbox authentication; unchanged web-only configuration and DNS are the
preservation evidence.

Fresh [public PageSpeed report, 1:24:13 PM GMT+3](https://pagespeed.web.dev/analysis/https-www-jeanpierreboutros-com/ilzvfpdb8abcu44yyzhdxp):

| Metric | Immediately preceding public report | Post-migration |
| --- | ---: | ---: |
| Mobile performance | 96 | 96 |
| Desktop performance | 99 | 100 |
| Accessibility / Best Practices / SEO | 100 / 100 / 100 | 100 / 100 / 100 |
| Agentic Browsing | 3/3 | 3/3 |
| TBT / CLS, both devices | 0 ms / 0 | 0 ms / 0 |

The owner-supplied original baseline was 95 mobile / 100 desktop. The fresh
post-migration report meets or exceeds those scores. Mobile LCP is 2.477s and
desktop LCP is 0.562s. This is one lab report with no CrUX field data; the primary
payload is unchanged, and timing variance does not prove that the redirect
rules caused a performance improvement.

Evidence files:

- `domain-migration-head-after.json`: actual first-response HEAD headers for all
  eight HTTP/HTTPS origin combinations.
- `domain-migration-http-after-validation.json`: every one of the 480 requests,
  actual header chains, final URL/status, body hashes and pass/fail details.
- `domain-migration-primary-assets-after.json`: separate full active-site delivery
  and cache/compression/crawler evidence.
- `domain-migration-dns-after.json`, `domain-migration-tls-after.json`:
  unchanged DNS records and validated HTTPS endpoints.
- `domain-migration-browser-qa-after.json`, `domain-migration-pagespeed-after.json`:
  observed production accessibility/behavior and public performance results.
- `domain-migration-preservation.json`, `domain-migration-publication.json`:
  source comparison and observed deployment/search-platform status.

The source follow-up commits containing these reports do not need another
website deployment: documentation and audit tools are excluded by the existing
production copy manifest.

## Final read-only recheck

The later recheck repeats all 480 migration requests and the 243-request primary
audit with no unexpected failures. It queries both authoritative DNS servers
directly (76 queries), confirms unchanged records and validates four HTTPS hosts.
Google/Bing still show sitemap Success with 42 discovered URLs. Google manual
actions/security reports show no issues; its aggregate coverage data remains
dated 16 November and the three exclusions are intentional homepage redirects.
Old-domain ownership remains absent in both connected accounts. The latest
performance evidence is the existing 13:24:13 report, not a new performance run.
No message-delivery test, payment, renewal or migration filing was performed.
See [the complete recheck](domain-migration-recheck-2026-11-24.json).

## Remaining owner actions and monitoring

1. Complete old-domain Google ownership and the prepared Change of Address
   procedure for apex and www. No request has been submitted in this work.
2. Verify/import the old domains in Bing, reconcile historical landing/backlink
   exports, and notify its changed old URLs using the supported verified-site
   tools. No Bing migration submission is claimed.
3. Review old-domain access-log 404s and search exports for additional legacy
   URLs over the next several weeks. Extend the explicit map when an equivalent
   destination is verified. Historical backlink coverage is not exhaustive.
4. Renew **both** Business Plan hosting and cPanel Email Basic before
   **1 December 2026**; auto-renew is off for both. Retain old-domain registration,
   DNS, certificate renewal and working redirects.
5. Monitor old/new indexing, clicks and impressions, referring traffic, selected
   canonicals, crawl errors and Bing AI Performance. Keep a dated baseline and
   compare after recrawling; consolidation is a search-engine process, not an
   immediate measurable transfer of every signal.

The technical migration is complete and verified. Search-platform filing,
ongoing monitoring and the limits above remain explicit; complete authority
transfer or AI citation gains are not claimed.
