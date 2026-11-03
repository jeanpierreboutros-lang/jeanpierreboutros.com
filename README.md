# jeanpierreboutros.com

Personal portfolio of Jean-Pierre Boutros: FOH and monitor engineering, studio and broadcast sound engineering, audio system integration, StudioJPB and Zynforge Audio.

Live site: https://www.jeanpierreboutros.com/

Documentation reconciled: 3 November 2026. The published website includes 39 canonical HTML pages, 28 project records, six service pages, 41 artist and ensemble collaborations, 34 gallery photographs, 51 studio release entries across 27 credited artists, and a downloadable one-page professional profile. HostGator deployed content release `24ec55e` on 3 November 2026 (Asia/Beirut).

## Documentation and evidence

These files are repository documentation and are excluded from the public website deployment. Research dates record when sources were checked; reconciliation dates record when documentation was aligned with the published release. Historical test results retain their original scope and measurements.

| Document | Purpose and scope |
| --- | --- |
| [Implementation report](docs/SEO-IMPLEMENTATION-REPORT.md) | Current architecture, content inventory, release history and verification limits |
| [Search registration](docs/SEARCH-CONSOLE.md) | Production checks and outstanding Google/Bing ownership and sitemap setup |
| [Measurement plan](docs/MEASUREMENT.md) | Published baseline and future search/inquiry measurement |
| [Portfolio release verification](docs/portfolio-release-verification-2026-11-03.json) | Current release: 39 pages and 152 referenced resources matched live bytes |
| [Studio credit research](docs/studio-credit-research.json) | All 41 collaboration names, exact role decisions and 51 unique release entries |
| [Nancy Ajram review](docs/nancy-credit-research-2026-11-02.json) | Five published song credits and limits on unconfirmed work |
| [Broader name review](docs/broad-credit-research-2026-11-02.json) | Six approved additions, unselected leads and the owner's two exclusions |
| [Recorded search queries](docs/studio-credit-search-queries.json) | Historical query batches; not an exhaustive log of every later search |
| [Pre-SEO audit](docs/audit-before.json) | Historical observations before the original SEO release |
| [Apache fixture](docs/apache-checks.json) | Historical 2 November local tests of the original 28-page SEO release |
| [External links](docs/external-links.json) | Historical 30-target audit; not a current audit of every studio release link |
| [PageSpeed attempts](docs/pagespeed-attempt.json) | Historical mobile/desktop HTTP 429 results; no performance score obtained |
| [Font provenance](fonts/README.md) | Self-hosted font sources, subset behavior and licenses |

## Portfolio presentation

The portfolio opens with Jean-Pierre's outdoor FOH photograph beside his name and a profile download near the top. The StudioJPB card and detail use the close-up of Manley outboard equipment. The opening flows directly into Selected Work.

The project browser starts with six featured projects: Nancy Ajram at L'Olympia, Abeer Nehme with the Qatar Philharmonic, Marcel Khalifé in Muscat, Al Shami at Ehdeniyat, Nancy's Baligh Hamdi Night monitor credit, and The Eighties in Kuwait. Filters expose all 28 projects or FOH, Monitors, Broadcast, Studio and Technical categories. Homepage image cards link to dedicated `/projects/<slug>/` pages and progressively open the complete sourced description in a native modal when JavaScript is available. The existing homepage project anchors still work. Each modal also offers an ordinary link to the full project page. Closing a project restores focus to its originating link. Opening a photograph inside a project uses the existing image viewer, and closing it returns to the project.

