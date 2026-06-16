#!/usr/bin/env python3
# Builds clean static index.html + styles.css + main.js for the JPB redesign.
import html, json, os

OUT = os.path.dirname(os.path.abspath(__file__))
os.makedirs(OUT, exist_ok=True)

# ---- data (from the bundle component) ----
clients = [
    ("Nancy Ajram","Pop Icon","Lebanon's most celebrated pop icon and one of the Arab world's biggest stars."),
    ("Marcel Khalifé","Oud Virtuoso · UNESCO Artist for Peace","UNESCO Artist for Peace, legendary oud virtuoso and composer of modern Arabic music."),
    ("Georges Wassouf","The Sultan of Tarab","The Sultan of Tarab — Syria and Lebanon's most iconic voice in classical Arabic song."),
    ("Carole Samaha","Singer & Actress","Lebanese singer and actress known for her powerful voice and enduring presence in Arabic pop."),
    ("Abeer Nehme","Singer & Musicologist","Lebanese singer and musicologist known as 'The All-Styles Specialist' — moving between tarab, Rahbani, Syriac and Byzantine sacred music and opera, in over 20 languages."),
    ("Maya Diab","Singer & Actress","Lebanese singer, actress and fashion icon who rose to fame with the group The 4 Cats — one of the Arab world's most recognised media personalities."),
    ("Adam","Singer","Lebanese singer (Wael Shehada) with a soulful voice, beloved for his romantic tarab-pop and work in film and television."),
    ("Al Shami","Singer-Songwriter","Syrian singer-songwriter and Gen Z streaming phenomenon who fuses Middle Eastern melodies with Western pop — his hit 'Ya Leil W Yal Ein' topped 200 million views."),
    ("Melhem Zein","Singer","Lebanese singer who rose to fame on Super Star — nicknamed 'The Boss' for his powerful voice and his command of Lebanese folklore song."),
    ("Ramy Ayyach","Singer & Composer","Lebanese singer, composer and actor crowned the Arab world's 'Pop Star,' behind hits like 'Mabrouk' and 'Albi Mal.'"),
    ("Zade Dirani","Pianist & Composer","Jordanian-American pianist, composer and UNICEF goodwill ambassador whose Billboard-charting music fuses Arabic scales with classical and pop."),
    ("Joseph Attiye","Singer","Lebanese singer who became the first Lebanese to win Star Academy Arabia, beloved for romantic ballads and the anthem 'Lebnan Rah Yerjaa.'"),
    ("Georges Nehme","Singer","Lebanese singer who shared the stage with Wadih El Safi as a boy, became a lead singer in Ziad Rahbani's concerts and toured with Fairuz."),
    ("Salim Assaf","Singer · Composer · Songwriter","Lebanese singer, composer and songwriter behind major hits for Carole Samaha, Nancy Ajram, Wael Kfoury and others — a three-time Murex d'Or winner."),
    ("Mazeej","Fusion Project","A bold musical fusion project blending Arabic roots with contemporary sounds."),
    ("Orchestra Cartoon","Orchestra","A beloved Kuwaiti orchestra bringing cinematic and animated scores to life on stage."),
    ("Macadi Nahhas","Singer","Jordanian singer who revives Middle Eastern folk and heritage songs with a contemporary style, trained at the Beirut Conservatory."),
    ("Tania Saleh","Singer-Songwriter","Lebanese singer-songwriter and visual artist, a pioneer of the Arabic alternative scene blending folk, jazz and electronic sounds."),
    ("Remi Bandali","Singer","Lebanese singer who rose to fame as a child star in the 1980s, beloved across the Arab world for the anthem 'Atouna El Toufoule.'"),
    ("Rasha Rizk","Soprano","Syrian opera-trained singer-songwriter — the beloved voice behind countless Arabic cartoon and anime themes for a generation of Spacetoon viewers."),
    ("Yara","Pop Singer","One of the Arab world's biggest pop stars — born Carla Nazih al-Berkashi — beloved across the Levant and Gulf for hits sung in multiple Arabic dialects."),
    ("Leen Hayek","Pop Singer","Lebanese pop singer from Tripoli who won the first season of The Voice Kids Arabia, now an emerging voice in Lebanese pop."),
    ("Salah El Kurdi","Singer · Writer · Composer","Lebanese singer, songwriter and composer (born in Kuwait), a multi-talented artist active between Lebanon and the US."),
    ("Charbel Rouhana","Oud Virtuoso","Lebanese oud master and composer, a pioneer of 'oud jazz' who reshaped the instrument's technique and has accompanied Fairuz and Marcel Khalifé."),
    ("Chantal Bitar","Singer","Lebanese singer with a crystalline voice, known for reviving the nostalgic Lebanese folk songs of the golden era."),
    ("Carlos Azar","Singer & Actor","Lebanese singer, actor and TV presenter — son of veteran singer Joseph Azar — trained in oriental singing at the Lebanese National Conservatory."),
    ("Ziad Bourji","Singer · Actor · Composer","Lebanese singer, actor and composer who has also written songs for Georges Wassouf, Elissa and Nancy Ajram."),
    ("Sarina Cross","Singer","Lebanese-Armenian singer (Sarine Sagherian) with a multilingual repertoire spanning Armenian folk, Arabic pop and Greek song."),
    ("Ziad Jamal","Singer & Composer","Lebanese singer and composer known for refined live performances of timeless classical Arabic songs."),
    ("Mouhamad Khairy","Singer","Syrian singer from Aleppo, a torchbearer for the classical Qudud and tarab tradition with a rich, traditional voice."),
    ("Manel Mallat","Singer & Actress","Lebanese-French singer, songwriter and actress — an Arabs Got Talent finalist known for her powerful, multilingual voice and musical-theatre work."),
    ("Faraj Hanna","Singer · Buzuq · Composer","Lebanese singer, buzuq player and composer who performed with Ziad Rahbani before launching a solo project reviving classic underground songs."),
    ("UN Women","Production","United Nations entity for gender equality — collaborations on advocacy events and productions."),
    ("Mike Massy","Singer & Composer","Lebanese singer, pianist and composer — a Murex d'Or winner known for fusing Arabic song with baroque harmonies and jazz."),
    ("Ria Ellinidou","Singer","Greek singer and multi-instrumentalist from Thessaloniki, blending traditional Greek folk with laïko and jazz."),
    ("Pope Visit 2025","Historic Live Production","Sound engineering for the historic papal visit — one of the most demanding live productions of the year."),
]

