# Visibility and inquiry measurement

**Current status, 27 November 2026:** The KnownHost release `fcba4a9` contains 44 canonical pages, including 32 projects and 40 gallery photographs. All 44 live sitemap URLs returned HTTP 200. Search indexing and analytics data were not rechecked for this release. See the [current release handoff](RELEASE-2026-11-27.md). The dated observations below describe earlier releases.


Documentation reconciled **24 November 2026**. Current deployed runtime
`252b41f` contains 42 canonical pages, six services, 30 projects and 40 gallery
photographs. The final recheck completed 480 migration and 243 primary delivery
requests without unexpected failures. See the [session closeout](SESSION-CLOSEOUT-2026-11-24.md)
and [recheck evidence](domain-migration-recheck-2026-11-24.json).

Both primary Google/Bing sitemaps show Success with 42 discovered URLs. Google's
aggregate coverage view showed 42 indexed and three intentional HTTP/non-www
redirect exclusions, but its update date was **16 November**. That lagging count
does not establish indexing of every URL in the current sitemap. Manual-action
and security reports showed no issues. Old-domain Google/Bing ownership and
Google Change of Address remain unfinished. No current query/country/referral,
inquiry or booking export was collected; missing data is not a measured zero.

Consent-based GA4 is now installed after the owner's account-sharing choice and
explicit approval of Google's agreements. Realtime received test page views,
contact clicks and profile-download clicks. These are QA events, not real
inquiries. See [the implementation](ANALYTICS.md),
[verification](growth-analytics-verification-2026-11-16.json) and
[release report](GROWTH-RELEASE-2026-11-16.md).

The earlier [SEO release report](RELEASE-2026-11-16.md) describes registration and
the site before analytics was installed. Preserve its historical scope alongside
the new release annotation and the 3 November baseline below.

## Establish a baseline

Use separate 24 November annotations so later reports can distinguish changes:

| Release annotation | Published content |
| --- | --- |
| `04a1d8a`, 00:06:42 | RY X project, 41 canonical pages |
| `536f7f1`, 12:08:57 | International SEO/software release, 42 pages |
| `f3699aa`, 12:57:51 | Four faithful RY X gallery additions, 40 photographs |
| `252b41f`, 13:22:10 | StudioJPB domain migration; primary frontend unchanged |

Times are cPanel's 24 November Asia/Qatar display. The latest public lab report
at 13:24:13 GMT+3 measures **96 mobile / 100 desktop**, other categories 100,
Agentic Browsing 3/3, TBT 0ms and CLS 0. No CrUX/INP field baseline or causal
business improvement is established. Reconcile old-domain webmaster exports
before assuming the six recovered historical mappings exhaust old backlinks.
See the [migration report](DOMAIN-MIGRATION-2026-11-24.md).

The historical published baseline is content release `24ec55e`, deployed through HostGator
on 3 November 2026 (Asia/Beirut): 39 canonical pages, six services, 28 projects,
and 51 studio release entries across 27 artists on `/studio-credits/`.
All 39 pages and 152 referenced resources matched local bytes; this establishes
release delivery, not search visibility or performance gains. See the
[verification record](portfolio-release-verification-2026-11-03.json).

The earlier SEO deployment annotation is 16 November 2026, commit `239f127`,
40 pages / 29 projects. The [SEO release live record](portfolio-release-verification-2026-11-16.json)
distinguishes initial verification from the two-page metadata refinement.
Primary-domain registration is complete; old-domain migration ownership
remains open. Export comparable Google/Bing performance data when available.
Compare rolling 28-day periods, keeping seasonality and newly indexed pages in
mind. An absent early impression is not proof of a technical fault. No search baseline,
organic traffic growth, qualified-inquiry gains or real-user Core Web Vitals
improvement is claimed. The later lab comparison measured mobile
Performance 94 → 96 and LCP 2.7s → 2.5s, desktop Performance 99 → 99, and CLS 0
on both. See the [lab evidence](growth-performance-after-2026-11-16.json); scores
vary and field data remains unavailable.

