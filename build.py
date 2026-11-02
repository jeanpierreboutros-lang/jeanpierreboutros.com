#!/usr/bin/env python3
"""Render the portfolio from confirmed credits and local image metadata."""
import html
import json
import re
from datetime import date
from hashlib import sha256
from pathlib import Path

from search_pages import DESCRIPTION, faq_html, graph, page_head, render_search_pages, site_links
from services import AVAILABILITY, HOME_FAQ, SERVICES

OUT = Path(__file__).resolve().parent
e = html.escape
image_manifest = json.loads((OUT / "photos/optimized/manifest.json").read_text())
asset_versions = {name: sha256((OUT / name).read_bytes()).hexdigest()[:12]
                  for name in ("styles.css", "main.js")}
profile_path = "output/pdf/jean-pierre-boutros-profile.pdf"
profile_bytes = (OUT / profile_path).read_bytes()
profile_url = f"{profile_path}?v={sha256(profile_bytes).hexdigest()[:12]}"
profile_size = f"{len(profile_bytes) / 1024:.0f} KB"

# Keep existing collaborations. Only state specific roles supported by the bio.
artists = [
    "Nancy Ajram", "Marcel Khalifé", "Georges Wassouf", "Carole Samaha",
    "Abeer Nehme", "Maya Diab", "Adam", "Al Shami", "Melhem Zein",
    "Ramy Ayyach", "Zade Dirani", "Joseph Attiye", "Georges Nehme",
    "Salim Assaf", "Mazeej", "Cartoon Orchestra", "Macadi Nahhas",
    "Tania Saleh", "Remi Bandali", "Rasha Rizk", "Yara", "Leen Hayek",
    "Salah El Kurdi", "Charbel Rouhana", "Chantal Bitar", "Carlos Azar",
    "Ziad Bourji", "Sarina Cross", "Ziad Jamal", "Mouhamad Khairy",
    "Manel Mallat", "Faraj Hanna", "Mike Massy", "Ria Ellinidou", "Marina Viotti",
    "Lebanese National Philharmonic Orchestra",
]

# Captions describe visible content, without guessing venues or artists.
gallery = [
    ("the-eighties-knockout-kuwait-2026.jpg", "The Eighties… The Knockout", "Signed production artwork above a cast photograph for The Eighties… The Knockout in Kuwait", "FOH engineer · Kuwait, 2026"),
    ("marina-viotti-zouk-mikael-2026.jpg", "Marina Viotti · Opera gala", "Front-of-house mixing console facing the illuminated stage at the Beirut International Opera Festival gala in Zouk Mikael", "FOH engineer · Zouk Mikael, 2026"),
    ("cartoon-orchestra-kuwait-2025.jpg", "Cartoon Orchestra", "Cartoon Orchestra production poster displayed at Sheikh Jaber Al-Ahmad Cultural Centre in Kuwait", "FOH engineer · Kuwait, 2025"),
    ("al-sharq-symphony-istanbul-2017.jpg", "Al Sharq Symphony", "Orchestra and choir performing Al Sharq Symphony in Istanbul, from Al Sharq Youth’s official concert video", "FOH engineer · Istanbul, 2017"),
    ("abeer-nehme-qatar-philharmonic-2026.jpg", "Abeer Nehme · Qatar Philharmonic", "Abeer Nehme singing on stage with the Qatar Philharmonic Orchestra at U VENUE in Doha, 23 January 2026", "FOH engineer · U VENUE, Doha, 2026"),
    ("nancy-ajram-baligh-hamdi-riyadh-2023.jpg", "Nancy Ajram · Baligh Hamdi Night", "Nancy Ajram performing with orchestral musicians at Baligh Hamdi Night in Riyadh, 9 November 2023", "Nancy Ajram’s monitor engineer · Riyadh, 2023"),
    ("nancy-ajram-warda-night-jeddah-2024.jpg", "Nancy Ajram · Warda Night", "Nancy Ajram on stage with orchestral musicians at Warda Night in Jeddah, 4 July 2024", "Nancy Ajram’s monitor engineer · Jeddah, 2024"),
    ("nancy-ajram-arab-stars-riyadh-2023.jpg", "Nancy Ajram · Night of Arab Stars", "Nancy Ajram singing with dancers and musicians at Night of Arab Stars in Riyadh, 31 December 2023", "Nancy Ajram’s monitor engineer · Riyadh Season, 2023"),
    ("lebanese-philharmonic-diman-2026.jpg", "Lebanese Philharmonic · Diman", "Lebanese National Philharmonic Orchestra performing beneath an illuminated cross at the Patriarchal Summer Residence in Diman, conducted by Harout Fazlian", "FOH engineer · Diman, 26 July 2026"),
    ("nancy-ajram-olympia-paris-2022.jpg", "Nancy Ajram · L’Olympia", "Nancy Ajram singing in a red gown with her band at L’Olympia in Paris, 10 June 2022", "FOH engineer · Paris, 2022"),
    ("marcel-khalife-muscat-2019.jpg", "Marcel Khalifé · Muscat", "Marcel Khalifé singing and playing the oud during his September 2019 concerts at the Royal Opera House of Musical Arts in Muscat", "FOH engineer · Muscat, Oman, 2019"),
    ("nancy-ajram-expo-dubai-2021.jpg", "Nancy Ajram · Expo 2020 Dubai", "Nancy Ajram singing with her band beneath the Al Wasl Plaza dome during Infinite Nights at Expo 2020 Dubai, 12 November 2021", "Nancy Ajram’s monitor engineer · Dubai, 2021"),
    ("abeer-nehme-ehdeniyat-2025.jpg", "Abeer Nehme · Ehdeniyat 2025", "Abeer Nehme singing with musicians and a dancer at Ehdeniyat International Festival, 25 July 2025", "FOH engineer · Ehden, Lebanon, 2025"),
    ("al-shami-ehdeniyat-2025.jpg", "Al Shami · Ehdeniyat 2025", "Al Shami performing amid stage effects and LED screens at Ehdeniyat International Festival, 3 August 2025", "FOH engineer · Ehden, Lebanon, 2025"),
    ("adam-ehdeniyat-2025.jpg", "Adam · Ehdeniyat 2025", "Adam singing with musicians behind him at Ehdeniyat International Festival, 31 July 2025", "Monitor engineer for Adam · Ehden, Lebanon, 2025"),
    ("live-outdoor-foh-night.jpg", "At the desk", "Jean-Pierre Boutros mixing an outdoor concert at night", "Live sound"),
    ("foh-pov-theater-stage.jpg", "A view from front of house", "Mixing console facing an illuminated theatre stage", "Live sound"),
    ("concert-arena-led-screens.jpg", "Sound at scale", "Concert stage with large LED screens, seen from the audience", "Live production"),
    ("studio-manley-outboard.jpg", "The studio details", "Hands adjusting Manley outboard audio equipment", "Studio"),
    ("foh-church-concert-organ.jpg", "Every room has a voice", "Front-of-house console during a concert in a church", "Live sound"),
    ("pope-leo-waterfront.jpg", "Papal visit, 2025", "Stage prepared for Pope Leo XIV’s 2025 visit to Lebanon", "Lebanon"),
    ("foh-orchestra-ornate-backdrop.jpg", "An orchestral perspective", "Mixing console overlooking orchestral musicians on stage", "Live sound"),
    ("midas-heritage-console.jpg", "Behind the mix", "Midas Heritage mixing console and production screens", "Live production"),
    ("foh-concert-hall-aerial.jpg", "From the back of the room", "Concert hall and stage viewed from above the front-of-house position", "Live sound"),
]
tv = [
    ("MTV Lebanon", "Hek Menghanni", "Music television"),
    ("Abu Dhabi TV", "Ghanni Al Aali", "Music television"),
    ("Al Mayadeen TV", "Ethnophilia", "Music documentary series"),
]
zyn = [
    ("zynforge-live.png", "Zynforge Live", "Live performance", "A plugin host for taking audio processing onto the stage."),
    ("zynforge-recording.png", "Zynforge Recording", "Recording & playback", "Multitrack recording and playback for live performance."),
    ("zynforge-stage.png", "Zynforge Stage", "Production planning", "Stage plots and technical riders for planning a production."),
]
navigation = [("work", "Selected work"), ("credits", "Credits"), ("about", "About"),
              ("zynforge", "Zynforge"), ("gallery", "Gallery"), ("contact", "Contact")]

