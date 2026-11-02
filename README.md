# jeanpierreboutros.com

Personal portfolio of Jean-Pierre Boutros: FOH and monitor engineering, studio and broadcast sound engineering, audio system integration, StudioJPB and Zynforge Audio.

Live site: https://www.jeanpierreboutros.com/

Content and documentation reviewed: 2 November 2026. The website includes 28 canonical HTML pages, 18 project records, six service pages, 36 artist and ensemble collaborations, 24 gallery photographs, and a downloadable one-page professional profile. See [the implementation report](docs/SEO-IMPLEMENTATION-REPORT.md), [search registration steps](docs/SEARCH-CONSOLE.md) and [measurement plan](docs/MEASUREMENT.md).

## Portfolio presentation

The portfolio opens with Jean-Pierre's outdoor FOH photograph beside his name and a profile download near the top. The StudioJPB card and detail use the close-up of Manley outboard equipment. The opening flows directly into Selected Work.

The project browser starts with six featured projects: Nancy Ajram at L'Olympia, Abeer Nehme with the Qatar Philharmonic, Marcel Khalifé in Muscat, Al Shami at Ehdeniyat, Nancy's Baligh Hamdi Night monitor credit, and The Eighties in Kuwait. Filters expose all 18 projects or FOH, Monitors, Broadcast and Studio categories. Homepage image cards link to dedicated `/projects/<slug>/` pages and progressively open the complete sourced description in a native modal when JavaScript is available. The existing homepage project anchors still work. Each modal also offers an ordinary link to the full project page. Closing a project restores focus to its originating link. Opening a photograph inside a project uses the existing image viewer, and closing it returns to the project.

`projects` in `build.py` holds the compact card summaries and filter categories. Its order must match `PROJECT_DETAILS`; the build validates matching anchors. `featured_order` determines the opening selection. All 18 project descriptions remain available without JavaScript. The gallery initially shows six photographs of engineering work, with a control to show all 24; the image viewer always includes every photograph. The project header keeps its title, role and close button visible while scrolling. Links from a project to another section close the project and move focus to that section. The one-page PDF retains its current text and layout; its 11 production links now target the dedicated project pages. It is linked from the opening, About and Contact sections.

## Current project register

| Project | Jean-Pierre's role | Location and date | Website anchor |
| --- | --- | --- | --- |
| The Eighties... The Knockout | FOH engineer | JACC, Kuwait; October 2026 | `#the-eighties` |
| Marina Viotti - Opera gala | FOH engineer | Roman Amphitheatre, Zouk Mikael, Lebanon; 8 September 2026 | `#marina-viotti` |
| Cartoon Orchestra | FOH engineer | JACC National Theatre, Kuwait; 4 October 2025 | `#cartoon-orchestra` |
| Al Sharq Symphony - Marcel Khalifé and Istanbul Philharmonic | FOH engineer | Istanbul, Turkey; 2017; conductor Lubnan Baalbaki | `#al-sharq-symphony` |
| Abeer Nehme with Qatar Philharmonic Orchestra | FOH engineer | U VENUE, Doha, Qatar; 23 January 2026 | `#abeer-nehme-qatar` |
| Nancy Ajram - Baligh Hamdi Night | Monitor engineer for Nancy Ajram | Abu Bakr Salem Theatre, Riyadh; 9 November 2023 | `#baligh-hamdi-night` |
| Nancy Ajram - Warda Night | Monitor engineer for Nancy Ajram | Abadi Al Johar Arena, Jeddah; 4 July 2024 | `#warda-night` |
| Nancy Ajram - Night of Arab Stars | Monitor engineer for Nancy Ajram | Mohammed Abdu Arena, Riyadh Season; 31 December 2023 | `#night-of-arab-stars` |
| Lebanese National Philharmonic - Eternal Covenant | FOH engineer | Patriarchal Summer Residence, Diman, North Lebanon; 26 July 2026; conductor Harout Fazlian | `#lebanese-philharmonic-diman` |
| Nancy Ajram - L'Olympia | FOH engineer | L'Olympia, Paris, France; 10 June 2022 | `#nancy-ajram-olympia` |
| Marcel Khalifé - Royal Opera House Muscat | FOH engineer | House of Musical Arts, Muscat, Oman; 26-27 September 2019 | `#marcel-khalife-muscat` |
| Abeer Nehme - Ehdeniyat 2025 | FOH engineer | Ehdeniyat International Festival, Ehden, Lebanon; 25 July 2025 | `#ehdeniyat-abeer-nehme` |
| Al Shami - Ehdeniyat 2025 | FOH engineer | Ehdeniyat International Festival, Ehden, Lebanon; 3 August 2025 | `#ehdeniyat-al-shami` |
| Nancy Ajram - Infinite Nights, Expo 2020 Dubai | Monitor engineer for Nancy Ajram | Al Wasl Plaza, Dubai, UAE; 12 November 2021 | `#nancy-ajram-expo-dubai` |
| Adam - Ehdeniyat 2025 | Monitor engineer for Adam | Ehdeniyat International Festival, Ehden, Lebanon; 31 July 2025 | `#ehdeniyat-adam` |
| Papal Mass broadcast | Broadcast sound engineer | Beirut Waterfront, Lebanon; 2025 | `#papal-broadcast` |
| StudioJPB | Founder; recording, mixing and mastering | Jounieh, Lebanon; founded 2008 | `#studio-jpb` |
| Studio system integration | Audio system integration | Merwas Studios, Riyadh; Playsound Studios, Lebanon | `#studio-integration` |