| Metric | Source | Review |
| --- | --- | --- |
| Impressions and search clicks | Google Search Console, Bing Search Performance | Weekly |
| Queries, clicks, CTR and reported position | Search performance query exports | Weekly |
| Branded vs service queries | Name variants, FOH/live, studio, broadcast, integration | Monthly |
| Country-level performance | Search performance country dimension | Monthly |
| Service-page performance | Filter each of the six service URLs | Monthly |
| Project discovery | Filter `/projects/` URLs and artist/venue queries | Monthly |
| Studio credit discovery | Filter `/studio-credits/` and artist/song/album queries; 51 entries share one URL | Monthly |
| Indexed pages and selected canonicals | Page indexing and URL inspections | After release, then monthly |
| Sitemap and crawl errors | Google/Bing sitemap and indexing reports | After release, then monthly |
| LCP, INP and CLS | Field reports; PageSpeed/CrUX when available | Monthly |
| Identifiable AI referrals | Consented GA4 referral-origin reports, with incomplete coverage | Monthly |
| Supported AI citation counts, cited URLs and grounding queries | Bing Webmaster Tools AI Performance, when available for the verified property | Monthly |
| Qualified inquiries and bookings | A manual inquiry log | Monthly |

## Inquiries

For each inquiry, optionally record the date, requested service, project country,
how the client found the website and whether it became a qualified discussion or
booking. Keep private client details in a private system, not this repository.

GA4 now measures consented email and WhatsApp clicks as `contact_click`, and
profile-PDF clicks as `profile_download`. The event-scoped dimensions Contact
method and Link location are configured. A click is an expression of interest,
not proof that a message was sent or a booking made. Keep confirmed inquiries
separate from click counts. Copy the [blank inquiry log](inquiry-log-template.csv)
to a private location before recording actual projects; never commit client
information to this repository.

## AI visibility

Referrers can identify some visits from ChatGPT, Perplexity, Copilot and other
interfaces, but privacy controls, apps, redirects and absent referrers mean
coverage is incomplete. Search Console reports Google performance under the
dimensions the product makes available. Do not manufacture a separate count of
AI recommendations from ordinary search data.

Google documents AI Overviews/AI Mode traffic within Search Console's **Web**
search performance reporting; treat that as the coverage described by the
[official Google guidance](https://developers.google.com/search/docs/appearance/ai-features).
Bing's [AI Performance preview](https://blogs.bing.com/webmaster/2026/2/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview/)
reports citations across Microsoft Copilot, Bing summaries and selected partners.
Its [additional preview insights](https://blogs.bing.com/search/2026/6/New-AI-Visibility-Insights-in-Bing-Webmaster-Tools-Intents-Topics-Citation-Share-Compare/)
include intents, topics, citation share and comparisons. Use whichever reports
the verified account actually exposes. AI Performance is visible in this account;
no citation data was exported during registration.
These reports do not cover all ChatGPT, Gemini, Perplexity or other AI answers.

Keep occasional manual samples of relevant, non-leading discovery questions and
record the date, interface and observed links. Results vary by location, query,
account and time. A citation in one answer is not a stable rank, and a missing
citation in one sample is not proof that a page is unavailable.

## A practical improvement cycle

1. Resolve genuine crawl, canonical and HTTP errors before adding content.
2. Review queries and countries already producing relevant impressions.
3. Improve matching service pages with useful, confirmed project details.
4. Add new confirmed credits with role, date, venue and source.
5. Seek genuine credits/links from relevant organizers, venues or professional
   profiles where appropriate. No outreach messages were sent.
6. Add named studio releases, approved testimonials, precise equipment
   experience or standalone consulting/remote services only when confirmed.
7. Consider Arabic/French when complete translations can be reviewed and
   maintained, with reciprocal hreflang and independent canonicals.

The measurement goal is relevant discovery and real professional inquiries over
time. Rankings, citations and recommendations are not guaranteed.