`projects` in `build.py` holds the compact card summaries and filter categories. Its order must match `PROJECT_DETAILS`; the build validates matching anchors. `featured_order` determines the opening selection. All 28 project descriptions remain available without JavaScript. The gallery initially shows six photographs of engineering work, with a control to show all 34; the image viewer always includes every photograph. The project header keeps its title, role and close button visible while scrolling. Links from a project to another section close the project and move focus to that section. The one-page PDF includes the confirmed production roles and 16 links to dedicated project pages. It is linked from the opening, About and Contact sections.

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
| Marcel Khalifé - Amman Citadel | Monitor & recording engineer | Amman Citadel, Jordan Festival, Amman, Jordan; 13 September 2016 | `#marcel-khalife-amman` |
| Abeer Nehme - Baalbeck International Festival | FOH engineer | Temple of Bacchus, Baalbeck, Lebanon; 19 August 2016 | `#abeer-nehme-baalbeck` |
| On the Steps of Marco Polo - Abeer Nehme, Charbel Rouhana and cast | Audio technical supervision | Beiteddine Palace, Lebanon; 21-22 June 2013 | `#beiteddine-marco-polo` |
| Carole Samaha - Golden Album | Mixing & mastering engineer | Album released 3 March 2023 | `#carole-samaha-golden-album` |
| Zade Dirani - Palais des Congrès | FOH engineer | Palais des Congrès, Dbayeh, Lebanon; 11 October 2018 | `#zade-dirani-dbayeh` |
| Zade Dirani - The Hope Concert | FOH engineer | Royal Cultural Palace, Amman, Jordan; 22 February 2019 | `#zade-dirani-amman` |
| Marcel Khalifé - Ode to a Homeland | FOH engineer | Steps of the Temple of Bacchus, Baalbeck, Lebanon; 5 July 2019 | `#marcel-khalife-baalbeck` |
| Nancy Ajram - Bnoss Jounieh | FOH engineer | Fouad Chehab Stadium, Jounieh, Lebanon; 18 August 2022 | `#nancy-ajram-jounieh` |
| Mazeej by Lucas Sakr - On Stage at NDU | FOH engineer | Bechara El Rahi Theater, NDU, Zouk Mosbeh, Lebanon; 11 March 2019 | `#mazeej-ndu` |
| Beirut the Sea Lover | 3D sound mixing | Roman Baths, downtown Beirut, Lebanon; 14 June 2019 | `#beirut-the-sea-lover` |

Production roles come from Jean-Pierre's confirmations, original biography or explicit published engineering credits. Event coverage alone establishes context, not his engineering assignment; the official Beirut the Sea Lover page explicitly names his 3D sound mixing credit. Nancy Ajram's monitor credits apply specifically to her performances.

## Stack and structure

A static website using HTML, CSS and vanilla JavaScript. No framework, bundler, database or runtime package installation. The existing Fraunces and Hanken Grotesk fonts are self-hosted under `fonts/`, with their original Unicode ranges, font-display: swap and open licenses. Images and all runtime assets are self-hosted. Normal page requests need no third-party font stylesheet.

- `build.py` generates the homepage and invokes the static page generator.
- `services.py` holds the six service descriptions, FAQs and the reviewed content date.
- `studio_credits.py` holds 51 song/album entries, their exact engineering scope and source notes excluded from rendered pages; it generates the homepage disclosures and `/studio-credits/`.
- `docs/studio-credit-research.json` reconciles the initial 36-name audit and five added artists to all 41 current collaboration names; the research records above preserve role evidence, owner confirmations and recorded search batches.
- `search_pages.py` generates 38 additional HTML pages, shared metadata, linked JSON-LD entities, sitemap and robots files.
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

Edit `build.py` for portfolio content, `studio_credits.py` for song/album credits, `services.py` for services and FAQs, and `search_pages.py` for shared page generation, metadata and structured data. Regenerate with `python3 build.py`. The generator needs Python 3.9 or later and only its standard library. It fingerprints CSS and JavaScript URLs so deployed updates do not reuse stale browser caches. Rebuild after editing either asset, too. Do not hand-edit generated HTML, sitemap, robots or `llms.txt` files. Keep research evidence and publication decisions in the corresponding documentation records.