baligh_coverage_url = "https://www.sayidaty.net/مشاهير/مشاهير-العرب/1692211-بالصور-7-فنانين-و185-عازفاً-بموسم-الرياض-ما-الأغاني-التي-اختاروها-في"
warda_coverage_url = "https://aawsat.com/يوميات-الشرق/5037424-ليلة-وردة-سهرة-باذخة-الجمال-لعشاق-الطرب-على-مسرح-أرينا"
arab_stars_coverage_url = "https://www.sayidaty.net/مشاهير/مشاهير-العرب/1711121-بالفيديو-والصور-تفاصيل-حفلة-ليلة-نجمات-العرب-في-الرياض"
arab_stars_photo_url = "https://www.aljamila.com/node/791121/بسعر-خيالي-نانسي-عجرم-تألقت-بفستان-أسود-شفاف-في-ليلة-نجمات-العرب%C2%A0"
diman_coverage_url = "https://bkerki.org/news-article/امسية-موسيقية-بعنوان-عهد-أبدي/"
olympia_coverage_url = "https://www.parisbouge.com/events/234789"
olympia_photo_url = "https://www.filfan.com/news/147643"
muscat_programme_url = "https://rohmuscat.org.om/en/performance/performance-detail?i=404"
muscat_photo_url = "https://www.omanobserver.om/article/23830/Main/marcel-khalife-created-his-own-global-sound-world"
expo_coverage_url = "https://virtualexpodubai.com/listen-watch/events/infinite-nights-starring-ragheb-alama-and-nancy-ajram"
ehdeniyat_programme_url = "https://lebanonuntravelled.com/ehdeniyat-international-festival-2025/"
abeer_ehdeniyat_coverage_url = "https://today.lorientlejour.com/article/1471284/at-ehdeniyat-abeer-nehme-reaches-saltana.html"
shami_ehdeniyat_coverage_url = "https://www.cairo24.com/2256107"
adam_ehdeniyat_coverage_url = "https://aghaniaghani.com/news/regional-celebrities/آدم-يُشعل-مسرح-إهدنيات-الدولي-بلحظات-إ/"
adam_ehdeniyat_gallery_url = "https://www.beiruting.com/events/43820/adam-at-ehdeniyat-festival"

gallery_sources = {
    "abeer-nehme-ehdeniyat-2025.jpg": {
        "name": "Ehdeniyat Festival / L’Orient-Le Jour",
        "url": abeer_ehdeniyat_coverage_url,
        "image_url": "https://s.lorientlejour.com/storage/attachments/1472/PIE_9590_836549.jpg/r/2400/PIE_9590_836549.jpg",
    },
    "al-shami-ehdeniyat-2025.jpg": {
        "name": "Cairo24",
        "url": shami_ehdeniyat_coverage_url,
        "image_url": "https://www.cairo24.com/Upload/libfiles/163/0/191.jpg",
    },
    "adam-ehdeniyat-2025.jpg": {
        "name": "Beiruting",
        "url": adam_ehdeniyat_gallery_url,
        "image_url": "https://api.beiruting.com/images/1210x807xi/527531944_1336761888016831_8705915139313954408_n.webp",
    },
    "nancy-ajram-expo-dubai-2021.jpg": {
        "name": "Expo 2020 Dubai / Virtual Expo",
        "url": expo_coverage_url,
        "image_url": "https://images.ctfassets.net/opz1rk40r4ou/1Z8NDz0CUIBH8xHsnKBvCu/e7dab9c5f3fa9c5b5cc9fd1912a19dbd/Expo_Nights_Nancy_54.jpg?fm=jpg&q=90&w=1600",
    },
    "nancy-ajram-olympia-paris-2022.jpg": {
        "name": "FilFan",
        "url": olympia_photo_url,
        "image_url": "https://media.filfan.com/NewsPics/FilfanNew/large/389566_0.PNG",
    },
    "marcel-khalife-muscat-2019.jpg": {
        "name": "Oman Observer",
        "url": muscat_photo_url,
        "image_url": "https://www.omanobserver.om/uploads/imported_images/uploads/2019/09/IMG_4593.jpg",
    },
    "nancy-ajram-arab-stars-riyadh-2023.jpg": {
        "name": "Rotana Live / Al Jamila",
        "url": arab_stars_photo_url,
        "image_url": "https://static.aljamila.com/styles/1100x732_scale/public/2024-01/نانسي%20عجرم%20-%20الصورة%20من%20الحساب%20الرسمي%20لحفلات%20روتانا%20على%20إنستجرام_0.jpg",
    },
    "nancy-ajram-baligh-hamdi-riyadh-2023.jpg": {
        "name": "Benchmark / Sayidaty",
        "url": baligh_coverage_url,
        "image_url": "https://static.sayidaty.net/2023-11/298244.jpg",
    },
    "nancy-ajram-warda-night-jeddah-2024.jpg": {
        "name": "Asharq Al-Awsat",
        "url": warda_coverage_url,
        "image_url": "https://static.srpcdigital.com/2024-07/704233.jpeg",
    },
    "abeer-nehme-qatar-philharmonic-2026.jpg": {
        "name": "U Events / U VENUE",
        "url": "https://uevents.me/en/events/abeer-nehme-with-qatar-philharmonic-orchestra",
        "image_url": "https://uevents.me/storage/372/81dae70b-e952-4a5d-82c4-1eefb0fa1753.jpg",
    },
    "al-sharq-symphony-istanbul-2017.jpg": {
        "name": "Al Sharq Youth",
        "url": "https://www.youtube.com/watch?v=hAZbbyPg7GE",
        "image_url": "https://i.ytimg.com/vi/hAZbbyPg7GE/maxresdefault.jpg",
    },
}


def image(filename, alt, *, css="", sizes="100vw", eager=False):
    """Use responsive assets while keeping the HTML build dependency-free."""
    info = image_manifest[filename]
    variants = info["variants"]
    for variant in variants:
        if not (OUT / variant["src"]).is_file():
            raise FileNotFoundError(f"Run optimize_images.py: {variant['src']}")
    default = next((v for v in variants if v["width"] >= 960), variants[-1])
    srcset = ", ".join(f"{v['src']} {v['width']}w" for v in variants)
    loading = 'fetchpriority="high"' if eager else 'loading="lazy"'
    return (f'<img class="{e(css)}" src="{e(default["src"])}" '
            f'srcset="{e(srcset)}" sizes="{e(sizes)}" alt="{e(alt)}" '
            f'width="{info["width"]}" height="{info["height"]}" '
            f'{loading} decoding="async" />')


def nav_links(css=""):
    return "\n".join(f'<a href="#{key}" class="{css if key == "contact" else ""}">{label}</a>'
                     for key, label in navigation)


artist_projects = {
    "Al Shami": ("ehdeniyat-al-shami", "FOH engineer · Ehdeniyat, 2025"),
    "Adam": ("ehdeniyat-adam", "Monitor engineer · Ehdeniyat, 2025"),
    "Lebanese National Philharmonic Orchestra": ("lebanese-philharmonic-diman", "FOH engineer · Diman, 2026"),
    "Nancy Ajram": ("nancy-ajram-olympia", "FOH & monitor engineer · 2021–24"),
    "Abeer Nehme": ("ehdeniyat-abeer-nehme", "FOH engineer · Qatar & Ehden, 2025–26"),
    "Marcel Khalifé": ("marcel-khalife-muscat", "FOH engineer · Istanbul & Muscat"),
    "Marina Viotti": ("marina-viotti", "FOH engineer · Lebanon, 2026"),
    "Cartoon Orchestra": ("cartoon-orchestra", "FOH engineer · Kuwait, 2025"),
}
artist_html = "\n".join(
    f'<li><a href="#{artist_projects[name][0]}">{e(name)}<span class="credit-role">{e(artist_projects[name][1])}</span></a></li>'
    if name in artist_projects else f'<li>{e(name)}</li>' for name in artists)
tv_html = "\n".join(f'''<li class="broadcast-row">
  <span class="tv-channel">{e(channel)}</span>
  <h4>{e(title)}</h4><span class="broadcast-format">{e(kind)}</span>
</li>''' for channel, title, kind in tv)
zyn_html = "\n".join(f'''<article class="product-card">
  {image(filename, "", css="zyn-icon", sizes="64px")}
  <p class="product-category">{e(category)}</p>
  <h3>{e(title)}</h3><p>{e(description)}</p>
</article>''' for filename, title, category, description in zyn)