Production roles come from Jean-Pierre's confirmations and original biography. Public sources support event names, dates, venues and programme details; they do not independently establish his engineering credits. Nancy Ajram's monitor credits apply specifically to her performances.

## Stack and structure

A static website using HTML, CSS and vanilla JavaScript. No framework, bundler, database or runtime package installation. The existing Fraunces and Hanken Grotesk fonts are self-hosted under `fonts/`, with their original Unicode ranges, font-display: swap and open licenses. Images and all runtime assets are self-hosted. Normal page requests need no third-party font stylesheet.

- `build.py` generates the homepage and invokes the static page generator.
- `services.py` holds the six service descriptions, FAQs and the reviewed content date.
- `search_pages.py` generates 27 additional HTML pages, shared metadata, linked JSON-LD entities, sitemap and robots files.
- `check_site.py` validates the generated inventory, links, metadata, images, specific credits and crawler rules.
- `hosting/seo.htaccess` contains domain-scoped canonical redirects; `hosting/install-seo.sh` merges the managed block and privately backs up existing rules.
- `fonts/` contains the original typefaces, CSS, provenance manifest and SIL Open Font Licenses.
- `styles.css` contains design tokens, responsive components and print styles.
- `main.js` handles navigation, progressive scroll reveals and native modal dialogs.
- `optimize_images.py` creates responsive WebP assets and metadata.
- `build_profile.py` creates the downloadable one-page professional profile.
- `output/pdf/jean-pierre-boutros-profile.pdf` is the published profile PDF.
- `photos/` holds originals; `photos/optimized/` holds generated derivatives.
- `.cpanel.yml` copies runtime files and photos to HostGator's document root.

The homepage follows: introduction → selected work → collaborations and television → biography, expertise and factual FAQs → Zynforge → gallery → contact. Its navigation, animation and original section anchors, including `#tv`, remain valid. Service links use the existing expertise list and a compact footer directory. Dedicated pages reuse the same palette, typography, navigation, imagery and layout components. English remains the maintained language; no incomplete translations or hreflang alternates are generated.

## Editing content

Edit `build.py`, then regenerate with `python3 build.py`. The generator needs Python 3.9 or later and only its standard library. It fingerprints CSS and JavaScript URLs so deployed updates do not reuse stale browser caches. Rebuild after editing either asset, too. Do not hand-edit `index.html`.

- `artists`: existing artist and ensemble collaborations, without speculative role descriptions.
- `tv`: existing television credits and production formats.
- `zyn`: product names, categories, descriptions and icons.
- `gallery`: original filename, visible title, descriptive alternative text and context.
- `gallery_sources`: photo attribution, coverage URL and original image URL for externally sourced photographs.
- `artist_projects`: role labels and project anchors for confirmed artist and ensemble credits.
- `navigation`: shared desktop and mobile links.
- The homepage template: selected projects, biography and contact. Shared metadata and linked JSON-LD are generated by `search_pages.py`.

