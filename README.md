# jeanpierreboutros.com

Personal portfolio of Jean-Pierre Boutros: live, studio and broadcast sound engineering, audio system integration, StudioJPB and Zynforge Audio.

Live site: https://www.jeanpierreboutros.com/

## Stack and structure

A static website using HTML, CSS and vanilla JavaScript. No framework, bundler, database or runtime package installation. Fonts load from Google Fonts; images and other assets are self-hosted.

- `build.py` generates `index.html` from the content and structured data.
- `styles.css` contains design tokens, responsive components and print styles.
- `main.js` handles navigation, progressive scroll reveals and native modal dialogs.
- `optimize_images.py` creates responsive WebP assets and metadata.
- `build_profile.py` creates the downloadable one-page professional profile.
- `output/pdf/jean-pierre-boutros-profile.pdf` is the published profile PDF.
- `photos/` holds originals; `photos/optimized/` holds generated derivatives.
- `.cpanel.yml` copies runtime files and photos to HostGator's document root.

The page follows: introduction → selected work → collaborations and television → biography and expertise → Zynforge → gallery → contact. Original section anchors, including `#tv`, remain valid.

## Editing content

Edit `build.py`, then regenerate with `python3 build.py`. The generator only needs Python's standard library. It fingerprints CSS and JavaScript URLs so deployed updates do not reuse stale browser caches. Rebuild after editing either asset, too. Do not hand-edit `index.html`.

- `artists`: existing artist and ensemble collaborations, without speculative role descriptions.
- `tv`: existing television credits and production formats.
- `zyn`: product names, categories, descriptions and icons.
- `gallery`: original filename, visible title, descriptive alternative text and context.
- `navigation`: shared desktop and mobile links.
- `jsonld` and the HTML template: metadata, selected projects, biography and contact.

Only add specific production roles, dates, venues, results and testimonials that are confirmed. The Papal Mass broadcast role, StudioJPB founding date and integration credits come from the original biography. The broadcast link is attributed to Vatican News; the Merwas record is attributed to Guinness World Records. Uncertain attendance figures and artist biographies have been removed.

The Eighties… The Knockout is featured with Jean-Pierre's confirmed FOH engineering role, his supplied signed artwork/cast photograph, and October 2026 production context from JACC's official event listing: https://tickets.jacc-kw.com/event/info/the-eighties--the-knockout/599. The original image is preserved, and both its feature and gallery view display the full composition.

The Marina Viotti gala is dated 8 September 2026 at Zouk Mikael's Roman Amphitheatre, using the festival's official programme: https://beirutoperafestival.com/the-festival/first-edition-2026/. Cartoon Orchestra is dated 4 October 2025 at JACC's National Theatre, matching the supplied poster and page 7 of JACC's official season calendar: https://jacc-kw.com/survey/calen/JACC_Season_Calendar_25-26.pdf. Jean-Pierre confirmed his FOH role for both events. Their HEIC sources remain untouched in Downloads; browser-compatible JPEG sources and responsive WebP derivatives are included in the site. FFmpeg was used for HEIC decoding because the system image converter produced blank output.

The product enquiry opens email because no confirmed public Zynforge product URL was supplied.

Abeer Nehme with the Qatar Philharmonic Orchestra is featured with Jean-Pierre's confirmed FOH role at U VENUE, Doha, on 23 January 2026. Concert context and the U Events production credit come from the orchestra's official listing: https://qatarphilharmonicorchestra.org/concert/abeer-nehme-with-qatar-philharmonic-orchestra/. The performance photograph shows Abeer and the orchestra together and comes from the organizer’s event gallery: https://uevents.me/en/events/abeer-nehme-with-qatar-philharmonic-orchestra. U Events / U VENUE attribution appears in the project, gallery and image viewer. The full composition and venue watermark are preserved. Image origin (DSC06098): https://uevents.me/storage/372/81dae70b-e952-4a5d-82c4-1eefb0fa1753.jpg.