- `artists`: existing artist and ensemble collaborations, without speculative role descriptions.
- `tv`: existing television credits and production formats.
- `zyn`: product names, categories, descriptions and icons.
- `gallery`: original filename, visible title, descriptive alternative text and context.
- `gallery_sources`: photo attribution, coverage URL and original image URL for externally sourced photographs.
- `artist_projects`: role labels and project anchors for confirmed artist and ensemble credits.
- `navigation`: shared desktop and mobile links.
- The homepage template: selected projects, biography and contact. Shared metadata and linked JSON-LD are generated by `search_pages.py`.

Only add specific production roles, dates, venues, results and testimonials that are confirmed. The Papal Mass broadcast role, StudioJPB founding date and integration credits come from the original biography. The broadcast link is attributed to Vatican News; the Merwas record is attributed to Guinness World Records. Uncertain attendance figures and artist biographies have been removed.

Featured image links use explicit `gallery_data` indices and `data-gallery-index` values. When inserting or reordering gallery entries, update every affected project link and verify that its enlarged photograph and caption still match. Update this register and the content totals whenever the inventory changes. Review `build_profile.py` when its selected credits change; the one-page PDF is a selection, not an exhaustive project or song list.

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

Marcel Khalifé's 2019 Muscat project also carries Jean-Pierre's confirmed FOH credit. The official archive lists 26 and 27 September 2019 at the House of Musical Arts, part of the Royal Opera House Muscat: https://rohmuscat.org.om/en/performance/performance-detail?i=404. The venue's 21 September 2019 announcement confirms pianist Rami Khalifé's participation: https://rohmuscat.org.om/en/media-centre/press-release-detail?i=140. The concert photograph is attributed to Oman Observer's contemporary review: https://www.omanobserver.om/article/23830/Main/marcel-khalife-created-his-own-global-sound-world; image origin: https://www.omanobserver.om/uploads/imported_images/uploads/2019/09/IMG_4593.jpg. Attribution appears in the project, gallery and image viewer. Marcel's collaboration label covers FOH in Istanbul, Muscat and Baalbeck, plus monitors and recording in Amman.

Jean-Pierre confirmed his monitor-engineering role for Nancy Ajram's Infinite Nights performance at Expo 2020 Dubai. The show took place on 12 November 2021 at Al Wasl Plaza, as confirmed by Dubai Media Office's 8 November 2021 announcement: https://mediaoffice.ae/en/news/2021/November/08-11/Expo-2020-Dubai-latest-visit-figure-approaches-3-million. The official concert archive provides programme context and the selected band photograph: https://virtualexpodubai.com/listen-watch/events/infinite-nights-starring-ragheb-alama-and-nancy-ajram. Image origin: https://images.ctfassets.net/opz1rk40r4ou/1Z8NDz0CUIBH8xHsnKBvCu/e7dab9c5f3fa9c5b5cc9fd1912a19dbd/Expo_Nights_Nancy_54.jpg?fm=jpg&q=90&w=1600. Expo 2020 Dubai / Virtual Expo attribution appears in the project, gallery and image viewer. The event retains its official Expo 2020 name; the performance year is 2021. Jean-Pierre's credit applies to Nancy's show.

Jean-Pierre confirmed three artist-specific roles at Ehdeniyat International Festival 2025: FOH for Abeer Nehme on 25 July and Al Shami on 3 August, and monitors for Adam on 31 July. Dates match the published festival programme at https://lebanonuntravelled.com/ehdeniyat-international-festival-2025/ and the archived ticketing information at https://www.ticketingboxoffice.com/news/details/2941/. Each show has its own project card and gallery image; the artist collaboration labels identify the corresponding role. These entries credit the named artist's performance rather than the complete festival.

Abeer Nehme's performance photo is credited by L'Orient-Le Jour to Ehdeniyat Festival: https://today.lorientlejour.com/article/1471284/at-ehdeniyat-abeer-nehme-reaches-saltana.html. Its 28 July 2025 review also supports the choir and Marc Abou Naoum programme context. Image origin: https://s.lorientlejour.com/storage/attachments/1472/PIE_9590_836549.jpg/r/2400/PIE_9590_836549.jpg. Visible attribution is Ehdeniyat Festival / L'Orient-Le Jour.

