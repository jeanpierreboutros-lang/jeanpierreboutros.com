# RY X gallery update — 24 November 2026

This is the gallery publication record. The final deployed runtime is
`252b41f`, with 42 pages, 40 gallery photographs and the verified StudioJPB
migration. Latest public PageSpeed is 96 mobile / 100 desktop at 13:24:13
GMT+3. See the [final session closeout](SESSION-CLOSEOUT-2026-11-24.md) for
current renewal deadlines, search-platform follow-ups and recheck results.
The measurements and release-specific statements below retain their dated scope.

Published and verified: content commit `f3699aa4cbe61f2a49fc2a98b239c1cee55839ac`.
cPanel displayed the matching Last Deployed SHA and completion time
24 November 2026, 12:57:51 PM. The earlier usage-limit interruption to browser
approval review was resolved after the owner requested continuation; no approval
check was bypassed.

Four owner-supplied RY X photographs are added to the existing gallery, increasing
it from 36 to 40 photographs. All four appear among the six initially visible
tiles. Existing project image indices 0–35 remain stable. The owner confirmed
the RY X context and explicitly chose faithful photo corrections.

| Supplied original | Published photograph | Size |
| --- | --- | --- |
| IMG_3654.HEIC | ry-x-foh-console-performance-2026.jpg | 2400 × 1800 |
| IMG_3642.HEIC | ry-x-foh-console-stage-2026.jpg | 2400 × 1800 |
| IMG_3648.HEIC | ry-x-production-blue-light-2026.jpg | 2317 × 2400 |
| IMG_3666.HEIC | ry-x-backstage-portrait-2026.jpg | 2384 × 2400 |

## Photo treatment and implementation

The original HEIC files remain unchanged in Downloads and are not published.
Oriented sRGB decodes receive modest shadow/exposure, color and white balance
corrections, chroma noise reduction, cropping, resizing and mild sharpening.
No generative editing, face retouching, object replacement or reconstruction is
used in the published images. Earlier generative previews were discarded.
Camera EXIF and GPS data are omitted from the published JPEG and WebP files.
The repeatable recipe and exact source/export hashes are recorded in
`enhance_gallery_photos.py` and `gallery-corrections-2026-11-24.json`.

Each photograph has responsive WebP derivatives at 160, 240, 480, 960 and
1600 pixels, intrinsic dimensions, descriptive alt text and visible captions.
The four 480px thumbnails total 71,638 bytes; all 20 derivatives total 883,064
bytes. Below-the-fold loading remains lazy. The full-size viewer includes all
40 images. Portrait thumbnail positioning keeps the faces visible; the viewer
shows the complete corrected export. Captions identify the confirmed event
without inventing other people's names, roles or client relationships.

`optimize_images.py --only` preserves every unselected original and derivative.
The build and validation inventory now expect 40 distinct photographs. All 42
canonical pages are regenerated because they share the gallery viewer data.
No new canonical URL, sitemap entry, crawler policy or structured-data claim
is introduced.

## Preservation and validation

- Existing photographs, derivatives, fonts, PDF, logos, CSS and JavaScript match
  their previous bytes. All previous image manifest entries remain identical.
- Homepage HTML before the gallery section matches the published baseline.
  Branding, animations, responsive layout and above-the-fold asset requests
  are unchanged. The homepage grows by 6,098 uncompressed HTML bytes.
- Production build, `check_site.py`, Python compilation, JavaScript syntax and
  analytics checks pass. The SEO validator covers all 42 canonical pages and
  the official Schema.org vocabulary.
- Six axe scans across 390px mobile and 1440px desktop views report zero
  violations. Gallery expansion/collapse, all four new full-size views,
  keyboard arrows/wrapping, Escape and focus return pass. No horizontal
  overflow or JavaScript errors occur. Without JavaScript all 40 photographs
  remain available. No new photograph is requested above the fold.

| Local Lighthouse 13.6.0 metric | Before | After |
| --- | ---: | ---: |
| Mobile performance | 99 | 98 |
| Desktop performance | 100 | 100 |
| Accessibility, both devices | 100 | 100 |
| Best Practices, both devices | 100 | 100 |
| SEO, both devices | 100 | 100 |
| Agentic browsing, both devices | 3/3 | 3/3 |
| Total blocking time, both devices | 0 ms | 0 ms |
| Cumulative layout shift, both devices | 0 | 0 |