gallery_all = [
    ("foh-concert-hall-aerial","tall"),("concert-arena-led-screens","tall"),
    ("live-outdoor-foh-night","tall"),("foh-pov-red-curtain-concert","wide"),
    ("foh-pov-theater-stage","wide"),("midas-heritage-console","tall"),
    ("foh-console-dark-venue","tall"),("foh-outdoor-night-setup","wide"),
    ("foh-church-concert-organ","tall"),("monitor-desk-video-screens","normal"),
    ("foh-orchestra-ornate-backdrop","tall"),("foh-purple-ornate-venue","tall"),
    ("foh-mixer-closeup-blue","normal"),("studio-manley-outboard","tall"),
    ("pope-leo-waterfront","wide"),("foh-headphones-monitor","normal"),
    ("foh-cl5-closeup","tall"),("foh-yamaha-multiview","tall"),
]
gallery = [(n,c) for (n,c) in gallery_all if os.path.exists(f"{OUT}/photos/{n}.jpg")]
missing = [n for (n,c) in gallery_all if not os.path.exists(f"{OUT}/photos/{n}.jpg")]

skills = ['Recording & Tracking','Mixing','Mastering','Live Sound','Sound Design','Post-Production']
wave = [20,55,80,40,70,30,90,50,65,25,75,45,100,55,35,80,60,20,70,45,90,30,65,50,85,40,70,25,55,15]

zyn = [
    ("zynforge-live.png","Zynforge Live","A live plugin host for live performance."),
    ("zynforge-recording.png","Zynforge Recording","Multitrack and playback software for live performance."),
    ("zynforge-stage.png","Zynforge Stage","Tools for stage plots and technical riders."),
]
tv = [
    ("MTV Lebanon","Hek Menghanni","A flagship Lebanese music television program celebrating Arab vocal talent and live performance."),
    ("Abu Dhabi TV","Ghanni Al Aali","An Abu Dhabi TV music program uniting the Arab world's biggest singing stars in fresh musical arrangements — filmed across Lebanon, Egypt, and the UAE."),
    ("Al Mayadeen TV","Ethnophilia","A 40-episode music documentary series travelling the globe to trace the roots of folk and ethnic music — winner of the Murex d'Or for Best Documentary."),
]
e = html.escape