Al Shami's stage photo comes from Cairo24's 4 August 2025 concert report: https://www.cairo24.com/2256107. Image origin: https://www.cairo24.com/Upload/libfiles/163/0/191.jpg. The full portrait composition, including the LED stage and effects, is retained and credited to Cairo24.

Adam's performance portrait comes from the dated Beiruting event gallery: https://www.beiruting.com/events/43820/adam-at-ehdeniyat-festival. Image origin: https://api.beiruting.com/images/1210x807xi/527531944_1336761888016831_8705915139313954408_n.webp. The WebP was converted to JPEG with its full composition retained. The 1 August 2025 report from festival media partner Aghani Aghani confirms the previous evening's show and its Ziad Rahbani tribute: https://aghaniaghani.com/news/regional-celebrities/آدم-يُشعل-مسرح-إهدنيات-الدولي-بلحظات-إ/. Visible photo attribution is Beiruting.

Marcel Khalifé at Amman Citadel is a monitor and recording credit confirmed by Jean-Pierre. The Jordan Times' festival announcement supports 13 September 2016 and the Jordan Festival context: https://jordantimes.com/news/local/jordan-host-international-artists-bands-summer-remember%E2%80%99. The concert photo comes from photographer Ali Barqawi's own 2016 Amman Citadel collection: https://www.alibarqawistudios.com/music-festivals; original image: https://images.squarespace-cdn.com/content/v1/52a47d3de4b06e67e555171a/1604348542791-XRIIAD43439NZXZLL331/Ali-Barqawi-Studios-Art-Series-Music-Event-Amman-Citadel-Festival-Marcel-Khalifeh-Jordan-2016-053.jpg. It replaces the preliminary MTV close-up and preserves the original photographer/copyright metadata. Roya Music's indexed Citadel clips were checked; their matching image endpoints returned 404, so they were not used as image sources. The project belongs to the Monitors filter and is also linked from Recording & tracking and the Jordan section of International projects.

Abeer Nehme's Baalbeck FOH role and the 19 August 2016 engagement were confirmed by Jean-Pierre. The official programme identifies “Al Mutanabbi… Mousafiran Abadan” and the Temple of Bacchus: https://www.baalbeck.org.lb/programs/abeer-nehme/. Its migrated date field shows 1 January; use the confirmed 19 August date, corroborated by the contemporary ticketing archive: https://www.ticketingboxoffice.com/media/Events-Media/9012/en and MTV's published festival programme: https://www.mtv.com.lb/news/615743. The photograph is from the festival's 2016 highlights archive: https://www.baalbeck.org.lb/highlights/?program=highlights#798; original image: https://www.baalbeck.org.lb/wp-content/uploads/2016/05/abeernehme2016-1.jpg. Visible attribution is Baalbeck International Festival. All four new originals retain their full compositions. Their appended gallery indices (24-27) preserve all existing image links.

“On the Steps of Marco Polo: A Musical Journey on the Silk Road” opened Beiteddine Art Festival on 21-22 June 2013. Jean-Pierre confirmed audio technical supervision, rather than FOH. The dated production archive names Abeer Nehme, Charbel Rouhana, Rafic Ali Ahmad, artistic director Alain Weber, musical director Kyriakos Kalaitzidis and the Lebanese Philharmonic conducted by Lubnan Baalbaki: https://www.ticketingboxoffice.com/media/Events-Media/6577/en and https://www.ticketingboxoffice.com/media/bf-silk-road-marco-polo-22-june-13sat/6578/en. The card uses the original production artwork, clearly identified as artwork: https://cdn.ticketingboxoffice.com/uploadImages/EventsPics/B-6577-635035519961590527.JPG. The Technical filter includes this supervision project and Beirut the Sea Lover’s 3D sound mixing.