gallery_items = []
gallery_data = []
for index, (filename, title, alt, context) in enumerate(gallery):
    full = image_manifest[filename]["variants"][-1]
    source = gallery_sources.get(filename)
    credit_text = f" · Image: {source['name']}" if source else ""
    credit_html = (f'<a class="image-credit" href="{e(source["url"])}" target="_blank" rel="noopener noreferrer">Image: {e(source["name"])}<span class="sr-only"> (opens in a new tab)</span></a>' if source else "")
    gallery_data.append({"src": full["src"], "alt": alt, "caption": f"{title} · {context}{credit_text}",
                         "width": full["width"], "height": full["height"]})
    poster_class = " gallery-card--poster" if filename in ("the-eighties-knockout-kuwait-2026.jpg", "cartoon-orchestra-kuwait-2025.jpg") else ""
    featured_attribute = ' data-gallery-featured' if index in (15, 16, 18, 19, 21, 23) else ''
    gallery_items.append(f'''<figure class="gallery-card{poster_class}"{featured_attribute}>
  <a class="gallery-item" href="{e(full["src"])}" data-gallery-index="{index}"
     aria-label="Enlarge photo: {e(alt)}" aria-haspopup="dialog" aria-controls="lightbox">
    {image(filename, alt, sizes="(max-width: 600px) 100vw, (max-width: 980px) 50vw, 33vw")}
    <span class="gallery-expand" aria-hidden="true">↗</span>
  </a>
  <figcaption><span>{e(title)}</span><span>{e(context)}{credit_html}</span></figcaption>
</figure>''')

# Lead with the working side of the performance; retain every photograph in the viewer.
gallery_items.sort(key=lambda item: 'data-gallery-featured' not in item)