# ---- name wall ----
nw = []
for i,(name,role,desc) in enumerate(clients):
    nw.append(f'''        <button class="namewall-cell" data-ci="{i}" type="button" aria-expanded="false">
          <span class="namewall-name">{e(name)}</span><span class="namewall-plus" aria-hidden="true">+</span>
          <span class="namewall-pop" role="dialog" aria-label="{e(name)}">
            <span class="namewall-pop-arrow" aria-hidden="true"></span>
            <span class="namewall-pop-close" role="button" aria-label="Close" tabindex="0">✕</span>
            <span class="namewall-pop-role">{e(role)}</span>
            <span class="namewall-pop-name">{e(name)}</span>
            <span class="namewall-pop-desc">{e(desc)}</span>
          </span>
        </button>''')
namewall = "\n".join(nw)

# ---- gallery ----
gc = []
for i,(n,cls) in enumerate(gallery):
    mod = f" gallery-item--{cls}" if cls in ("tall","wide") else ""
    gc.append(f'''      <button class="gallery-item{mod}" data-index="{i}" data-src="photos/{n}.jpg" type="button" aria-label="View image">
        <img src="photos/{n}.jpg" alt="" loading="lazy" decoding="async" />
      </button>''')
gallery_html = "\n".join(gc)

# ---- waves / skills / zyn / tv ----
waves = "".join(f'<span style="height:{h}%;animation-delay:{(i%10)*0.12:.2f}s"></span>' for i,h in enumerate(wave))
skill_html = "\n".join(f'        <li>{e(s)}</li>' for s in skills)
zyn_html = "\n".join(f'''        <div class="card card--zyn">
          <img class="zyn-icon" src="photos/{ic}" alt="{e(t)}" loading="lazy" decoding="async" />
          <h3>{e(t)}</h3>
          <p>{e(d)}</p>
        </div>''' for ic,t,d in zyn)
tv_html = "\n".join(f'''        <div class="card card--tv">
          <span class="tv-channel">{e(ch)}</span>
          <h3>{e(t)}</h3>
          <p>{e(d)}</p>
        </div>''' for ch,t,d in tv)

gallery_json = json.dumps([f"photos/{n}.jpg" for n,_ in gallery])

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E"
"%3Crect width='100' height='100' fill='%230b0b0b'/%3E"
"%3Ccircle cx='50' cy='38' r='4' fill='%23c8a96e'/%3E"
"%3Cpath d='M30 60 L50 40 L70 60' fill='none' stroke='%23c8a96e' stroke-width='4' stroke-linecap='round' stroke-linejoin='round'/%3E"
"%3Ctext x='50' y='82' font-family='Georgia,serif' font-size='11' letter-spacing='2' fill='%23e9e7e2' text-anchor='middle'%3EJPB%3C/text%3E%3C/svg%3E")

jsonld = {
    "@context":"https://schema.org","@type":"Person","name":"Jean-Pierre Boutros",
    "jobTitle":"Sound Engineer",
    "description":"Live and studio sound engineer based in Lebanon — mixing, mastering, live sound and system integration. Founder of Studio Jean-Pierre Boutros (StudioJPB) and Zynforge Audio.",
    "url":"https://www.jeanpierreboutros.com","email":"jp@jeanpierreboutros.com",
    "telephone":"+9613883863","image":"https://www.jeanpierreboutros.com/photos/about-portrait.jpg",
    "address":{"@type":"PostalAddress","addressLocality":"Jounieh","addressCountry":"LB"},
    "sameAs":["https://www.instagram.com/jp.boutros","https://www.facebook.com/jean.p.boutros"],
    "knowsAbout":["Sound Engineering","Mixing","Mastering","Live Sound","FOH Engineering","Sound Design","Post-Production","Recording","Audio System Integration"],
    "worksFor":{"@type":"Organization","name":"Studio Jean-Pierre Boutros (StudioJPB)","foundingDate":"2008","url":"https://www.jeanpierreboutros.com"},
}