Jean-Pierre confirmed mixing and mastering Carole Samaha’s Golden Album. Her official “Beirut” release credits name him and Studio Playsound Lebanon: https://www.youtube.com/watch?v=M--KeGtmvgM. Apple Music confirms 3 March 2023, 12 tracks and the artwork: https://music.apple.com/us/album/golden-album/1675126762. The album track list is retained in the research data. Mixing & mastering links to this album project as selected experience.

Zade Dirani: Jean-Pierre confirmed FOH mixing for Palais des Congrès, Dbayeh (11 October 2018), and The Hope Concert, Amman (22 February 2019). The dated Dbayeh programme and artwork come from https://www.ticketingboxoffice.com/media/Events-Media/11365/en; event context is also corroborated by Taawon’s partner ULYP: https://unitelebanonyouth.wordpress.com/tag/concert/. The Amman venue, date and charity context are confirmed by the King Hussein Cancer Foundation: https://www.khcc.jo/en/news/under-the-patronage-of-hrh-princess-ghida-talal-khcf-to-hold-charity-concert-with-renowned-pianist-and-composer-zade-dirani. Its image is the thumbnail of Zade’s official 2019 concert highlights: https://www.youtube.com/watch?v=pkbnvbAltXk. These sources establish event context; Jean-Pierre directly confirmed his engineering assignment. No additional production stages are inferred.

Jean-Pierre confirmed concert mixing for Marcel Khalifé’s Ode to a Homeland (5 July 2019, Baalbeck) and Nancy Ajram’s Bnoss Jounieh concert (18 August 2022, Fouad Chehab Stadium). These are listed as FOH mixing in the live portfolio. Marcel’s date/title are in the official programme https://www.baalbeck.org.lb/programs/marcel-khalife/; the steps of the Temple of Bacchus venue is corroborated by https://www.prestigemag.co/2019/05/baalbeck-international-festival-2019-program/. The photograph is the festival’s archive image attached to its 2019 programme at https://www.baalbeck.org.lb/highlights/?program=highlights#2615. Its capture date is not independently established; the older upload-directory date is not treated as the concert date. Nancy’s date/venue are recorded in https://www.ticketingboxoffice.com/media/we-are-lebanon-18-aug-22-thurs/19612/en; the linked full concert and its thumbnail are from her official artist upload https://www.youtube.com/watch?v=blbqRLqgoEU. No other contributors’ engineering or production credits are shown.

Mazeej by Lucas Sakr: Jean-Pierre confirmed FOH for the NDU concert, then corrected his initial 12 March date to 11 March 2019 after reviewing the archive. The original event artwork explicitly identifies Monday 11 March, Bechara El Rahi Theater, NDU, Zouk Mosbeh, in collaboration with the NDU School of Music: https://www.ticketingboxoffice.com/media/mazeej-11-mar19-mon/11892/en. The same-day agenda corroborates the NDU theatre: https://www.lorientlejour.com/article/1161014/concerts.html. The published page uses the original event artwork, labelled as artwork.

## Studio credit research

The current audit covers all 41 artist/ensemble collaboration names. The published directory contains 51 unique song/album entries across 27 credited artists, arranged in 27 groups. A shared release appears once in the directory even when it is documented under both artists in the research audit. Albums count as one entry; private track lists do not increase the total.

Thirteen entries carry Jean-Pierre’s direct role confirmations: Salah El Kurdi’s Taii Nkhoun; Ria Ellinidou’s Στα Κόκκινα and Όταν Αγαπάς; Salim Assaf’s Shu Hal Hob and Eza Fik; Ramy Ayach’s Ma Bensak; Abeer Nehme’s Fallou, Hikayi, Fi Asfour and Kil Ma T’illi; Al Walid Hallani’s Zeffo El Amar; Mohammed Islam’s Nheb El Dini; and Rasha Rizk’s اللعبة (The Play). Their links identify official artist/label releases, album audio or the Spotify album. A release link identifies the work; the owner confirmation establishes the role where a public engineering credit was not found. Cyrine Abdel Nour’s Aamellon Aeqdi is corroborated by her official music video.