PROJECT_DETAILS = f'''
        <!-- Event context: JACC's official listing, event 599. FOH role confirmed by Jean-Pierre. -->
        <article class="project-feature project-feature--kuwait" id="the-eighties" aria-labelledby="eighties-title" data-reveal>
          <figure class="project-poster">
            <a href="{e(gallery_data[0]['src'])}" data-gallery-index="0" aria-label="Enlarge the signed artwork and cast photograph for The Eighties… The Knockout" aria-haspopup="dialog" aria-controls="lightbox">
              {image("the-eighties-knockout-kuwait-2026.jpg", "Signed production artwork and cast photograph for The Eighties… The Knockout in Kuwait", sizes="(max-width: 760px) 100vw, 50vw")}
            </a>
            <figcaption>Signed production artwork &amp; cast photograph · Kuwait, 2026</figcaption>
          </figure>
          <div class="project-copy">
            <p class="project-index">01 <span>Front-of-house engineering</span></p>
            <h3 id="eighties-title">The Eighties…<br /><em>The Knockout.</em></h3>
            <p class="project-title-ar" lang="ar" dir="rtl">الثمانينات.. الضربة القاضية</p>
            <p>Front-of-house engineering for the 2026 return of this live musical production at the National Theatre, Sheikh Jaber Al-Ahmad Cultural Centre, Kuwait.</p>
            <p>A journey through the music and television memories of the 1980s, presented as part of the centre’s tenth-anniversary celebrations.</p>
            <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Venue</dt><dd>National Theatre · JACC</dd></div><div><dt>Location &amp; date</dt><dd>Kuwait · October 2026</dd></div></dl>
            <p class="production-credit">Direction · Jassim Al-Qames<br />Musical direction · Dr Khaled Noori</p>
            <a class="text-link" href="https://tickets.jacc-kw.com/event/info/the-eighties--the-knockout/599" target="_blank" rel="noopener noreferrer">Explore the production <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
            <p class="source-note">Production details · Official JACC listing</p>
          </div>
        </article>
        <div class="event-grid" data-reveal-group>
          <!-- Gala date, venue and programme: BIOFC's official first-edition page. FOH role confirmed by Jean-Pierre. -->
          <article class="project-event" id="marina-viotti" aria-labelledby="marina-title" data-reveal>
            <a class="event-media" href="{e(gallery_data[1]['src'])}" data-gallery-index="1" aria-label="Enlarge the front-of-house photograph from the Marina Viotti opera gala" aria-haspopup="dialog" aria-controls="lightbox">
              {image("marina-viotti-zouk-mikael-2026.jpg", "Front-of-house console overlooking the opera gala at Zouk Mikael’s Roman Amphitheatre", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">02 <span>Front-of-house engineering · Opera</span></p>
              <h3 id="marina-title">Marina Viotti.<br /><em>Opera under the stars.</em></h3>
              <p>FOH engineering for the inaugural gala of the Beirut International Opera Festival &amp; Competition, headlined by mezzo-soprano Marina Viotti at Zouk Mikael’s Roman Amphitheatre.</p>
              <p>The open-air programme brought together Les Solistes de Beyrouth and a symphony orchestra under conductor Fernando Afara.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Venue</dt><dd>Roman Amphitheatre, Zouk Mikael</dd></div><div><dt>Date</dt><dd>8 September 2026 · Lebanon</dd></div></dl>
              <a class="text-link" href="https://beirutoperafestival.com/the-festival/first-edition-2026/" target="_blank" rel="noopener noreferrer">Explore the inaugural gala <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Programme details · Beirut International Opera Festival &amp; Competition</p>
            </div>
          </article>
          <!-- Programme and date: JACC's official 2025–26 season calendar, page 7. -->
          <article class="project-event" id="cartoon-orchestra" aria-labelledby="cartoon-title" data-reveal>
            <a class="event-media event-media--poster" href="{e(gallery_data[2]['src'])}" data-gallery-index="2" aria-label="Enlarge the Cartoon Orchestra production poster from Kuwait" aria-haspopup="dialog" aria-controls="lightbox">
              {image("cartoon-orchestra-kuwait-2025.jpg", "Cartoon Orchestra poster at JACC, showing the concert date of 4 October 2025", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">03 <span>Front-of-house engineering · Orchestra</span></p>
              <h3 id="cartoon-title">Cartoon Orchestra.<br /><em>Memories, live.</em></h3>
              <p class="project-title-ar" lang="ar" dir="rtl">أوركسترا الكرتون</p>
              <p>FOH engineering for Cartoon Orchestra at the National Theatre, Sheikh Jaber Al-Ahmad Cultural Centre, Kuwait.</p>
              <p>Led by Dr Khaled Noori, the production revisited the themes and scores of Arabic and international animated series, combining live orchestral music with visual storytelling.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Venue</dt><dd>National Theatre · JACC</dd></div><div><dt>Date</dt><dd>4 October 2025 · Kuwait</dd></div></dl>
              <a class="text-link" href="https://jacc-kw.com/survey/calen/JACC_Season_Calendar_25-26.pdf#page=7" target="_blank" rel="noopener noreferrer">View the official programme <span aria-hidden="true">↗</span><span class="sr-only"> (PDF opens in a new tab)</span></a>
              <p class="source-note">Production details · JACC 2025–26 season calendar</p>
            </div>
          </article>
          <!-- Official Al Sharq Youth coverage identifies this as the 2017 Istanbul concert, not the later upload date. -->
          <article class="project-event" id="al-sharq-symphony" aria-labelledby="al-sharq-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[3]['src'])}" data-gallery-index="3" aria-label="Enlarge the Al Sharq Symphony concert image, credited to Al Sharq Youth" aria-haspopup="dialog" aria-controls="lightbox">
              {image("al-sharq-symphony-istanbul-2017.jpg", "Orchestra and choir on stage at Al Sharq Symphony, Istanbul, 2017 — image from Al Sharq Youth’s official concert video", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">04 <span>Front-of-house engineering · Symphony</span></p>
              <h3 id="al-sharq-title">Al Sharq<br /><em>Symphony.</em></h3>
              <p>FOH engineering for Marcel Khalifé and the Istanbul Philharmonic Orchestra, conducted by Lubnan Baalbaki.</p>
              <p>The concert was presented as part of the Al Sharq Youth Annual Conference in Istanbul in 2017.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Conductor</dt><dd>Lubnan Baalbaki</dd></div><div><dt>Location &amp; year</dt><dd>Istanbul, Turkey · 2017</dd></div></dl>
              <a class="text-link" href="https://www.youtube.com/watch?v=hAZbbyPg7GE" target="_blank" rel="noopener noreferrer">Watch the concert <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Image &amp; official concert coverage: <a href="https://youth.sharqforum.org/asy-gallery/al-sharq-symphony-marcel-khalife-and-istanbul-philharmonic-orchestra-conducted-by-lubnan-baalbaki/" target="_blank" rel="noopener noreferrer">Al Sharq Youth<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
          <!-- Date, venue and repertoire: Qatar Philharmonic Orchestra. FOH role confirmed by Jean-Pierre. -->
          <article class="project-event" id="abeer-nehme-qatar" aria-labelledby="abeer-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[4]['src'])}" data-gallery-index="4" aria-label="Enlarge Abeer Nehme performing with the Qatar Philharmonic Orchestra in Doha" aria-haspopup="dialog" aria-controls="lightbox">
              {image("abeer-nehme-qatar-philharmonic-2026.jpg", "Abeer Nehme performing with the Qatar Philharmonic Orchestra at U VENUE, Doha, 23 January 2026 — photo by U Events / U VENUE", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">05 <span>Front-of-house engineering · Orchestra</span></p>
              <h3 id="abeer-title">Abeer Nehme.<br /><em>With Qatar Philharmonic.</em></h3>
              <p>FOH engineering for Abeer Nehme with the Qatar Philharmonic Orchestra at U VENUE in Doha, Qatar.</p>
              <p>Presented by U Events, the concert brought her original songs and familiar favourites to the stage with live orchestral accompaniment.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Venue</dt><dd>U VENUE · Doha, Qatar</dd></div><div><dt>Date</dt><dd>23 January 2026</dd></div></dl>
              <a class="text-link" href="https://qatarphilharmonicorchestra.org/concert/abeer-nehme-with-qatar-philharmonic-orchestra/" target="_blank" rel="noopener noreferrer">Explore the concert <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Concert photo: <a href="https://uevents.me/en/events/abeer-nehme-with-qatar-philharmonic-orchestra" target="_blank" rel="noopener noreferrer">U Events / U VENUE<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
          <!-- Monitor role is specifically for Nancy Ajram; it is not a credit for the whole production. -->
          <article class="project-event" id="baligh-hamdi-night" aria-labelledby="baligh-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[5]['src'])}" data-gallery-index="5" aria-label="Enlarge Nancy Ajram performing with the orchestra at Baligh Hamdi Night in Riyadh" aria-haspopup="dialog" aria-controls="lightbox">
              {image("nancy-ajram-baligh-hamdi-riyadh-2023.jpg", "Nancy Ajram and orchestral musicians at Baligh Hamdi Night, Riyadh, 9 November 2023 — photo by Benchmark, via Sayidaty", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">06 <span>Monitor engineering · Nancy Ajram</span></p>
              <h3 id="baligh-title">Nancy Ajram.<br /><em>Baligh Hamdi Night.</em></h3>
              <p class="project-title-ar" lang="ar" dir="rtl">روائع بليغ حمدي</p>
              <p>Monitor engineering for Nancy Ajram’s performance at Masterpieces of Baligh Hamdi, held at Abu Bakr Salem Theatre in Riyadh.</p>
              <p>Presented during Riyadh Season 2023, the concert celebrated the Egyptian composer’s repertoire with live orchestral performances.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>Monitor engineer for Nancy Ajram</dd></div><div><dt>Venue</dt><dd>Abu Bakr Salem Theatre · Riyadh, Saudi Arabia</dd></div><div><dt>Date</dt><dd>9 November 2023</dd></div></dl>
              <a class="text-link" href="https://www.harpersbazaararabia.com/culture/entertainment/baligh-hamdi-tribute" target="_blank" rel="noopener noreferrer">Explore the tribute <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Concert photo: <a href="{e(baligh_coverage_url)}" target="_blank" rel="noopener noreferrer">Benchmark, via Sayidaty<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
          <!-- User confirmed this is the 4 July 2024 Jeddah show; date and venue match GEA's Enjoy listing. -->
          <article class="project-event" id="warda-night" aria-labelledby="warda-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[6]['src'])}" data-gallery-index="6" aria-label="Enlarge Nancy Ajram performing with the orchestra at Warda Night in Jeddah" aria-haspopup="dialog" aria-controls="lightbox">
              {image("nancy-ajram-warda-night-jeddah-2024.jpg", "Nancy Ajram performing with orchestral musicians at Warda Night, Jeddah, 4 July 2024 — photo from Asharq Al-Awsat", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">07 <span>Monitor engineering · Nancy Ajram</span></p>
              <h3 id="warda-title">Nancy Ajram.<br /><em>Warda Night.</em></h3>
              <p class="project-title-ar" lang="ar" dir="rtl">ليلة وردة</p>
              <p>Monitor engineering for Nancy Ajram’s performance at Warda Night, the inaugural concert at Abadi Al Johar Arena in Jeddah.</p>
              <p>The Jeddah Season 2024 tribute honoured Warda Al-Jazairia, with an orchestra conducted by Walid Fayed and performances by four Arab vocalists.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>Monitor engineer for Nancy Ajram</dd></div><div><dt>Venue</dt><dd>Abadi Al Johar Arena · Jeddah, Saudi Arabia</dd></div><div><dt>Date</dt><dd>4 July 2024</dd></div></dl>
              <a class="text-link" href="https://enjoy.sa/en/events/warda-night/" target="_blank" rel="noopener noreferrer">View the official event listing <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Concert photo: <a href="{e(warda_coverage_url)}" target="_blank" rel="noopener noreferrer">Asharq Al-Awsat<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
          <article class="project-event" id="night-of-arab-stars" aria-labelledby="arab-stars-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[7]['src'])}" data-gallery-index="7" aria-label="Enlarge Nancy Ajram performing at Night of Arab Stars in Riyadh" aria-haspopup="dialog" aria-controls="lightbox">
              {image("nancy-ajram-arab-stars-riyadh-2023.jpg", "Nancy Ajram performing with dancers and musicians at Night of Arab Stars, Riyadh, 31 December 2023 — photo by Rotana Live, via Al Jamila", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">08 <span>Monitor engineering · Nancy Ajram</span></p>
              <h3 id="arab-stars-title">Nancy Ajram.<br /><em>Night of Arab Stars.</em></h3>
              <p class="project-title-ar" lang="ar" dir="rtl">ليلة نجمات العرب</p>
              <p>Monitor engineering for Nancy Ajram’s performance at Night of Arab Stars, the Riyadh Season concert welcoming 2024 at Mohammed Abdu Arena.</p>
              <p>Presented by Rotana, the New Year’s Eve programme brought together six Arab vocalists for solo performances and duets, with musical direction by Hany Farhat.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>Monitor engineer for Nancy Ajram</dd></div><div><dt>Venue</dt><dd>Mohammed Abdu Arena · Riyadh, Saudi Arabia</dd></div><div><dt>Date</dt><dd>31 December 2023</dd></div></dl>
              <a class="text-link" href="{e(arab_stars_coverage_url)}" target="_blank" rel="noopener noreferrer">Explore the concert <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Concert photo: <a href="{e(arab_stars_photo_url)}" target="_blank" rel="noopener noreferrer">Rotana Live, via Al Jamila<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
          <article class="project-event" id="lebanese-philharmonic-diman" aria-labelledby="diman-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[8]['src'])}" data-gallery-index="8" aria-label="Enlarge the Lebanese National Philharmonic Orchestra performing in Diman" aria-haspopup="dialog" aria-controls="lightbox">
              {image("lebanese-philharmonic-diman-2026.jpg", "Lebanese National Philharmonic Orchestra conducted by Harout Fazlian at the Patriarchal Summer Residence, Diman, 26 July 2026", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">09 <span>Front-of-house engineering · Orchestra</span></p>
              <h3 id="diman-title">Lebanese Philharmonic.<br /><em>An evening in Diman.</em></h3>
              <p class="project-title-ar" lang="ar" dir="rtl">العهد الأبدي</p>
              <p>FOH engineering for the Lebanese National Philharmonic Orchestra, conducted by Harout Fazlian, at the Patriarchal Summer Residence in Diman, North Lebanon.</p>
              <p>The open-air concert, titled “Eternal Covenant”, formed part of the celebrations for the beatification of Patriarch Elias Hoayek.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Conductor</dt><dd>Harout Fazlian</dd></div><div><dt>Location &amp; date</dt><dd>Diman, North Lebanon · 26 July 2026</dd></div></dl>
              <a class="text-link" href="{e(diman_coverage_url)}" target="_blank" rel="noopener noreferrer">Read the concert coverage <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Concert details · Maronite Patriarchate</p>
            </div>
          </article>
          <article class="project-event" id="nancy-ajram-olympia" aria-labelledby="olympia-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[9]['src'])}" data-gallery-index="9" aria-label="Enlarge Nancy Ajram performing at L’Olympia in Paris" aria-haspopup="dialog" aria-controls="lightbox">
              {image("nancy-ajram-olympia-paris-2022.jpg", "Nancy Ajram performing with her band at L’Olympia, Paris, 10 June 2022 — photo via FilFan", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">10 <span>Front-of-house engineering · Nancy Ajram</span></p>
              <h3 id="olympia-title">Nancy Ajram.<br /><em>L’Olympia, Paris.</em></h3>
              <p>FOH engineering for Nancy Ajram’s concert at L’Olympia in Paris on 10 June 2022.</p>
              <p>Her return to the Paris stage followed the release of Nancy 10, with a programme drawn from her repertoire and live band accompaniment.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Venue</dt><dd>L’Olympia · Paris, France</dd></div><div><dt>Date</dt><dd>10 June 2022</dd></div></dl>
              <a class="text-link" href="https://www.youtube.com/watch?v=4l2mWDhjhtk" target="_blank" rel="noopener noreferrer">Watch the official concert recap <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Concert photo: <a href="{e(olympia_photo_url)}" target="_blank" rel="noopener noreferrer">FilFan<span class="sr-only"> (opens in a new tab)</span></a> · <a href="{e(olympia_coverage_url)}" target="_blank" rel="noopener noreferrer">Event listing<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
          <article class="project-event" id="marcel-khalife-muscat" aria-labelledby="muscat-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[10]['src'])}" data-gallery-index="10" aria-label="Enlarge Marcel Khalifé performing in Muscat in 2019" aria-haspopup="dialog" aria-controls="lightbox">
              {image("marcel-khalife-muscat-2019.jpg", "Marcel Khalifé singing and playing oud in Muscat, September 2019 — photo from Oman Observer", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">11 <span>Front-of-house engineering · Marcel Khalifé</span></p>
              <h3 id="muscat-title">Marcel Khalifé.<br /><em>Royal Opera House Muscat.</em></h3>
              <p>FOH engineering for Marcel Khalifé at the House of Musical Arts, part of the Royal Opera House Muscat, Oman.</p>
              <p>Presented on 26–27 September 2019, the concerts brought together his voice and oud with live accompaniment, including pianist Rami Khalifé.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Venue</dt><dd>House of Musical Arts · Royal Opera House Muscat</dd></div><div><dt>Location &amp; dates</dt><dd>Muscat, Oman · 26–27 September 2019</dd></div></dl>
              <a class="text-link" href="{e(muscat_programme_url)}" target="_blank" rel="noopener noreferrer">View the official programme <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Concert photo &amp; review: <a href="{e(muscat_photo_url)}" target="_blank" rel="noopener noreferrer">Oman Observer<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
          <article class="project-event" id="ehdeniyat-abeer-nehme" aria-labelledby="ehdeniyat-abeer-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[12]['src'])}" data-gallery-index="12" aria-label="Enlarge Abeer Nehme performing at Ehdeniyat 2025" aria-haspopup="dialog" aria-controls="lightbox">
              {image("abeer-nehme-ehdeniyat-2025.jpg", "Abeer Nehme with musicians and a dancer at Ehdeniyat, 25 July 2025 — photo courtesy Ehdeniyat Festival, via L’Orient-Le Jour", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">12 <span>Front-of-house engineering · Festival</span></p>
              <h3 id="ehdeniyat-abeer-title">Abeer Nehme.<br /><em>Ehdeniyat 2025.</em></h3>
              <p>FOH engineering for Abeer Nehme’s concert at Ehdeniyat International Festival in Ehden, North Lebanon, on 25 July 2025.</p>
              <p>Her open-air performance brought together her own songs and a multilingual repertoire, accompanied by musicians and a choir under Marc Abou Naoum.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Festival</dt><dd>Ehdeniyat International Festival · Ehden, Lebanon</dd></div><div><dt>Date</dt><dd>25 July 2025</dd></div></dl>
              <a class="text-link" href="{e(abeer_ehdeniyat_coverage_url)}" target="_blank" rel="noopener noreferrer">Read the concert review <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Photo: <a href="{e(abeer_ehdeniyat_coverage_url)}" target="_blank" rel="noopener noreferrer">Ehdeniyat Festival, via L’Orient-Le Jour<span class="sr-only"> (opens in a new tab)</span></a> · <a href="{e(ehdeniyat_programme_url)}" target="_blank" rel="noopener noreferrer">Festival programme<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
          <article class="project-event" id="ehdeniyat-al-shami" aria-labelledby="ehdeniyat-shami-title" data-reveal>
            <a class="event-media event-media--concert" href="{e(gallery_data[13]['src'])}" data-gallery-index="13" aria-label="Enlarge Al Shami performing at Ehdeniyat 2025" aria-haspopup="dialog" aria-controls="lightbox">
              {image("al-shami-ehdeniyat-2025.jpg", "Al Shami performing with stage effects at Ehdeniyat, 3 August 2025 — photo via Cairo24", sizes="(max-width: 760px) 100vw, 50vw")}
              <span class="gallery-expand" aria-hidden="true">↗</span>
            </a>
            <div class="project-copy">
              <p class="project-index">13 <span>Front-of-house engineering · Festival</span></p>
              <h3 id="ehdeniyat-shami-title">Al Shami.<br /><em>Ehdeniyat 2025.</em></h3>
              <p>FOH engineering for Al Shami’s concert at Ehdeniyat International Festival on 3 August 2025, the closing night of the festival’s 21st edition.</p>
              <p>The outdoor production combined his songs with dancers, LED visuals and stage effects in the mountain setting of Ehden, North Lebanon.</p>
              <dl class="project-details"><div><dt>My role</dt><dd>FOH engineer</dd></div><div><dt>Festival</dt><dd>Ehdeniyat International Festival · Ehden, Lebanon</dd></div><div><dt>Date</dt><dd>3 August 2025</dd></div></dl>
              <a class="text-link" href="{e(shami_ehdeniyat_coverage_url)}" target="_blank" rel="noopener noreferrer">Explore the concert coverage <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
              <p class="source-note">Photo: <a href="{e(shami_ehdeniyat_coverage_url)}" target="_blank" rel="noopener noreferrer">Cairo24<span class="sr-only"> (opens in a new tab)</span></a> · <a href="{e(ehdeniyat_programme_url)}" target="_blank" rel="noopener noreferrer">Festival programme<span class="sr-only"> (opens in a new tab)</span></a></p>
            </div>
          </article>
        </div>
        <article class="project-feature project-feature--concert" id="nancy-ajram-expo-dubai" aria-labelledby="expo-title" data-reveal>
          <figure class="project-poster">
            <a href="{e(gallery_data[11]['src'])}" data-gallery-index="11" aria-label="Enlarge Nancy Ajram performing at Expo 2020 Dubai" aria-haspopup="dialog" aria-controls="lightbox">
              {image("nancy-ajram-expo-dubai-2021.jpg", "Nancy Ajram performing with her band at Al Wasl Plaza, Expo 2020 Dubai, 12 November 2021 — photo from Expo 2020 Dubai / Virtual Expo", sizes="(max-width: 760px) 100vw, 50vw")}
            </a>
            <figcaption>Infinite Nights · Al Wasl Plaza · Dubai, 2021</figcaption>
          </figure>
          <div class="project-copy">
            <p class="project-index">14 <span>Monitor engineering · Nancy Ajram</span></p>
            <h3 id="expo-title">Nancy Ajram.<br /><em>Expo 2020 Dubai.</em></h3>
            <p>Monitor engineering for Nancy Ajram’s Infinite Nights performance at Expo 2020 Dubai on 12 November 2021.</p>
            <p>The concert took place beneath the dome of Al Wasl Plaza and was streamed internationally as part of the Expo’s live music series.</p>
            <dl class="project-details"><div><dt>My role</dt><dd>Monitor engineer for Nancy Ajram</dd></div><div><dt>Venue</dt><dd>Al Wasl Plaza · Dubai, UAE</dd></div><div><dt>Date</dt><dd>12 November 2021</dd></div></dl>
            <a class="text-link" href="{e(expo_coverage_url)}" target="_blank" rel="noopener noreferrer">Explore the official concert archive <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
            <p class="source-note">Concert photo · Expo 2020 Dubai / Virtual Expo</p>
          </div>
        </article>
        <article class="project-feature project-feature--concert project-feature--portrait" id="ehdeniyat-adam" aria-labelledby="ehdeniyat-adam-title" data-reveal>
          <figure class="project-poster">
            <a href="{e(gallery_data[14]['src'])}" data-gallery-index="14" aria-label="Enlarge Adam performing at Ehdeniyat 2025" aria-haspopup="dialog" aria-controls="lightbox">
              {image("adam-ehdeniyat-2025.jpg", "Adam singing with musicians behind him at Ehdeniyat, 31 July 2025 — photo via Beiruting", sizes="(max-width: 760px) 100vw, 50vw")}
            </a>
            <figcaption>Adam · Ehdeniyat International Festival · 31 July 2025</figcaption>
          </figure>
          <div class="project-copy">
            <p class="project-index">15 <span>Monitor engineering · Adam</span></p>
            <h3 id="ehdeniyat-adam-title">Adam.<br /><em>Ehdeniyat 2025.</em></h3>
            <p>Monitor engineering for Adam’s performance at Ehdeniyat International Festival in Ehden, North Lebanon, on 31 July 2025.</p>
            <p>The evening included songs from his own repertoire and a tribute to Ziad Rahbani.</p>
            <dl class="project-details"><div><dt>My role</dt><dd>Monitor engineer for Adam</dd></div><div><dt>Festival</dt><dd>Ehdeniyat International Festival · Ehden, Lebanon</dd></div><div><dt>Date</dt><dd>31 July 2025</dd></div></dl>
            <a class="text-link" href="{e(adam_ehdeniyat_coverage_url)}" target="_blank" rel="noopener noreferrer">Explore the concert coverage <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
            <p class="source-note">Photo: <a href="{e(adam_ehdeniyat_gallery_url)}" target="_blank" rel="noopener noreferrer">Beiruting<span class="sr-only"> (opens in a new tab)</span></a> · <a href="{e(ehdeniyat_programme_url)}" target="_blank" rel="noopener noreferrer">Festival programme<span class="sr-only"> (opens in a new tab)</span></a></p>
          </div>
        </article>
        <article class="project-feature" data-reveal>
          <figure class="project-photo">
            {image("pope-leo-waterfront.jpg", "Stage prepared for Pope Leo XIV’s 2025 visit to Lebanon", sizes="(max-width: 760px) 100vw, 55vw")}
            <figcaption>Papal visit · Lebanon, 2025</figcaption>
          </figure>
          <div class="project-copy">
            <p class="project-index">16 <span>Broadcast sound engineering</span></p>
            <h3>A moment<br /><em>to be heard.</em></h3>
            <p>Broadcast sound engineering for the Papal Mass at Beirut Waterfront during Pope Leo XIV’s 2025 visit to Lebanon.</p>
            <dl class="project-details"><div><dt>Production</dt><dd>Papal Mass</dd></div><div><dt>Location</dt><dd>Beirut, Lebanon · 2025</dd></div></dl>
            <a class="text-link" href="https://www.youtube.com/watch?v=BVXL9Sy_HMo" target="_blank" rel="noopener noreferrer">Watch the official broadcast <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
            <p class="source-note">Full production · Vatican News</p>
          </div>
        </article>
        <div class="project-pair" data-reveal-group>
          <article class="project-studio" data-reveal>
            <div class="studio-image">{image("studio-manley-outboard.jpg", "Hands adjusting Manley outboard audio equipment during studio work", sizes="(max-width: 760px) 100vw, 50vw")}</div>
            <div class="project-copy">
              <p class="project-index">17 <span>Recording · Mixing · Mastering</span></p>
              <h3>StudioJPB.<br /><em>Since 2008.</em></h3>
              <p>I founded Studio Jean-Pierre Boutros in Jounieh, Lebanon, as a home for my studio work, from recording sessions to the final master.</p>
              <a class="text-link" href="#about">Meet the engineer <span aria-hidden="true">↗</span></a>
            </div>
          </article>
          <article class="project-integration" data-reveal>
            <p class="project-index">18 <span>Audio system integration</span></p>
            <div class="signal-lines" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></div>
            <h3>Studio systems.<br /><em>Working together.</em></h3>
            <p>My integration work includes recording facilities such as Merwas Studios in Riyadh and Playsound Studios in Lebanon.</p>
            <div class="integration-credit"><span>Selected facilities</span><p>Merwas Studios <small>Riyadh, Saudi Arabia</small></p><p>Playsound Studios <small>Lebanon</small></p></div>
            <a class="text-link" href="https://www.guinnessworldrecords.com/world-records/723575-largest-music-production-studio" target="_blank" rel="noopener noreferrer">About the Merwas studio <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
            <p class="source-note">Merwas was recognised by Guinness World Records as the world’s largest music production studio in 2022.</p>
          </article>
        </div>
'''