INDEX = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />

  <title>Jean-Pierre Boutros — Sound Engineer | Mixing, Mastering & Live Sound</title>
  <meta name="description" content="Jean-Pierre Boutros is a live and studio sound engineer based in Lebanon — mixing, mastering, live sound and system integration. Founder of StudioJPB and Zynforge Audio. Credits include Nancy Ajram, Marcel Khalifé, Georges Wassouf and more." />
  <meta name="keywords" content="Jean-Pierre Boutros, sound engineer, mixing engineer, mastering engineer, live sound, FOH engineer, Lebanon, Beirut, Jounieh, StudioJPB, Zynforge, Arabic music, Nancy Ajram, Marcel Khalife, Georges Wassouf" />
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
  <meta property="og:description" content="Live and studio sound engineer based in Lebanon — mixing, mastering, live sound and system integration. Founder of StudioJPB and Zynforge Audio." />
  <meta property="og:image" content="https://www.jeanpierreboutros.com/photos/about-portrait.jpg" />
  <meta property="og:image:width" content="1920" />
  <meta property="og:image:height" content="1280" />
  <meta property="og:locale" content="en_US" />

  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="Jean-Pierre Boutros — Sound Engineer" />
  <meta name="twitter:description" content="Live and studio sound engineer based in Lebanon — mixing, mastering, live sound and system integration." />
  <meta name="twitter:image" content="https://www.jeanpierreboutros.com/photos/about-portrait.jpg" />

  <script type="application/ld+json">
{json.dumps(jsonld, indent=2, ensure_ascii=False)}
  </script>

  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,wght@0,400;0,500;1,400;1,500&family=Hanken+Grotesk:wght@300;400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="styles.css" />