The deeper Nancy Ajram review and later broad-name search establish five published songs: Men Nazra, Aamon Jadidon, Ya Eid and Akher Esdar for mixing/mastering, and Warana Eh for recording. The broader research added five studio release entries and one live production project, detailed below. Other collaboration names retain their existing live work without an inferred studio role. The linked research records preserve the source dates, version distinctions and publication decisions.

The homepage offers native artist disclosures and a link to the complete `/studio-credits/` directory. At Jean-Pierre’s request, entries show the project/song title and his engineering credit only; title links open the release or project. Other contributors, research notes, source labels, dates and album track lists are not rendered. Studio-only credits remain attributed to Studio Jean-Pierre Boutros, without inferring a personal engineering role. Naseej is labelled vocal recording for selected takes. Related collaborators retain plain artist names without songwriting or performance-role credits. Named conductor/director credits were also removed from project copy and the downloadable profile. Image attribution remains with the photographs. Research files, source generators and notes are excluded from public deployment; the complete generated studio directory is included.

Published on 3 November 2026 after owner approval, the six selected broader-search findings are: Nancy Ajram’s Akher Esdar (mixing/mastering), Marwan Chami’s Tayer (mixing/mastering), Nader Khoury’s Idi bi Idik (recording studio), Georges Nehme’s Moving Mountains (selected vocal recording), Abeer Nehme’s Addaysh Bhebak (recording studio), and Beirut the Sea Lover (3D sound mixing). Maher Zain and Between the two Blacks were explicitly excluded from the portfolio. Moving Mountains links to the OK World album release and retains its precise vocal scope from the CD personnel notes at https://musicbase.net/ok-world. Addaysh Bhebak uses the official artist video https://www.youtube.com/watch?v=-NSBIfNe7pA with studio attribution corroborated by https://www.mtv.com.lb/news/1250854. Idi bi Idik links to the original UN announcement https://unicbeirut.org/index.php/Press%20Release/create-press-releases-32. The complete Beirut Spring Festival archive https://www.beirutspringfestival.org/beirut-the-sea-lover/2019/en names Jean-Pierre for 3D sound mixing and supplies the projection image. This production appears under Technical, without inferring a FOH role. All these additions are included in deployed content release `24ec55e`. Unselected Mawwal and Photo Umbrella leads remain research-only. Shou Baamel retains its narrower 2022 album mastering/studio credit; the 2025 video lead does not expand that role without version confirmation.

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

The opening, About and Contact sections offer a one-page A4 PDF with a biography, portrait, seven areas of expertise, ten production groups covering nineteen concert productions or broadcasts and Golden Album, studio and software work, television credits and clickable contact details. A compact Ehdeniyat 2025 block lists Abeer Nehme and Al Shami as FOH credits and Adam as a monitor credit, with each date and links to the project cards. Nancy Ajram's group identifies the Olympia FOH role separately from her four monitor credits in Dubai and Saudi Arabia. Marcel Khalifé's group covers FOH for Al Sharq Symphony in Istanbul and the Muscat engagement, plus monitors and recording at Amman Citadel. Abeer Nehme's group includes FOH in Qatar and Baalbeck and audio technical supervision for On the Steps of Marco Polo at Beiteddine with Charbel Rouhana; her Ehdeniyat credit remains in the festival block. Carole Samaha’s Golden Album mixing/mastering credit appears under Studio & systems. The footer links to the full studio credits directory. The Diman FOH project is also included. Nancy's grouped monitor credits use years in the profile; the website project cards and register retain the complete dates and venues. The complete collaboration list remains on the website. The download URL includes a content fingerprint so updated profiles do not reuse old cached files. The PDF is committed; normal website builds do not require PDF libraries.

