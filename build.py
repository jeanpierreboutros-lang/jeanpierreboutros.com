#!/usr/bin/env python3
"""Render the portfolio from confirmed credits and local image metadata."""
import html
import json
from datetime import date
from hashlib import sha256
from pathlib import Path

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
]

# Captions describe visible content, without guessing venues or artists.
gallery = [
    ("the-eighties-knockout-kuwait-2026.jpg", "The Eighties… The Knockout", "Signed production artwork above a cast photograph for The Eighties… The Knockout in Kuwait", "FOH engineer · Kuwait, 2026"),
    ("marina-viotti-zouk-mikael-2026.jpg", "Marina Viotti · Opera gala", "Front-of-house mixing console facing the illuminated stage at the Beirut International Opera Festival gala in Zouk Mikael", "FOH engineer · Zouk Mikael, 2026"),
    ("cartoon-orchestra-kuwait-2025.jpg", "Cartoon Orchestra", "Cartoon Orchestra production poster displayed at Sheikh Jaber Al-Ahmad Cultural Centre in Kuwait", "FOH engineer · Kuwait, 2025"),
    ("al-sharq-symphony-istanbul-2017.jpg", "Al Sharq Symphony", "Orchestra and choir performing Al Sharq Symphony in Istanbul, from Al Sharq Youth’s official concert video", "FOH engineer · Istanbul, 2017"),
    ("abeer-nehme-qatar-philharmonic-2026.jpg", "Abeer Nehme · Qatar Philharmonic", "Abeer Nehme singing on stage with the Qatar Philharmonic Orchestra at U VENUE in Doha, 23 January 2026", "FOH engineer · U VENUE, Doha, 2026"),
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

gallery_sources = {
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
    "Abeer Nehme": ("abeer-nehme-qatar", "FOH engineer · Qatar, 2026"),
    "Marcel Khalifé": ("al-sharq-symphony", "FOH engineer · Istanbul, 2017"),
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
    gallery_items.append(f'''<figure class="gallery-card{poster_class}">
  <a class="gallery-item" href="{e(full["src"])}" data-gallery-index="{index}"
     aria-label="Enlarge photo: {e(alt)}" aria-haspopup="dialog" aria-controls="lightbox">
    {image(filename, alt, sizes="(max-width: 600px) 100vw, (max-width: 980px) 50vw, 33vw")}
    <span class="gallery-expand" aria-hidden="true">↗</span>
  </a>
  <figcaption><span>{e(title)}</span><span>{e(context)}{credit_html}</span></figcaption>
</figure>''')

jsonld = {
    "@context": "https://schema.org", "@type": "Person", "name": "Jean-Pierre Boutros",
    "jobTitle": "Live, studio and broadcast sound engineer",
    "description": "Sound engineer based in Lebanon, working internationally in live sound, recording, mixing, mastering, broadcast and audio system integration. Founder of StudioJPB and Zynforge Audio.",
    "url": "https://www.jeanpierreboutros.com/", "email": "jp@jeanpierreboutros.com",
    "telephone": "+9613883863", "image": "https://www.jeanpierreboutros.com/photos/about-portrait.jpg",
    "address": {"@type": "PostalAddress", "addressLocality": "Jounieh", "addressCountry": "LB"},
    "sameAs": ["https://www.instagram.com/jp.boutros", "https://www.facebook.com/jean.p.boutros"],
    "knowsAbout": ["Live Sound", "FOH Engineering", "Broadcast Sound", "Recording", "Mixing", "Mastering", "Audio System Integration", "Sound Design", "Post-Production"],
    "affiliation": [
        {"@type": "Organization", "name": "Studio Jean-Pierre Boutros (StudioJPB)", "foundingDate": "2008", "founder": {"@type": "Person", "name": "Jean-Pierre Boutros"}},
        {"@type": "Organization", "name": "Zynforge Audio", "founder": {"@type": "Person", "name": "Jean-Pierre Boutros"}},
    ],
}

INDEX = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Jean-Pierre Boutros — Live, Studio &amp; Broadcast Sound Engineer</title>
  <meta name="description" content="Jean-Pierre Boutros is a sound engineer based in Lebanon, working internationally in live sound, studio recording, mixing, mastering, broadcast and audio system integration." />
  <meta name="author" content="Jean-Pierre Boutros" />
  <meta name="robots" content="index, follow" />
  <meta name="theme-color" content="#0b0b0b" />
  <link rel="canonical" href="https://www.jeanpierreboutros.com/" />
  <link rel="icon" type="image/png" href="favicon.png" />
  <link rel="apple-touch-icon" href="favicon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.jeanpierreboutros.com/" />
  <meta property="og:site_name" content="Jean-Pierre Boutros" />
  <meta property="og:title" content="Jean-Pierre Boutros — Sound Engineer" />
  <meta property="og:description" content="Live sound. Studio craft. Broadcast precision. Selected work and collaborations from sound engineer Jean-Pierre Boutros." />
  <meta property="og:image" content="https://www.jeanpierreboutros.com/photos/about-portrait.jpg" />
  <meta property="og:image:alt" content="Jean-Pierre Boutros, sound engineer" />
  <meta property="og:image:width" content="1920" />
  <meta property="og:image:height" content="1280" />
  <meta property="og:locale" content="en_US" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Jean-Pierre Boutros — Sound Engineer" />
  <meta name="twitter:description" content="Live, studio and broadcast sound engineer. Based in Lebanon, working internationally." />
  <meta name="twitter:image" content="https://www.jeanpierreboutros.com/photos/about-portrait.jpg" />
  <meta name="twitter:image:alt" content="Jean-Pierre Boutros, sound engineer" />
  <script type="application/ld+json">{json.dumps(jsonld, ensure_ascii=False)}</script>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,500;1,400;1,500&amp;family=Hanken+Grotesk:wght@400;500;600&amp;display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css?v={asset_versions['styles.css']}" />
  <script src="main.js?v={asset_versions['main.js']}" defer></script>
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

  <header class="hero" id="top" tabindex="-1">
    <div class="hero-bg" aria-hidden="true">
      {image("hero-foh.jpg", "", eager=True)}
      <div class="hero-grad-1"></div><div class="hero-grad-2"></div>
    </div>
    <div class="hero-content">
      <p class="eyebrow hero-eyebrow"><span></span>Beirut, Lebanon · Working internationally</p>
      <h1 class="hero-title">Jean-Pierre<br /><em>Boutros</em></h1>
      <div class="hero-bottom">
        <div class="hero-description">
          <p class="hero-role">Live, studio &amp; broadcast <span>sound engineer.</span></p>
          <p class="hero-lede">From the first note to the final mix.<br />Sound shaped around the performance.</p>
        </div>
        <div class="hero-actions">
          <a href="#work" class="btn btn-primary">Explore selected work <span aria-hidden="true">↘</span></a>
          <a href="#contact" class="btn btn-ghost">Get in touch</a>
        </div>
      </div>
    </div>
    <div class="hero-wave" aria-hidden="true">{''.join(f'<span style="height:{h}%;--wave-duration:{1.4 + (i % 7) * .21:.2f}s;--wave-delay:-{(i % 11) * .17:.2f}s"></span>' for i, h in enumerate([20,55,80,40,70,30,90,50,65,25,75,45,100,55,35,80,60,20,70,45,90,30,65,50,85,40,70,25,55,15]))}</div>
  </header>

  <main id="main" tabindex="-1">
    <div class="practice-strip container" role="group" aria-label="Areas of practice" data-reveal-group>
      <p><span>On stage</span>Live sound &amp; broadcast</p>
      <p><span>In the studio</span>Recording, mixing &amp; mastering</p>
      <p><span>Behind the systems</span>Audio integration &amp; software</p>
    </div>

    <section class="section" id="work" aria-labelledby="work-title" tabindex="-1">
      <div class="container">
        <div class="section-heading" data-reveal>
          <div><p class="eyebrow">Selected work</p><h2 class="section-title" id="work-title">The work.<br /><em>The worlds behind it.</em></h2></div>
          <p class="section-intro">Concert stages, studio sessions, and live broadcasts. A few perspectives on my work in sound.</p>
        </div>
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
        </div>
        <article class="project-feature" data-reveal>
          <figure class="project-photo">
            {image("pope-leo-waterfront.jpg", "Stage prepared for Pope Leo XIV’s 2025 visit to Lebanon", sizes="(max-width: 760px) 100vw, 55vw")}
            <figcaption>Papal visit · Lebanon, 2025</figcaption>
          </figure>
          <div class="project-copy">
            <p class="project-index">06 <span>Broadcast sound engineering</span></p>
            <h3>A moment<br /><em>to be heard.</em></h3>
            <p>Broadcast sound engineering for the Papal Mass at Beirut Waterfront during Pope Leo XIV’s 2025 visit to Lebanon.</p>
            <dl class="project-details"><div><dt>Production</dt><dd>Papal Mass</dd></div><div><dt>Location</dt><dd>Beirut, Lebanon · 2025</dd></div></dl>
            <a class="text-link" href="https://www.youtube.com/watch?v=BVXL9Sy_HMo" target="_blank" rel="noopener noreferrer">Watch the official broadcast <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
            <p class="source-note">Full production · Vatican News</p>
          </div>
        </article>
        <div class="project-pair" data-reveal-group>
          <article class="project-studio" data-reveal>
            <div class="studio-image">{image("studio-strip.jpg", "Jean-Pierre Boutros working at a studio mixing console", sizes="(max-width: 760px) 100vw, 50vw")}</div>
            <div class="project-copy">
              <p class="project-index">07 <span>Recording · Mixing · Mastering</span></p>
              <h3>StudioJPB.<br /><em>Since 2008.</em></h3>
              <p>I founded Studio Jean-Pierre Boutros in Jounieh, Lebanon, as a home for my studio work, from recording sessions to the final master.</p>
              <a class="text-link" href="#about">Meet the engineer <span aria-hidden="true">↗</span></a>
            </div>
          </article>
          <article class="project-integration" data-reveal>
            <p class="project-index">08 <span>Audio system integration</span></p>
            <div class="signal-lines" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span></div>
            <h3>Studio systems.<br /><em>Working together.</em></h3>
            <p>My integration work includes recording facilities such as Merwas Studios in Riyadh and Playsound Studios in Lebanon.</p>
            <div class="integration-credit"><span>Selected facilities</span><p>Merwas Studios <small>Riyadh, Saudi Arabia</small></p><p>Playsound Studios <small>Lebanon</small></p></div>
            <a class="text-link" href="https://www.guinnessworldrecords.com/world-records/723575-largest-music-production-studio" target="_blank" rel="noopener noreferrer">About the Merwas studio <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
            <p class="source-note">Merwas was recognised by Guinness World Records as the world’s largest music production studio in 2022.</p>
          </article>
        </div>
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
            <p class="lead">I’m Jean-Pierre, a live and studio sound engineer based in Lebanon, working with artists, musicians, and production teams internationally.</p>
            <p>My work moves between the stage, the studio, and the broadcast desk. I bring the same attention to each: understanding the performance and shaping the sound around it.</p>
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
          <ul class="skills" data-reveal-group>{''.join(f'<li>{e(skill)}</li>' for skill in ['Live sound & FOH', 'Broadcast sound', 'Recording & tracking', 'Mixing & mastering', 'Audio system integration', 'Sound design & post-production'])}</ul>
        </div>
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
          <p class="section-intro">A few frames from the working side of a performance. Select a photograph to take a closer look.</p>
        </div>
        <div class="gallery-grid" data-reveal-group>{''.join(gallery_items)}</div>
      </div>
    </section>

    <section class="section section--contact" id="contact" aria-labelledby="contact-title" tabindex="-1">
      <div class="container contact-grid">
        <div data-reveal><p class="eyebrow">Start a conversation</p><h2 class="section-title" id="contact-title">Good sound starts<br /><em>with a conversation.</em></h2><p class="section-intro">For a concert, a recording, a broadcast, or a studio system, tell me what you’re working on.</p><p class="contact-location">Based in Lebanon · Available for projects internationally</p></div>
        <div class="contact-details">
          <a href="mailto:jp@jeanpierreboutros.com" class="contact-link"><span><span class="contact-tag">Email</span>jp@jeanpierreboutros.com</span><span aria-hidden="true">↗</span></a>
          <a href="https://wa.me/9613883863" target="_blank" rel="noopener noreferrer" class="contact-link"><span><span class="contact-tag">WhatsApp</span>+961 3 883 863</span><span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a>
          <a href="{e(profile_url)}" download="Jean-Pierre-Boutros-Profile.pdf" class="contact-link"><span><span class="contact-tag">Professional profile</span>Download PDF · 1 page · {profile_size}</span><span aria-hidden="true">↓</span></a>
          <div class="social"><a href="https://www.instagram.com/jp.boutros" target="_blank" rel="noopener noreferrer">Instagram<span class="sr-only"> (opens in a new tab)</span></a><a href="https://www.facebook.com/jean.p.boutros" target="_blank" rel="noopener noreferrer">Facebook<span class="sr-only"> (opens in a new tab)</span></a></div>
        </div>
      </div>
    </section>
  </main>
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