Al Sharq Symphony features Jean-Pierre's confirmed FOH role for Marcel Khalifé and the Istanbul Philharmonic Orchestra, conducted by Lubnan Baalbaki. The organizer identifies the event as part of the Al Sharq Youth Annual Conference in Istanbul in 2017; later video/page publication dates are not treated as concert dates. The featured image is the organizer's official concert-video thumbnail, with visible Al Sharq Youth attribution in the project, gallery and image viewer. Sources: https://www.youtube.com/watch?v=hAZbbyPg7GE and https://youth.sharqforum.org/asy-gallery/al-sharq-symphony-marcel-khalife-and-istanbul-philharmonic-orchestra-conducted-by-lubnan-baalbaki/. Image origin: https://i.ytimg.com/vi/hAZbbyPg7GE/maxresdefault.jpg.

## Images

Original photographs are preserved. Responsive WebP derivatives use widths up to 480, 960 and 1600 pixels. Zynforge icons use 128px assets for their 64px display size. Images have intrinsic dimensions, responsive sources and meaningful alternative text. All except the hero load lazily.

After adding or replacing originals under `photos/`, run:

```sh
# Pillow is needed only for image preparation, not normal HTML builds.
python3 -m pip install Pillow
python3 optimize_images.py
python3 build.py
```

Commit the generated WebP files and `photos/optimized/manifest.json` with the HTML. A normal HTML build does not require Pillow. The generator stops if a referenced derivative is missing.

Gallery captions describe visible content and established portfolio facts. Add specific event/venue information when confirmed.

## Downloadable professional profile

The About and Contact sections offer a one-page A4 PDF with a biography, portrait, expertise, six selected productions, collaborators, studio and software work, television credits and clickable contact details. The download URL includes a content fingerprint so updated profiles do not reuse old cached files. The PDF is committed; normal website builds do not require PDF libraries.

To update it, edit `build_profile.py`, then run:

```sh
# A dedicated Python environment is recommended.
python3 -m pip install 'reportlab>=4.2,<5'
python3 build_profile.py
python3 build.py
```

The generator uses Georgia and Arial TTF fonts from macOS's supplemental fonts directory and embeds their subsets in the final PDF. For another build machine, set `JPB_PROFILE_FONT_DIR` to a directory containing the named font files. Render and inspect the complete page after changes; confirm one A4 page, selectable text, working links and no clipped or overlapping text. The generator rejects content that exceeds the page's reserved body area. The deploy manifest copies only the finished PDF from `output/pdf/`.

## Accessibility and behaviour

- Main landmark, skip link, named sections and visible keyboard focus.
- Native modal menu and image viewer: focus containment, Escape and background inertness.
- Descriptive gallery links, captions, live image counter and arrow-key navigation.
- Closing the image viewer restores focus to the originating photograph.
- Reduced-motion preferences disable animation, transitions and smooth scrolling.
- Motion includes a staged hero entrance, a gentle one-time image zoom, a decorative waveform, staggered grid reveals, card/link hover feedback and modal/photo fades. The visible pause control stops site animations. The waveform and hero zoom pause offscreen, when the tab is hidden, or while a modal is open. No animation represents live audio playback. A system reduced-motion preference is honoured on load and when changed; keyboard-focused content is shown immediately.
- Content and navigation work without JavaScript; gallery links open images directly.
- The menu closes when switching to desktop width.
- No audio or video starts automatically.

## Local preview and verification

Run `python3 -m http.server 8000 --bind 127.0.0.1` and open http://127.0.0.1:8000/.

Before deployment:

1. Run `python3 build.py`, `node --check main.js` and `git diff --check`.
2. Check desktop and mobile layouts, especially 320px and 400px widths.
3. Verify mobile menu keyboard focus, Escape, destination focus and scroll unlocking.
4. Open the gallery, navigate with arrow keys, close with Escape and check focus restoration.
5. Confirm images and section links resolve and project links point to the intended source.
6. Review the final local preview.

## Deployment

The existing HostGator/cPanel workflow is unchanged:

1. Push reviewed changes to `main` on GitHub.
2. In cPanel Git Version Control, update from remote and deploy the HEAD commit.
3. Hard-refresh the live site and check it again.

The deploy manifest targets `/home2/studiojp/public_html/`, confirmed in cPanel's Domains screen for jeanpierreboutros.com. It copies HTML, CSS, JavaScript, robots, sitemap, icons, the professional profile PDF and the complete photos directory, including optimized assets. Build scripts, this README and Git metadata are not published. Local edits and previews do not deploy the website.