</head>
<body>

  <div class="progress" aria-hidden="true"></div>

  <nav class="nav" id="nav">
    <a href="#top" class="nav-brand"><img class="nav-logo" src="jpb-monogram.png" alt="" width="27" height="32" />Jean-Pierre Boutros</a>
    <ul class="nav-links">
      <li><a href="#about">About</a></li>
      <li><a href="#zynforge">Zynforge</a></li>
      <li><a href="#credits">Credits</a></li>
      <li><a href="#tv">Broadcast</a></li>
      <li><a href="#gallery">Gallery</a></li>
      <li><a href="#contact" class="nav-contact">Contact</a></li>
    </ul>
    <button class="nav-burger" aria-label="Toggle menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </nav>

  <div class="mobile-menu" id="mobileMenu">
    <a href="#about">About</a>
    <a href="#zynforge">Zynforge</a>
    <a href="#credits">Credits</a>
    <a href="#tv">Broadcast</a>
    <a href="#gallery">Gallery</a>
    <a href="#contact" class="mm-contact">Contact</a>
  </div>

  <!-- HERO -->
  <header class="hero" id="top">
    <div class="hero-bg" aria-hidden="true">
      <img src="photos/hero-foh.jpg" alt="" decoding="async" fetchpriority="high" />
      <div class="hero-grad-1"></div>
      <div class="hero-grad-2"></div>
    </div>
    <div class="hero-content">
      <p class="hero-eyebrow"><span class="hero-rule"></span>Sound Engineer · Beirut</p>
      <h1 class="hero-title">Jean-Pierre<br /><em>Boutros</em></h1>
      <div class="hero-bottom">
        <p class="hero-lede">Translating artistic vision into immersive sound — from the studio to the front of house.</p>
        <div class="hero-actions">
          <a href="#credits" class="btn btn-primary">View Credits</a>
          <a href="#contact" class="btn btn-ghost">Get in Touch</a>
        </div>
      </div>
    </div>
    <div class="hero-wave" aria-hidden="true">{waves}</div>
    <a href="#about" class="hero-scroll" aria-label="Scroll down">
      <span>Scroll</span>
      <svg width="16" height="10" viewBox="0 0 16 10" fill="none"><path d="M1 1l7 7 7-7" stroke="#c8a96e" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg>
    </a>
  </header>

  <!-- ABOUT -->
  <section class="section" id="about">
    <div class="container">
      <div class="about-grid" data-reveal>
        <div class="about-photos">
          <div class="about-photo"><img src="photos/about-portrait.jpg" alt="Jean-Pierre Boutros — Sound Engineer" loading="lazy" decoding="async" /></div>
          <div class="about-photo about-photo--2"><img src="photos/about-live-stage.jpg" alt="Jean-Pierre Boutros at a live event" loading="lazy" decoding="async" /></div>
        </div>
        <div class="about-text">
          <p class="eyebrow">About</p>
          <div>
            <h2 class="section-title">The ear behind <em>the sound.</em></h2>
            <p class="lead">Jean-Pierre Boutros is a live and studio mix engineer working with artists, musicians, and producers around the world. He brings a meticulous ear and steady hands to both the stage and the studio.</p>
            <p>In 2008, he founded his own recording studio — <span class="hl">Studio Jean-Pierre Boutros (StudioJPB)</span> — in Jounieh, Lebanon.</p>
            <p>His work has spanned major productions, including serving as broadcast sound engineer for a Papal Mass at the Beirut Waterfront — an event reaching an audience of over 150,000.</p>
            <p>Beyond mixing, he has served as system integrator for leading recording facilities, including <span class="hl">Merwas Studios</span> in Riyadh — holder of the Guinness World Record for the world's largest music production studio — along with Playsound Studios in Lebanon and many others.</p>
            <p>Jean-Pierre is also the founder of <span class="hl">Zynforge Audio</span>, a software company building tools for audio professionals — including Zynforge Live, Zynforge Recording, and Zynforge Stage.</p>
            <p>Combining hands-on engineering experience with a developer's instinct for solving real problems, he builds and works with the tools that modern audio production depends on.</p>
          </div>
          <ul class="skills">
{skill_html}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ZYNFORGE -->
  <section class="section section--alt" id="zynforge">
    <div class="container">
      <div data-reveal>
        <p class="eyebrow">Software</p>
        <h2 class="section-title section-title--tight">Zynforge <em>Audio.</em></h2>
        <p class="section-intro">A software company building tools for audio professionals — born from real engineering problems on stage and in the studio.</p>
      </div>
      <div class="card-grid" data-reveal>
{zyn_html}
      </div>
    </div>
  </section>

  <!-- STUDIO STRIP -->
  <div class="studio-strip">
    <img src="photos/studio-strip.jpg" alt="Jean-Pierre Boutros at the mixing console" loading="lazy" decoding="async" />
    <div class="studio-strip-grad"></div>
  </div>

  <!-- CREDITS / NAME WALL -->
  <section class="section" id="credits">
    <div class="container">
      <div data-reveal>
        <p class="eyebrow">Clients</p>
        <h2 class="section-title section-title--tight">Artists I've <em>worked with.</em></h2>
        <p class="section-intro">Select a name to read more.</p>
      </div>
      <div class="namewall" data-reveal>
{namewall}
      </div>
    </div>
  </section>

  <!-- TV / BROADCAST -->
  <section class="section section--alt" id="tv">
    <div class="container">
      <div data-reveal>
        <p class="eyebrow">Television</p>
        <h2 class="section-title section-title--tight">TV &amp; broadcast <em>productions.</em></h2>
        <div class="card-grid">
{tv_html}
        </div>
      </div>
    </div>
  </section>

  <!-- GALLERY -->
  <section class="section section--gallery" id="gallery">
    <div class="container container--gallery">
      <div data-reveal>
        <p class="eyebrow">Gallery</p>
        <h2 class="section-title">Behind the <em>scenes.</em></h2>
      </div>
    </div>
    <div class="gallery-grid">
{gallery_html}
    </div>
  </section>

  <!-- CONTACT -->
  <section class="section" id="contact">
    <div class="container">
      <div class="contact" data-reveal>
        <p class="eyebrow">Contact</p>
        <h2 class="section-title section-title--lg">Let's work <em>together.</em></h2>
        <p class="section-intro">Available for studio sessions, mixing, mastering, and live sound engagements worldwide.</p>
        <div class="contact-actions">
          <a href="mailto:jp@jeanpierreboutros.com" class="contact-link"><span>jp@jeanpierreboutros.com</span><span class="contact-tag">Email</span></a>
          <a href="https://wa.me/9613883863" target="_blank" rel="noopener" class="contact-link"><span>+961 3 883 863</span><span class="contact-tag">WhatsApp</span></a>
        </div>
        <div class="social">
          <a href="https://instagram.com/jp.boutros" target="_blank" rel="noopener">Instagram</a>
          <a href="https://www.facebook.com/jean.p.boutros" target="_blank" rel="noopener">Facebook</a>
        </div>
      </div>
    </div>
  </section>

  <footer class="footer">
    <img class="footer-logo" src="jpb-monogram.png" alt="Jean-Pierre Boutros" width="47" height="56" />
    <span class="footer-name">Jean-Pierre Boutros</span>
    <span class="footer-meta">© 2026 · Sound Engineer · Beirut, Lebanon</span>
  </footer>

  <!-- LIGHTBOX -->
  <div class="lightbox" id="lightbox" aria-hidden="true">
    <button class="lightbox-close" aria-label="Close">✕</button>
    <button class="lightbox-prev" aria-label="Previous">‹</button>
    <img class="lightbox-img" src="" alt="" />
    <button class="lightbox-next" aria-label="Next">›</button>
  </div>

  <script>window.__GALLERY__ = {gallery_json};</script>
  <script src="main.js"></script>
</body>
</html>
'''

open(f"{OUT}/index.html","w").write(INDEX)
print("index.html written")
if missing:
    print("MISSING gallery images (excluded):")
    for m in missing: print("  photos/"+m+".jpg")