These are controlled local lab runs, not public PageSpeed or real-user scores.
The mobile run changed from 99 to 98 (LCP 1.96s to 2.41s); an unchanged
above-the-fold payload and zero new initial image requests establish that
the new gallery files add no initial image download. Lab timing still varies,
and these measurements do not guarantee identical future scores. Previous
production PageSpeed measurements remain separately documented in the SEO
release report.

Evidence: `gallery-local-qa-2026-11-24.json`, mobile/desktop screenshots,
`gallery-performance-2026-11-24.json` and the four full Lighthouse JSON reports.

## Publication and rollback

The reviewed release was committed, pushed and deployed through the existing
cPanel Git workflow after all local checks passed. Live validation confirms:

- 243 public HTTP checks: all 42 canonical pages and 165 referenced/discovery
  resources match the reviewed local bytes. The only non-200 final response is
  the intentional missing-page 404 test; permanent canonical redirects pass.
- Separately, all four new JPEG exports, all 20 WebP derivatives and the image
  manifest match local bytes exactly (25 checks).
- Six production axe scans at 390px and 1440px have zero violations; all four
  new lightboxes, keyboard arrows/wrapping, Escape/focus return, show-all control
  and no-JavaScript access pass. No overflow or page JavaScript errors occur.
- The updated homepage was sent to IndexNow after its exact live HTML and
  ownership key were verified. The endpoint returned HTTP 200 for one URL.
  Acceptance does not establish indexing. Existing Google/Bing ownership and
  sitemap setup need no changes for this gallery addition.

A fresh [public PageSpeed report at 12:58:13 PM GMT+3](https://pagespeed.web.dev/analysis/https-www-jeanpierreboutros-com/u8h4n4cgfdj55919ihe3gz)
measures the published homepage:

| Production result | Before this gallery update, same-day reports | After |
| --- | ---: | ---: |
| Mobile performance | 95–96 | 96 |
| Desktop performance | 98–99 | 99 |
| Accessibility / Best Practices / SEO | 100 / 100 / 100 | 100 / 100 / 100 |
| Agentic browsing | 3/3 | 3/3 |
| TBT / CLS, both devices | 0 ms / 0 | 0 ms / 0 |

The supplied historical baseline was mobile 95 / desktop 100. Desktop 100 was
not reproduced in this production run; local desktop remains 100. Mobile LCP
is 2.477s and desktop LCP is 0.562s. This is one fresh lab report; there is no
CrUX field data and no claim of a causal ranking or Core Web Vitals improvement.
The new gallery photographs still generate zero initial image requests.

Evidence: `gallery-production-live-2026-11-24.json`,
`gallery-production-new-images-2026-11-24.json`,
`gallery-production-qa-2026-11-24.json`, production screenshots,
`gallery-pagespeed-production-2026-11-24.json`,
`gallery-preservation-2026-11-24.json` and
`gallery-publication-2026-11-24.json`.

A failed page/resource hash, missing image, broken viewer, accessibility
regression or changed layout is a rollback trigger. No trigger occurred.
The previous content release is `536f7f1`; the source baseline before this
addition is documentation commit `5e0b1dc`. A local backup of modified files
is retained under `Code/gallery-update-backups/before-2026-11-24`.
Documentation-only follow-ups do not require another website deployment.

## Expected benefit and remaining work

The gallery now supplies four more owner-confirmed examples of the working
side of the RY X production. Descriptive filenames, visible context, alt text
and ordinary image links help users and crawlers understand these photographs.
The existing professional credits and claims are unchanged. No ranking,
indexing, AI citation or inquiry increase is promised.

No manual gallery configuration remains. The original international SEO audit,
search-platform receipts, measurement limits and longer-term follow-ups remain
in [the SEO release report](SEO-RELEASE-2026-11-24.md) and
[original audit](SEO-AUDIT-2026-11-24.md). This gallery release adds no new office,
qualification, award, review or client claim.
