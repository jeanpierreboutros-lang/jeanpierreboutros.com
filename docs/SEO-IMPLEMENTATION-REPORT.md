# Worldwide SEO and AI search implementation

Documentation reconciled: 3 November 2026. Website: https://www.jeanpierreboutros.com/.

## Published release

HostGator deployed content release `24ec55eef9540cb49fab5f49328399e631a13c05`
on 3 November 2026 at 00:00:01 (Asia/Beirut). cPanel's Last Deployed SHA matched.
All 39 canonical pages and 152 referenced resources matched the approved local
bytes. Six canonical redirect cases, an unknown-path 404 and the two tested
research/source paths passed live verification. The published homepage was
observed in Chrome. See the [verification record](portfolio-release-verification-2026-11-03.json).

| Current inventory | Count |
| --- | ---: |
| Canonical HTML pages / sitemap URLs | 39 |
| Homepage | 1 |
| Service pages | 6 |
| Project pages | 28 |
| Directories: services, projects, studio credits, international projects | 4 |
| Artist and ensemble collaboration names | 41 |
| Gallery photographs | 34 |
| Unique studio song/album entries | 51 |
| Credited studio artists / directory groups | 27 / 27 |
| Profile PDF | One A4 page, 16 project links |

The homepage filters show Featured 6, All work 28, FOH 16, Monitors 6,
Broadcast 1, Studio 3 and Technical 2. Albums count as one studio entry; track
lists do not inflate the total. The shared Sing A Little entry is displayed once
while its evidence is recorded under both artists. Studio entries share the
`/studio-credits/` URL rather than creating 51 individual pages.

| Release | Deployment and evidence scope |
| --- | --- |
| `6cf3dda` — original SEO release | 2 November 2026; 28 pages and 93 referenced assets matched live bytes; canonical redirects, real 404 and a project dialog checked |
| `24ec55e` — portfolio expansion | 3 November 2026; 39 pages and 152 referenced resources matched live bytes; six redirect cases and three expected 404 responses checked |

Documentation commits may follow the deployed content commit without requiring a
new website deployment. Repository documentation and source generators are
excluded from the HostGator runtime manifest.

## Architecture and search access

The Python 3.9+ standard-library generator produces static HTML, CSS and vanilla
JavaScript. No frontend framework, database or rendering service is required.
`build.py` holds portfolio content, `studio_credits.py` holds release credits,
`services.py` holds service descriptions, and `search_pages.py` generates shared
metadata, structured data and discovery files. Editing and deployment instructions
are in the [README](../README.md).

| Area | Original finding | Current implementation |
| --- | --- | --- |
| Routing and discovery | One canonical homepage; substantial project descriptions shared hash/modal URLs | 28 complete project pages, six service pages and four directories available without JavaScript |
| Canonicals | HTTPS www canonical tag; four origin variants returned 200 | Retained HTTPS www identity; hostname-scoped 301 rules for duplicate origins, explicit index files and missing directory slashes |
| Metadata | Homepage metadata only | Unique title, description, H1, canonical and social metadata on 39 pages |
| Structured data | Unlinked Person object | Linked Person, site, organizations, services, catalog, pages, breadcrumbs, project articles, images and studio ItemList |
| Sitemap | Homepage only | 39 canonical indexable HTML URLs; release entries are not separate sitemap pages |
| Robots | Wildcard allow | Explicit access for four search crawlers; GPTBot disallowed at the owner's request |
| Fonts | External stylesheet and font requests | Original typefaces self-hosted, licensed and subset-aware, with three Latin preloads |
| Images | Responsive WebP, dimensions and lazy loading already present | Preserved and expanded with attributed event images and matching derivatives |
| Internal linking | Homepage sections and project hashes | Project/service directories, breadcrumbs, related links, release links and 16 PDF project links |
| Accessibility | Skip links, focus styles, native dialogs, reduced-motion controls | Preserved; semantic pages, valid ARIA references, native FAQs and artist disclosures |
| Measurement | No configured analytics or ownership tokens found | Registration instructions and measurement plan; no tracking or fabricated verification installed |