# Card summaries stay separate from the full, sourced project descriptions above.
# Tuple fields: anchor, artist/title, production, location/date, role, category, photo, featured.
projects = [
    ("the-eighties", "The Eighties… The Knockout", "National Theatre · JACC", "Kuwait · 2026", "FOH engineer", "foh", 0, True),
    ("marina-viotti", "Marina Viotti", "Opera under the stars", "Zouk Mikael · 2026", "FOH engineer", "foh", 1, False),
    ("cartoon-orchestra", "Cartoon Orchestra", "Sheikh Jaber Al-Ahmad Cultural Centre", "Kuwait · 2025", "FOH engineer", "foh", 2, False),
    ("al-sharq-symphony", "Al Sharq Symphony", "Marcel Khalifé & Istanbul Philharmonic", "Istanbul · 2017", "FOH engineer", "foh", 3, False),
    ("abeer-nehme-qatar", "Abeer Nehme", "With the Qatar Philharmonic Orchestra", "Doha · 2026", "FOH engineer", "foh", 4, True),
    ("baligh-hamdi-night", "Nancy Ajram", "Baligh Hamdi Night", "Riyadh · 2023", "Monitor engineer", "monitors", 5, True),
    ("warda-night", "Nancy Ajram", "Warda Night", "Jeddah · 2024", "Monitor engineer", "monitors", 6, False),
    ("night-of-arab-stars", "Nancy Ajram", "Night of Arab Stars · Riyadh Season", "Riyadh · 2023", "Monitor engineer", "monitors", 7, False),
    ("lebanese-philharmonic-diman", "Lebanese Philharmonic", "Eternal Covenant · Harout Fazlian", "Diman · 2026", "FOH engineer", "foh", 8, False),
    ("nancy-ajram-olympia", "Nancy Ajram", "L’Olympia", "Paris · 2022", "FOH engineer", "foh", 9, True),
    ("marcel-khalife-muscat", "Marcel Khalifé", "Royal Opera House Muscat", "Muscat · 2019", "FOH engineer", "foh", 10, True),
    ("ehdeniyat-abeer-nehme", "Abeer Nehme", "Ehdeniyat International Festival", "Ehden · 2025", "FOH engineer", "foh", 12, False),
    ("ehdeniyat-al-shami", "Al Shami", "Ehdeniyat International Festival", "Ehden · 2025", "FOH engineer", "foh", 13, True),
    ("nancy-ajram-expo-dubai", "Nancy Ajram", "Infinite Nights · Expo 2020 Dubai", "Dubai · 2021", "Monitor engineer", "monitors", 11, False),
    ("ehdeniyat-adam", "Adam", "Ehdeniyat International Festival", "Ehden · 2025", "Monitor engineer", "monitors", 14, False),
    ("papal-broadcast", "Papal Mass", "Live broadcast · Beirut Waterfront", "Beirut · 2025", "Broadcast sound engineer", "broadcast", 20, False),
    ("studio-jpb", "StudioJPB", "Recording, mixing & mastering", "Jounieh · Since 2008", "Founder & sound engineer", "studio", 18, False),
    ("studio-integration", "Studio systems", "Merwas Studios & Playsound Studios", "Riyadh & Lebanon", "Audio system integration", "studio", "studio-mixing-console.jpg", False),
]
project_articles = re.findall(r'<article\b[^>]*>.*?</article>', PROJECT_DETAILS, re.S)
if len(project_articles) != len(projects):
    raise ValueError("Project summaries and full descriptions must stay in sync")
