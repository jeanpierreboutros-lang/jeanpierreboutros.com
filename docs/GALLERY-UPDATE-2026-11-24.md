# RY X gallery update — 24 November 2026

Status: implementation and local validation complete; publication verification pending.

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

Publication must follow the passing checks above. The release will be pushed
to the existing repository and deployed through its established cPanel Git
workflow. Verify all 42 live canonical pages, referenced assets, new image
hashes and gallery interactions after deployment. A failed page/resource hash,
missing image, broken viewer, accessibility regression or changed layout is
a rollback trigger. The previous content release is `536f7f1`; the source
baseline before this addition is documentation commit `5e0b1dc`.

No Google/Bing ownership or sitemap configuration changes are needed for these
existing URLs. An IndexNow notification for the updated homepage is appropriate
after live verification. Submission does not establish indexing.