The historical [pre-release audit](audit-before.json) found no login requirement
or accidental `noindex`. Requests identifying as Googlebot, bingbot,
OAI-SearchBot and PerplexityBot received HTTP 200 from the test machine. Those
requests do not establish how the hosting firewall treats genuine crawler IPs.

The homepage retains its design, modals, gallery, animation controls, section
anchors and navigation. Real links progressively open project dialogs when
JavaScript is available and remain ordinary page links otherwise. Closing a
project returns focus to its originating link. The opening collaboration strip
remains removed and StudioJPB retains the Manley equipment photograph.

## Identity, services and directories

Jean-Pierre Boutros remains the professional name, with Jean Pierre Boutros as a
structured-data alternate. The site identifies a Lebanon home base and worldwide
availability by arrangement. StudioJPB's Jounieh location and 2008 founding and
Zynforge Audio's relationship remain intact. No foreign office, award, equipment
ownership or testimonial has been invented.

The international directory describes documented work in France, Oman, Qatar,
Kuwait, Saudi Arabia, the UAE, Turkey, Jordan and Lebanon. Availability elsewhere
does not imply a past project or permanent business there.

| Canonical path | Scope |
| --- | --- |
| `/live-sound-engineer/` | FOH, concerts, festivals and artist monitor assignments |
| `/orchestra-sound-engineer/` | Orchestral, vocal and opera FOH |
| `/recording-engineer/` | Recording/tracking and StudioJPB practice |
| `/mixing-mastering/` | Mixing and mastering stages, with confirmed album experience |
| `/broadcast-audio-engineer/` | Papal Mass broadcast and qualified television collaborations |
| `/studio-system-integration/` | Merwas Studios and Playsound Studios integration |
| `/services/` | Six services and factual professional FAQs |
| `/projects/` | All 28 project records |
| `/studio-credits/` | 51 linked song/album entries across 27 credited artists |
| `/international-projects/` | Documented locations and international inquiry guidance |

Service pages include an introduction, scope, inquiry guidance, project examples,
four FAQs, related services and contact links. FOH/concert/festival intent shares
one substantial page. Standalone consulting, optimization or remote-mixing pages
await confirmation of those offerings. English remains maintained; existing Arabic
production titles retain language attributes. No incomplete translated versions,
hreflang clusters or country doorway pages were created.

## Project and studio credit coverage