Only add specific production roles, dates, venues, results and testimonials that are confirmed. The Papal Mass broadcast role, StudioJPB founding date and integration credits come from the original biography. The broadcast link is attributed to Vatican News; the Merwas record is attributed to Guinness World Records. Uncertain attendance figures and artist biographies have been removed.

Featured image links use explicit `gallery_data` indices and `data-gallery-index` values. When inserting or reordering gallery entries, update every affected project link and verify that its enlarged photograph and caption still match. Update this register, the content totals and `build_profile.py` whenever the documented selection changes.

## Event sources and photograph records

The Eighties… The Knockout is featured with Jean-Pierre's confirmed FOH engineering role, his supplied signed artwork/cast photograph, and October 2026 production context from JACC's official event listing: https://tickets.jacc-kw.com/event/info/the-eighties--the-knockout/599. The original image is preserved, and both its feature and gallery view display the full composition.

The Marina Viotti gala is dated 8 September 2026 at Zouk Mikael's Roman Amphitheatre, using the festival's official programme: https://beirutoperafestival.com/the-festival/first-edition-2026/. Cartoon Orchestra is dated 4 October 2025 at JACC's National Theatre, matching the supplied poster and page 7 of JACC's official season calendar: https://jacc-kw.com/survey/calen/JACC_Season_Calendar_25-26.pdf. Jean-Pierre confirmed his FOH role for both events. Their HEIC sources remain untouched in Downloads; browser-compatible JPEG sources and responsive WebP derivatives are included in the site. FFmpeg was used for HEIC decoding because the system image converter produced blank output.

The product enquiry opens email because no confirmed public Zynforge product URL was supplied.

Abeer Nehme with the Qatar Philharmonic Orchestra is featured with Jean-Pierre's confirmed FOH role at U VENUE, Doha, on 23 January 2026. Concert context and the U Events production credit come from the orchestra's official listing: https://qatarphilharmonicorchestra.org/concert/abeer-nehme-with-qatar-philharmonic-orchestra/. The performance photograph shows Abeer and the orchestra together and comes from the organizer’s event gallery: https://uevents.me/en/events/abeer-nehme-with-qatar-philharmonic-orchestra. U Events / U VENUE attribution appears in the project, gallery and image viewer. The full composition and venue watermark are preserved. Image origin (DSC06098): https://uevents.me/storage/372/81dae70b-e952-4a5d-82c4-1eefb0fa1753.jpg.

Al Sharq Symphony features Jean-Pierre's confirmed FOH role for Marcel Khalifé and the Istanbul Philharmonic Orchestra, conducted by Lubnan Baalbaki. The organizer identifies the event as part of the Al Sharq Youth Annual Conference in Istanbul in 2017; later video/page publication dates are not treated as concert dates. The featured image is the organizer's official concert-video thumbnail, with visible Al Sharq Youth attribution in the project, gallery and image viewer. Sources: https://www.youtube.com/watch?v=hAZbbyPg7GE and https://youth.sharqforum.org/asy-gallery/al-sharq-symphony-marcel-khalife-and-istanbul-philharmonic-orchestra-conducted-by-lubnan-baalbaki/. Image origin: https://i.ytimg.com/vi/hAZbbyPg7GE/maxresdefault.jpg.

Three Saudi Arabian Nancy Ajram projects credit Jean-Pierre specifically as her monitor engineer. Baligh Hamdi Night (Masterpieces of Baligh Hamdi) took place at Abu Bakr Salem Theatre, Riyadh, on 9 November 2023; concert context: https://www.harpersbazaararabia.com/culture/entertainment/baligh-hamdi-tribute. Its performance photo comes from Benchmark's media office, credited in Sayidaty's 10 November 2023 concert report (article 1692211); image origin: https://static.sayidaty.net/2023-11/298244.jpg. Warda Night took place at Abadi Al Johar Arena, Jeddah, on 4 July 2024, as confirmed by Jean-Pierre and GEA's official listing: https://enjoy.sa/en/events/warda-night/. Its Nancy-with-orchestra photo is attributed to Asharq Al-Awsat's 5 July 2024 coverage (article 5037424); image origin: https://static.srpcdigital.com/2024-07/704233.jpeg. Both photos have visible attribution in the project, gallery and image viewer. Nancy's credit does not imply responsibility for the other performers' monitor mixes.