project_dialogs = []
project_cards = {}
for project, article in zip(projects, project_articles):
    slug, title, production, location, role, category, photo, featured = project
    opening = re.match(r'<article\b[^>]*>', article)[0]
    article_id = re.search(r'\bid="([^"]+)"', opening)
    if article_id and article_id[1] != slug:
        raise ValueError(f"Project order mismatch: {slug}")
    labelledby = re.search(r'aria-labelledby="([^"]+)"', opening)
    title_id = labelledby[1] if labelledby else f"{slug}-title"
    article = article.replace(opening, re.sub(r'\s(?:id|data-reveal)="[^"]*"|\sdata-reveal(?=[\s>])', '', opening), 1)
    if not labelledby:
        article = article.replace('<h3>', f'<h3 id="{slug}-title">', 1)
    project_dialogs.append(f'''<dialog class="project-dialog" id="{slug}" aria-labelledby="{title_id}" data-project-dialog open>
  <div class="project-dialog-bar"><p>{e(title)}<span>{e(role)}</span></p><button type="button" class="dialog-close" data-close aria-label="Close project">✕</button></div>
  {article}
  <p class="project-permalink"><a class="text-link" href="/projects/{slug}/">Read the full project page <span aria-hidden="true">↗</span></a></p>
</dialog>''')
    filename = gallery[photo][0] if isinstance(photo, int) else photo
    alt = gallery[photo][2] if isinstance(photo, int) else "Studio mixing console and audio equipment"
    source = gallery_sources.get(filename)
    source_html = (f'<p class="portfolio-credit">Photo: <a href="{e(source["url"])}" target="_blank" rel="noopener noreferrer">{e(source["name"])}<span class="sr-only"> (opens in a new tab)</span></a></p>' if source else '')
    poster_class = ' portfolio-card--poster' if photo in (0, 2) else ''
    featured_attr = ' data-featured' if featured else ''
    project_cards[slug] = f'''<article class="portfolio-card{poster_class}" data-project-card="{slug}" data-category="{category}"{featured_attr}>
  <a class="portfolio-link" href="/projects/{slug}/" data-project-open="{slug}">
    <div class="portfolio-image">
      {image(filename, alt, sizes="(max-width: 600px) 100vw, 50vw")}
      <span class="portfolio-role">{e(role)}</span>
    </div>
    <div class="portfolio-copy"><p class="portfolio-location">{e(location)}</p><h3>{e(title)}</h3><p class="portfolio-production">{e(production)}</p><span class="portfolio-arrow" aria-hidden="true">↗</span></div>
  </a>
{source_html}
</article>'''