All 28 project paths are listed below. The [README project register](../README.md#current-project-register)
records dates, venues and Jean-Pierre's exact roles.

```text
/projects/the-eighties/
/projects/marina-viotti/
/projects/cartoon-orchestra/
/projects/al-sharq-symphony/
/projects/abeer-nehme-qatar/
/projects/baligh-hamdi-night/
/projects/warda-night/
/projects/night-of-arab-stars/
/projects/lebanese-philharmonic-diman/
/projects/nancy-ajram-olympia/
/projects/marcel-khalife-muscat/
/projects/ehdeniyat-abeer-nehme/
/projects/ehdeniyat-al-shami/
/projects/nancy-ajram-expo-dubai/
/projects/ehdeniyat-adam/
/projects/papal-broadcast/
/projects/studio-jpb/
/projects/studio-integration/
/projects/marcel-khalife-amman/
/projects/abeer-nehme-baalbeck/
/projects/beiteddine-marco-polo/
/projects/carole-samaha-golden-album/
/projects/zade-dirani-dbayeh/
/projects/zade-dirani-amman/
/projects/marcel-khalife-baalbeck/
/projects/nancy-ajram-jounieh/
/projects/mazeej-ndu/
/projects/beirut-the-sea-lover/
```

The expansion includes Marcel Khalifé at Amman Citadel for monitors/recording;
Abeer Nehme at Baalbeck for FOH; Marco Polo at Beiteddine for audio technical
supervision; Carole Samaha's Golden Album for mixing/mastering; two Zade Dirani
FOH shows; Marcel at Baalbeck and Nancy at Jounieh for FOH; Mazeej at NDU for FOH;
and Beirut the Sea Lover for 3D sound mixing. Mazeej uses the owner's corrected
11 March 2019 date. Rasha Rizk's اللعبة (The Play) is a studio album recording
entry, not an additional project page.

Public wording retains artist/project identification and Jean-Pierre's own
engineering credit. Studio-only credits remain StudioJPB credits. Other
contributors' production credits, research notes and private track lists are
excluded from rendered copy; photo attribution remains visible. Owner
confirmations establish supplied roles. Public event coverage establishes
context unless it explicitly credits his work, as the Beirut festival archive
does. Nancy's monitor assignments apply specifically to her performances.

All 41 collaboration names were audited. The [studio research](studio-credit-research.json)
reconciles the 51 unique entries and thirteen directly confirmed role entries.
The [Nancy review](nancy-credit-research-2026-11-02.json) records four
mixing/mastering songs and Warana Eh recording. The [broader review](broad-credit-research-2026-11-02.json)
records the six selected additions: Akher Esdar, Tayer, Idi bi Idik, Moving
Mountains, Addaysh Bhebak and Beirut the Sea Lover. Maher Zain and Between the two
Blacks are excluded at the owner's request. Unselected leads remain research-only;
the 2025 Shou Baamel lead does not expand the existing 2022 album role.

The downloadable profile was updated with selected confirmed roles. Its current
one-page A4 artifact has 16 project links, is 317,690 bytes, and uses fingerprint
`02735665a277`. It is a selection rather than an exhaustive discography.

## Search intent and structured data

The qualitative intent mappings are international sound engineer to the homepage
and international directory; FOH/concert/festival/monitor work to live sound;
orchestral/opera work to orchestra sound; recording and mixing/mastering to their
respective service pages; broadcast and integration to their service pages; and
artist/song/album engineering queries to studio credits. Actual project queries
also have dedicated project destinations. These mappings are not measured keyword
volumes or ranking forecasts. The original review of public portfolios
[Berk Kula](https://berkkula.com/) and [Jacob Feinberg](https://jjmfp.com/)
informed clear service and role presentation; no competitor metrics were assumed.

The canonical identity is `https://www.jeanpierreboutros.com/#person`. Linked graphs
include Person, WebSite, WebPage, ProfilePage, CollectionPage, Organization,
Service, OfferCatalog/Offer, BreadcrumbList/ListItem, Article, ImageObject and the
studio ItemList. Schema describes visible content and adds no fake reviews,
ratings, unsupported addresses, event attendance or FAQ rich-result claims.

The current local check passed **4,828 property/domain/range checks** against the
official Schema.org vocabulary. This does not replace the public Schema.org
Validator or Google Rich Results Test, which remain outstanding, and does not
promise a rich result.

`robots.txt` permits Googlebot, bingbot, OAI-SearchBot and PerplexityBot and blocks
GPTBot following the owner's preference. Other access retains the prior wildcard
policy. Firewall protections were not disabled. The optional `/llms.txt` is a
factual public directory; it is supplementary rather than an indexing requirement
or instruction to recommend the website.

Original implementation references:
[Google AI features](https://developers.google.com/search/docs/appearance/ai-features),
[Google AI guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide),
[OpenAI crawler controls](https://developers.openai.com/api/docs/bots),
[Perplexity crawlers](https://docs.perplexity.ai/docs/resources/perplexity-crawlers),
[Bing guidelines](https://www.bing.com/webmasters/help/bing-webmaster-guidelines-30fba23a).

## Verification and its limits

| Current portfolio release check | Recorded result |
| --- | --- |
| Production build and `check_site.py` | Passed for all 39 pages, inventory, metadata, local links/fragments, ARIA targets, schema and crawler policy |
| Official Schema.org vocabulary | 4,828 local property/domain/range checks passed |
| JavaScript syntax / diff whitespace | `node --check main.js` and `git diff --check` passed |
| Live content delivery | 39 pages + 152 referenced resources = 191 exact byte matches; no failures |
| Live canonical redirects | Six cases passed |
| Unknown path and tested source/research paths | Three expected HTTP 404 responses |
| cPanel deployed SHA | Matched `24ec55eef9540cb49fab5f49328399e631a13c05` |
| PDF | One A4 page with 16 project links; rendered/inspected before release; delivered bytes matched |
| Browser observation | Published homepage loaded with 28 projects, 34 photographs, new artists and studio directory |

The byte check establishes delivery of the referenced resources, not successful
execution of every interaction or a check of every repository file. A full new
live desktop/mobile keyboard, filter, dialog and image-viewer matrix is not
recorded as complete. Earlier local page views and the original release's live
project-dialog check do not replace that matrix.

| Historical original SEO evidence — 2 November 2026 | Original scope retained |
| --- | --- |
| Local HTML5/CSS parsing | 28 HTML documents and site/font CSS passed with zero parser errors |
| Local Schema.org vocabulary | 3,316 checks for the original release |
| Python compilation / shell syntax | Passed for the original implementation |
| Apache 2.4.67 TLS fixture | 28 pages HTTP 200; eight redirect cases passed |
| Shared hostname / access restrictions | Unrelated hostname unaffected; protected fixture remained HTTP 403 |
| Font / missing-path delivery | Correct font MIME and immutable cache; actual unknown-path 404 |
| Redirect installer | Existing rules preserved; private backup, idempotence and malformed-block rejection passed |
| External link audit | 30 targets: 25 HTTP 200, three 403, one transport error and one Facebook 400; no confirmed 404/410 |
| PageSpeed attempts | Mobile and desktop API requests returned HTTP 429; no scores obtained |

The [Apache fixture](apache-checks.json), [external link results](external-links.json)
and [PageSpeed attempts](pagespeed-attempt.json) remain historical evidence.
The 30-target audit is not an audit of every current release link. Blocked or
denied responses were not automatically treated as broken links. Local shared-host
fixture results do not establish the current remote configuration.

Self-hosted fonts, responsive images, dimensions, lazy loading, deferred JavaScript,
reduced motion and static content improve implementation quality, but **no measured
Core Web Vitals gain is claimed**. No new successful PageSpeed run or field dataset
is recorded. Google/Bing ownership verification, sitemap submission and both public
structured-data validators remain outstanding. No analytics, ownership token or
search-performance baseline was installed or invented.

## Maintenance and follow-up

Build sources, generated pages, fonts, images, PDF and hosting scripts are mapped
in the [README](../README.md#stack-and-structure). The non-purging HostGator manifest
copies 39 pages and runtime resources while preserving unrelated shared-host files.
The redirect installer preserves other rules and stores backups outside the public
root. Every managed redirect is scoped to the portfolio's two hostnames.
Deployment and rollback instructions are in the [deployment runbook](../README.md#deployment).

1. Complete the desktop/mobile interaction matrix when reviewing behavior changes.
2. Run the public Schema.org and Google validators on representative homepage,
   service, project and studio-directory URLs.
3. Complete Google Search Console and Bing ownership with real account-issued
   values, submit the sitemap and inspect representative URLs using the
   [search registration instructions](SEARCH-CONSOLE.md).
4. Establish search, country, page and qualified-inquiry baselines using the
   [measurement plan](MEASUREMENT.md). AI referrals provide partial evidence only.
5. Add future credits with confirmed role/version scope and source evidence;
   preserve the owner's exclusions and person-versus-studio distinction. Review
   the selected PDF and documentation inventory when portfolio content changes.

Search engines and AI services decide crawling, indexing and presentation.
Rankings, citations and recommendations are not guaranteed.