The profile remains one A4 page; production links point directly to canonical project pages. To update it, edit `build_profile.py`, then run:

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
4. Verify Featured (6), All work (28), FOH (16), Monitors (6), Broadcast (1), Studio (3), and Technical (2) filters. Open a project, enlarge its image, close the image viewer with Escape, then close the project and check focus restoration. Test a direct project URL and the gallery show-all control. Check the full descriptions remain available without JavaScript.
5. Confirm images and section links resolve and project links point to the intended source.
6. If the PDF changed, render and inspect it; verify all production dates and roles, one A4 page, embedded fonts, and working project/contact links. Check all three website download links use the new PDF fingerprint and size.
7. Review the final local preview. For documentation-only changes, validate the affected records and links; repeat interaction checks when behavior changes.

## Deployment

Repository: https://github.com/jeanpierreboutros-lang/jeanpierreboutros.com.git. Published branch: `main`. HostGator's cPanel checkout is `/home2/studiojp/repositories/jeanpierreboutros.com`.

Portfolio release `24ec55eef9540cb49fab5f49328399e631a13c05` was deployed through HostGator on 3 November 2026 at 00:00:01 (Asia/Beirut). cPanel’s Last Deployed SHA matched. All 39 canonical pages and 152 referenced resources matched local bytes; redirects, the real 404 and unpublished source/research paths passed checks. See [the verification record](docs/portfolio-release-verification-2026-11-03.json).

Documentation-only commits can follow the deployed content commit without changing the website. They do not require a cPanel deployment because these documents are excluded from the runtime manifest. The steps below apply to future website releases.

1. Push reviewed changes to `main` on GitHub.
2. In cPanel Git Version Control, choose the existing repository and update from remote. Confirm the HEAD SHA equals the pushed commit.
3. Deploy HEAD and wait for completion. Confirm Last Deployed SHA equals the intended release.
4. Hard-refresh https://www.jeanpierreboutros.com/ and https://jeanpierreboutros.com/. Check all sitemap URLs, affected projects, service pages, updated images and all three profile download links. Verify HTTP/apex/index.html redirects to the HTTPS www canonical, a real 404, search crawler access and GPTBot exclusion. Compare downloaded PDF bytes with the committed artifact when the profile changes.

The deploy manifest targets `/home2/studiojp/public_html/`, confirmed in cPanel's Domains screen for jeanpierreboutros.com. It copies the 39 static pages, fonts, CSS, JavaScript, robots, sitemap, the supplementary llms.txt directory, icons, profile PDF and complete photos directory. Assets and new pages are copied before the homepage and discovery files. Build scripts, the SEO report, this README and Git metadata are not published. Local edits and previews do not deploy the website.

The document root is shared with the existing main hosting site. Deployment copies files without purging other content or changing domain mappings. The redirect installer prepends only the clearly marked JPB block, preserves existing non-JPB .htaccess rules, rejects malformed managed blocks and symlinked .htaccess files, and stores backups in the repository’s non-public `.deployment-backups/`. Every redirect is conditional on jeanpierreboutros.com or www.jeanpierreboutros.com, so the other domain is unaffected. Inspect live behaviour after deployment; local Apache/TLS tests cover canonical redirects and preservation of existing access restrictions.

### Rollback

If a release introduces a broken page, incorrect credit or inaccessible download, revert its commit on `main` with `git revert RELEASE_COMMIT_SHA`, review the resulting runtime files, and push the revert. Update from remote and deploy that new HEAD in cPanel. Verify Last Deployed SHA and the restored live page/PDF. Keep unrelated shared hosting files untouched. Reverting code alone does not remove the managed .htaccess block: restore the appropriate private `.deployment-backups/htaccess-before-jpb.*` backup in cPanel if redirect rules need rollback. Preserve the current non-JPB rules if they changed after that backup. Newly added static pages remain on the non-purging host until explicitly removed; remove only this release’s generated service/project pages if a full rollback is required, or retain their valid content while restoring the homepage.