Jean-Pierre also confirmed Night of Arab Stars (31 December 2023, Mohammed Abdu Arena, Riyadh Season) and his role as Nancy Ajram's monitor engineer. Sayidaty's 1 January 2024 concert report (article 1711121) supports the event context; Al Jamila's 7 January 2024 article (791121) explicitly credits the selected performance photo to Rotana Live's official Instagram account. The photo is preserved as downloaded, with visible attribution in the project, gallery and image viewer. The concert welcomed 2024; the performance date remains 31 December 2023.

The Diman project uses Jean-Pierre's supplied IMG_2750.HEIC, converted to JPEG for the responsive image pipeline. Its creation date (26 July 2026) matches the Maronite Patriarchate's official report of “Eternal Covenant” (العهد الأبدي) at the Patriarchal Summer Residence: https://bkerki.org/news-article/امسية-موسيقية-بعنوان-عهد-أبدي/. The report confirms the Lebanese National Philharmonic Orchestra, conductor Harout Fazlian and the beatification context. Jean-Pierre confirmed his role as FOH engineer. The supplied photograph was retained after comparing the official gallery and accessible press photos: it offers the strongest full-orchestra view among the inspected alternatives. The HEIC remains untouched in Downloads; the site uses `photos/lebanese-philharmonic-diman-2026.jpg` and its WebP derivatives.