featured_order = ["nancy-ajram-olympia", "abeer-nehme-qatar", "marcel-khalife-muscat",
                  "ehdeniyat-al-shami", "baligh-hamdi-night", "the-eighties"]
card_order = featured_order + [p[0] for p in projects if p[0] not in featured_order]
filter_labels = [("featured", "Featured"), ("all", "All work"), ("foh", "FOH"),
                 ("monitors", "Monitors"), ("broadcast", "Broadcast"), ("studio", "Studio")]
filter_buttons = ''.join(f'<button type="button" data-project-filter="{key}" aria-pressed="false" aria-controls="portfolio-grid">{label}</button>' for key, label in filter_labels)
portfolio_html = f'''<div class="portfolio-toolbar">
  <div class="portfolio-filters" role="group" aria-label="Filter projects" hidden>{filter_buttons}</div>
  <p class="portfolio-count" id="portfolio-count" role="status" aria-live="polite" aria-atomic="true">18 projects</p>
</div>
<div class="portfolio-grid" id="portfolio-grid">{''.join(project_cards[slug] for slug in card_order)}</div>
<div class="portfolio-footer"><p>Every room has a different story.</p><button class="text-link portfolio-more" type="button" data-show-all-projects hidden>View all 18 projects <span aria-hidden="true">↗</span></button></div>
<div class="project-details-fallback">{''.join(project_dialogs)}</div>'''