Nancy Ajram at L'Olympia, Paris, is a separate FOH credit confirmed by Jean-Pierre. The concert date is 10 June 2022, shown on the poster in Nancy's official announcement (https://x.com/NancyAjram/status/1485663322015944711) and the event listing (https://www.parisbouge.com/events/234789). Her official concert recap was published on 13 June 2022: https://www.youtube.com/watch?v=4l2mWDhjhtk. The performance photograph comes from FilFan's 12 June 2022 report of artist-shared concert images: https://www.filfan.com/news/147643; image origin: https://media.filfan.com/NewsPics/FilfanNew/large/389566_0.PNG. The PNG was converted to JPEG with the full composition retained. FilFan attribution appears in the project, gallery and image viewer. The Olympia FOH role is distinct from the four monitor credits in Saudi Arabia and Dubai.

Marcel Khalifé's 2019 Muscat project also carries Jean-Pierre's confirmed FOH credit. The official archive lists 26 and 27 September 2019 at the House of Musical Arts, part of the Royal Opera House Muscat: https://rohmuscat.org.om/en/performance/performance-detail?i=404. The venue's 21 September 2019 announcement confirms pianist Rami Khalifé's participation: https://rohmuscat.org.om/en/media-centre/press-release-detail?i=140. The concert photograph is attributed to Oman Observer's contemporary review: https://www.omanobserver.om/article/23830/Main/marcel-khalife-created-his-own-global-sound-world; image origin: https://www.omanobserver.om/uploads/imported_images/uploads/2019/09/IMG_4593.jpg. Attribution appears in the project, gallery and image viewer. Marcel's collaboration label now covers both Istanbul and Muscat.

Jean-Pierre confirmed his monitor-engineering role for Nancy Ajram's Infinite Nights performance at Expo 2020 Dubai. The show took place on 12 November 2021 at Al Wasl Plaza, as confirmed by Dubai Media Office's 8 November 2021 announcement: https://mediaoffice.ae/en/news/2021/November/08-11/Expo-2020-Dubai-latest-visit-figure-approaches-3-million. The official concert archive provides programme context and the selected band photograph: https://virtualexpodubai.com/listen-watch/events/infinite-nights-starring-ragheb-alama-and-nancy-ajram. Image origin: https://images.ctfassets.net/opz1rk40r4ou/1Z8NDz0CUIBH8xHsnKBvCu/e7dab9c5f3fa9c5b5cc9fd1912a19dbd/Expo_Nights_Nancy_54.jpg?fm=jpg&q=90&w=1600. Expo 2020 Dubai / Virtual Expo attribution appears in the project, gallery and image viewer. The event retains its official Expo 2020 name; the performance year is 2021. Jean-Pierre's credit applies to Nancy's show.

Jean-Pierre confirmed three artist-specific roles at Ehdeniyat International Festival 2025: FOH for Abeer Nehme on 25 July and Al Shami on 3 August, and monitors for Adam on 31 July. Dates match the published festival programme at https://lebanonuntravelled.com/ehdeniyat-international-festival-2025/ and the archived ticketing information at https://www.ticketingboxoffice.com/news/details/2941/. Each show has its own project card and gallery image; the artist collaboration labels identify the corresponding role. These entries credit the named artist's performance rather than the complete festival.

Abeer Nehme's performance photo is credited by L'Orient-Le Jour to Ehdeniyat Festival: https://today.lorientlejour.com/article/1471284/at-ehdeniyat-abeer-nehme-reaches-saltana.html. Its 28 July 2025 review also supports the choir and Marc Abou Naoum programme context. Image origin: https://s.lorientlejour.com/storage/attachments/1472/PIE_9590_836549.jpg/r/2400/PIE_9590_836549.jpg. Visible attribution is Ehdeniyat Festival / L'Orient-Le Jour.

Al Shami's stage photo comes from Cairo24's 4 August 2025 concert report: https://www.cairo24.com/2256107. Image origin: https://www.cairo24.com/Upload/libfiles/163/0/191.jpg. The full portrait composition, including the LED stage and effects, is retained and credited to Cairo24.

Adam's performance portrait comes from the dated Beiruting event gallery: https://www.beiruting.com/events/43820/adam-at-ehdeniyat-festival. Image origin: https://api.beiruting.com/images/1210x807xi/527531944_1336761888016831_8705915139313954408_n.webp. The WebP was converted to JPEG with its full composition retained. The 1 August 2025 report from festival media partner Aghani Aghani confirms the previous evening's show and its Ziad Rahbani tribute: https://aghaniaghani.com/news/regional-celebrities/آدم-يُشعل-مسرح-إهدنيات-الدولي-بلحظات-إ/. Visible photo attribution is Beiruting.

## Images

Original photographs are preserved. Responsive WebP derivatives use widths up to 480, 960 and 1600 pixels. Zynforge icons use 128px assets for their 64px display size. Images have intrinsic dimensions, responsive sources and meaningful alternative text. The homepage hero and service introduction photographs load eagerly; below-the-fold images load lazily.

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

The opening, About and Contact sections offer a one-page A4 PDF with a biography, portrait, seven areas of expertise, nine production groups covering sixteen concert productions or broadcasts, studio and software work, television credits and clickable contact details. A compact Ehdeniyat 2025 block lists Abeer Nehme and Al Shami as FOH credits and Adam as a monitor credit, with each date and links to the project cards. Nancy Ajram's group identifies the Olympia FOH role separately from her four monitor credits in Dubai and Saudi Arabia. Marcel Khalifé's group covers Al Sharq Symphony in Istanbul and the Muscat concert engagement. The Diman FOH project is also included. Nancy's grouped monitor credits use years in the profile; the website project cards and register retain the complete dates and venues. The complete collaboration list remains on the website. The download URL includes a content fingerprint so updated profiles do not reuse old cached files. The PDF is committed; normal website builds do not require PDF libraries.

Its text and one-page layout are unchanged in the SEO release; production links point directly to canonical project pages. To update it, edit `build_profile.py`, then run:

```sh
python3 -m venv /private/tmp/jpb-profile-venv
/private/tmp/jpb-profile-venv/bin/python -m pip install 'reportlab>=4.2,<5'
/private/tmp/jpb-profile-venv/bin/python build_profile.py
python3 build.py
```

Reuse an existing environment instead of recreating it when ReportLab is already installed. The generator uses Georgia and Arial TTF fonts from macOS's supplemental fonts directory and embeds their subsets in the final PDF. For another build machine, set `JPB_PROFILE_FONT_DIR` to a directory containing the named font files. Render and inspect the complete page after changes; confirm one A4 page, selectable text, working links and no clipped or overlapping text. Poppler or PyMuPDF can render the page for inspection. The generator rejects content that exceeds the page's reserved body area. Rebuilding `build.py` after the PDF updates both download fingerprints and the displayed size. The deploy manifest copies only the finished PDF from `output/pdf/`.

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

1. Run `python3 build.py`, `python3 check_site.py`, `node --check main.js`, `sh -n hosting/install-seo.sh` and `git diff --check`. For domain/range checks, download the official Schema.org vocabulary separately and run `python3 check_site.py --vocabulary /path/to/schemaorg-current-https.jsonld`. No network request is made by the checker.
2. Check desktop and mobile layouts, especially 320px and 400px widths.
3. Verify mobile menu keyboard focus, Escape, destination focus and scroll unlocking.
4. Verify Featured (6), All work (18), FOH (10), Monitors (5), Broadcast (1), and Studio (2) filters. Open a project, enlarge its image, close the image viewer with Escape, then close the project and check focus restoration. Test a direct project URL and the gallery show-all control. Check the full descriptions remain available without JavaScript.
5. Confirm images and section links resolve and project links point to the intended source.
6. If the PDF changed, render and inspect it; verify all production dates and roles, one A4 page, embedded fonts, and working project/contact links. Check all three website download links use the new PDF fingerprint and size.
7. Review the final local preview. For documentation-only changes, validate the affected records and links; repeat interaction checks when behavior changes.

## Deployment

Repository: https://github.com/jeanpierreboutros-lang/jeanpierreboutros.com.git. Published branch: `main`. HostGator's cPanel checkout is `/home2/studiojp/repositories/jeanpierreboutros.com`.

1. Push reviewed changes to `main` on GitHub.
2. In cPanel Git Version Control, choose the existing repository and update from remote. Confirm the HEAD SHA equals the pushed commit.
3. Deploy HEAD and wait for completion. Confirm Last Deployed SHA equals the intended release.
4. Hard-refresh https://www.jeanpierreboutros.com/ and https://jeanpierreboutros.com/. Check all sitemap URLs, affected projects, service pages, updated images and all three profile download links. Verify HTTP/apex/index.html redirects to the HTTPS www canonical, a real 404, search crawler access and GPTBot exclusion. Compare downloaded PDF bytes with the committed artifact when the profile changes.

The deploy manifest targets `/home2/studiojp/public_html/`, confirmed in cPanel's Domains screen for jeanpierreboutros.com. It copies the 28 static pages, fonts, CSS, JavaScript, robots, sitemap, the supplementary llms.txt directory, icons, profile PDF and complete photos directory. Assets and new pages are copied before the homepage and discovery files. Build scripts, the SEO report, this README and Git metadata are not published. Local edits and previews do not deploy the website.

The document root is shared with the existing main hosting site. Deployment copies files without purging other content or changing domain mappings. The redirect installer prepends only the clearly marked JPB block, preserves existing non-JPB .htaccess rules, rejects malformed managed blocks and symlinked .htaccess files, and stores backups in the private repository’s `.deployment-backups/`. Every redirect is conditional on jeanpierreboutros.com or www.jeanpierreboutros.com, so the other domain is unaffected. Inspect live behaviour after deployment; local Apache/TLS tests cover canonical redirects and preservation of existing access restrictions.

### Rollback

If a release introduces a broken page, incorrect credit or inaccessible download, revert its commit on `main` with `git revert RELEASE_COMMIT_SHA`, review the resulting runtime files, and push the revert. Update from remote and deploy that new HEAD in cPanel. Verify Last Deployed SHA and the restored live page/PDF. Keep unrelated shared hosting files untouched. Reverting code alone does not remove the managed .htaccess block: restore the appropriate private `.deployment-backups/htaccess-before-jpb.*` backup in cPanel if redirect rules need rollback. Preserve the current non-JPB rules if they changed after that backup. Newly added static pages remain on the non-purging host until explicitly removed; remove only this release’s generated service/project pages if a full rollback is required, or retain their valid content while restoring the homepage.