INDEX = f'''<!DOCTYPE html>
<html lang="en">
<head>
  {page_head("/", "Jean-Pierre Boutros | International FOH & Sound Engineer", DESCRIPTION,
             structured=graph("/", "Jean-Pierre Boutros | International FOH & Sound Engineer", DESCRIPTION, page_type="ProfilePage"),
             preload_image="live-outdoor-foh-night.jpg", image_sizes="(max-width: 760px) 100vw, 55vw")}
</head>
<body>
  <a class="skip-link" href="#main">Skip to content</a>
  <div class="progress" aria-hidden="true"></div>
  <nav class="nav" id="nav" aria-label="Primary">
    <a href="#top" class="nav-brand"><img class="nav-logo" src="jpb-monogram.png" alt="" width="27" height="32" /><span>Jean-Pierre Boutros</span></a>
    <div class="nav-links">{nav_links("nav-contact")}</div>
    <button class="nav-burger" type="button" aria-label="Open navigation" aria-expanded="false" aria-controls="mobileMenu" aria-haspopup="dialog">
      <span></span><span></span><span></span>
    </button>
  </nav>
  <dialog class="mobile-menu" id="mobileMenu" aria-label="Navigation">
    <button type="button" class="dialog-close" data-close aria-label="Close navigation">✕</button>
    <p class="eyebrow">Jean-Pierre Boutros</p>
    <nav aria-label="Mobile">{nav_links("mm-contact")}</nav>
    <p class="menu-location">Lebanon · Working internationally</p>
  </dialog>

  <header class="hero hero--portrait" id="top" tabindex="-1">
    <div class="hero-shell container">
      <div class="hero-content">
        <p class="eyebrow hero-eyebrow"><span></span>Sound engineer</p>
        <h1 class="hero-title">Jean-Pierre<br /><em>Boutros.</em></h1>
        <div class="hero-description">
          <p class="hero-role">FOH. Monitors. Studio. Broadcast.</p>
          <p class="hero-lede">An ear for the artist.<br />A sound that fills the room.</p>
        </div>
        <div class="hero-actions">
          <a href="#work" class="btn btn-primary">Explore selected work <span aria-hidden="true">↘</span></a>
          <a href="{e(profile_url)}" class="hero-profile" download="Jean-Pierre-Boutros-Profile.pdf" aria-label="Download professional profile (PDF, 1 page, {profile_size})">Download profile <span aria-hidden="true">↓</span><span class="hero-profile-format">PDF · 1 page</span></a>
        </div>
        <p class="hero-location">Based in Lebanon <span aria-hidden="true">/</span> Working internationally</p>
      </div>
      <figure class="hero-portrait">
        {image("live-outdoor-foh-night.jpg", "Jean-Pierre Boutros at the front-of-house console during an outdoor concert", sizes="(max-width: 760px) 100vw, 55vw", eager=True)}
        <figcaption><span>At front of house</span><span>In the moment. In the mix.</span></figcaption>
        <a href="#about" class="hero-about" aria-label="Meet Jean-Pierre Boutros"><span aria-hidden="true">↗</span></a>
      </figure>
    </div>
    <div class="hero-wave" aria-hidden="true">{''.join(f'<span style="height:{h}%;--wave-duration:{1.4 + (i % 7) * .21:.2f}s;--wave-delay:-{(i % 11) * .17:.2f}s"></span>' for i, h in enumerate([20,55,80,40,70,30,90,50,65,25,75,45,100,55,35,80,60,20,70,45,90,30,65,50,85,40,70,25,55,15]))}</div>
  </header>

  <main id="main" tabindex="-1">
    <section class="section" id="work" aria-labelledby="work-title" tabindex="-1">
      <div class="container">
        <div class="section-heading" data-reveal>
          <div><p class="eyebrow">Selected work</p><h2 class="section-title" id="work-title">On stage.<br /><em>Behind the sound.</em></h2></div>
          <p class="section-intro">From intimate performances to orchestras and festival stages. Explore the artists, the rooms, and my role in the mix.</p>
        </div>
        {portfolio_html}
      </div>
    </section>

    <section class="section section--alt" id="credits" aria-labelledby="credits-title" tabindex="-1">
      <div class="container">
        <div class="section-heading" data-reveal>
          <div><p class="eyebrow">Selected collaborations</p><h2 class="section-title" id="credits-title">On stage.<br /><em>In good company.</em></h2></div>
          <p class="section-intro">Artists, ensembles, and productions I’ve worked with across live and studio settings.</p>
        </div>
        <ul class="credits-list" aria-label="Artists, ensembles and productions" data-reveal-group>{artist_html}</ul>
        <section class="broadcast" id="tv" aria-labelledby="broadcast-title" tabindex="-1">
          <div class="broadcast-heading"><p class="eyebrow">On air</p><h3 id="broadcast-title">Television &amp; productions</h3></div>
          <ul class="broadcast-list" data-reveal-group>{tv_html}
            <li class="broadcast-row"><span class="tv-channel">UN Women</span><h4>Advocacy events &amp; productions</h4><span class="broadcast-format">Production collaboration</span></li>
          </ul>
        </section>
      </div>
    </section>

    <section class="section" id="about" aria-labelledby="about-title" tabindex="-1">
      <div class="container">
        <div class="about-grid" data-reveal-group>
          <div class="about-copy" data-reveal>
            <p class="eyebrow">The engineer</p>
            <h2 class="section-title" id="about-title">An ear for the music.<br /><em>A mind for the details.</em></h2>
            <p class="lead">I’m Jean-Pierre Boutros, an international sound engineer based in Lebanon, working with artists, musicians, and production teams worldwide.</p>
            <p>My work moves between the stage, the studio, and the broadcast desk: live sound, front-of-house and monitor mixing, concerts and festivals, recording, studio mixing, mastering, and audio system integration. I bring the same attention to each: understanding the performance and shaping the sound around it.</p>
            <p>I founded StudioJPB in 2008. Alongside engineering and studio integration, I build audio software through Zynforge Audio, turning everyday production challenges into practical tools.</p>
            <a class="text-link" href="{e(profile_url)}" download="Jean-Pierre-Boutros-Profile.pdf" aria-label="Download Jean-Pierre Boutros’s professional profile (PDF, 1 page, {profile_size})">Download profile (PDF) <span aria-hidden="true">↓</span></a>
          </div>
          <figure class="about-photo" data-reveal>
            {image("about-portrait.jpg", "Jean-Pierre Boutros, sound engineer and founder of StudioJPB", sizes="(max-width: 760px) 100vw, 40vw")}
            <figcaption>Jean-Pierre Boutros <span>Sound engineer · Founder, StudioJPB &amp; Zynforge Audio</span></figcaption>
          </figure>
        </div>
        <div class="expertise">
          <h3>Areas of practice</h3>
          <ul class="skills" data-reveal-group>{''.join(f'<li><a href="/{slug}/">{e(skill)}</a></li>' for skill, slug in [('Live sound & FOH', 'live-sound-engineer'), ('Monitor engineering', 'live-sound-engineer'), ('Broadcast sound', 'broadcast-audio-engineer'), ('Recording & tracking', 'recording-engineer'), ('Mixing & mastering', 'mixing-mastering'), ('Audio system integration', 'studio-system-integration')])}<li>Sound design &amp; post-production</li></ul>
        </div>
        <p class="expertise-more"><a class="text-link" href="/services/">Explore all engineering services <span aria-hidden="true">↗</span></a></p>
        {faq_html(HOME_FAQ, "About the engineer and international projects")}
      </div>
    </section>

    <section class="section section--alt" id="zynforge" aria-labelledby="zynforge-title" tabindex="-1">
      <div class="container">
        <div class="section-heading" data-reveal>
          <div><p class="eyebrow">From engineer to developer</p><h2 class="section-title" id="zynforge-title">Built from experience.<br /><em>Zynforge Audio.</em></h2></div>
          <p class="section-intro">The tools I build come from the work I do. Zynforge Audio brings that experience to software for the stage and studio.</p>
        </div>
        <div class="product-grid" data-reveal-group>{zyn_html}</div>
        <a class="text-link product-enquiry" href="mailto:jp@jeanpierreboutros.com?subject=Zynforge%20Audio%20enquiry">Ask me about Zynforge <span aria-hidden="true">↗</span></a>
      </div>
    </section>

    <section class="section" id="gallery" aria-labelledby="gallery-title" tabindex="-1">
      <div class="container">
        <div class="section-heading" data-reveal>
          <div><p class="eyebrow">Behind the scenes</p><h2 class="section-title" id="gallery-title">A life<br /><em>in sound.</em></h2></div>
          <p class="section-intro">The desk. The room. The moments between. A closer look at the working side of a performance.</p>
        </div>
        <div class="gallery-grid" id="gallery-grid" data-reveal-group>{''.join(gallery_items)}</div>
        <button class="text-link gallery-more" type="button" aria-controls="gallery-grid" aria-expanded="false" hidden>View all 24 photographs <span aria-hidden="true">↗</span></button>
      </div>
    </section>

    <section class="section section--contact" id="contact" aria-labelledby="contact-title" tabindex="-1">
      <div class="container contact-grid">
        <div data-reveal><p class="eyebrow">Start a conversation</p><h2 class="section-title" id="contact-title">Good sound starts<br /><em>with a conversation.</em></h2><p class="section-intro">For a concert, a recording, a broadcast, or a studio system, tell me what you’re working on.</p><p class="contact-location">{e(AVAILABILITY)} <a href="/international-projects/">International project information</a></p></div>
        <div class="contact-details">
          <a href="mailto:jp@jeanpierreboutros.com" class="contact-link"><span><span class="contact-tag">Email</span>jp@jeanpierreboutros.com</span><span aria-hidden="true">↗</span></a>
          <a href="https://wa.me/9613883863" target="_blank" rel="noopener noreferrer" class="contact-link"><span><span class="contact-tag">WhatsApp</span>+961 3 883 863</span><span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
          <a href="{e(profile_url)}" download="Jean-Pierre-Boutros-Profile.pdf" class="contact-link"><span><span class="contact-tag">Professional profile</span>Download PDF · 1 page · {profile_size}</span><span aria-hidden="true">↓</span></a>
          <div class="social"><a href="https://www.instagram.com/jp.boutros" target="_blank" rel="noopener noreferrer">Instagram<span class="sr-only"> (opens in a new tab)</span></a><a href="https://www.facebook.com/jean.p.boutros" target="_blank" rel="noopener noreferrer">Facebook<span class="sr-only"> (opens in a new tab)</span></a></div>
        </div>
      </div>
    </section>
  </main>
  {site_links()}
  <footer class="footer container">
    <a class="footer-brand" href="#top"><img src="jpb-monogram.png" alt="" width="27" height="32" />Jean-Pierre Boutros</a>
    <span>© {date.today().year} · Sound engineer · Lebanon</span><a class="back-top" href="#top">Back to top <span aria-hidden="true">↑</span></a>
  </footer>

  <button class="motion-toggle" id="motionToggle" type="button" aria-label="Pause animations" hidden>
    <span class="motion-icon" aria-hidden="true">Ⅱ</span><span class="motion-label">Pause motion</span>
  </button>

  <dialog class="lightbox" id="lightbox" aria-labelledby="lightbox-title" aria-describedby="lightbox-caption">
    <h2 class="sr-only" id="lightbox-title">Production gallery</h2>
    <button type="button" class="dialog-close" data-close aria-label="Close photograph">✕</button>
    <button type="button" class="lightbox-prev" aria-label="Previous photograph">‹</button>
    <figure><img class="lightbox-img" alt="" hidden /><figcaption><span id="lightbox-caption"></span><span id="lightbox-count" role="status" aria-live="polite" aria-atomic="true"></span></figcaption></figure>
    <button type="button" class="lightbox-next" aria-label="Next photograph">›</button>
  </dialog>
  <script type="application/json" id="gallery-data">{json.dumps(gallery_data, ensure_ascii=False).replace('<', chr(92) + 'u003c')}</script>
</body>
</html>
'''

(OUT / "index.html").write_text(INDEX, encoding="utf-8")
print(f"index.html written: {len(artists)} artist credits, {len(gallery)} gallery photographs")

search_paths = render_search_pages({
    "home": INDEX, "image": image, "projects": projects,
    "articles": project_articles, "cards": project_cards, "gallery": gallery,
    "sources": gallery_sources, "gallery_data": gallery_data,
})
print(f"Search pages written: {len(search_paths)} canonical pages, including the homepage")
