"""Static search landing pages, shared metadata and connected Schema.org entities."""
import html
import json
import re
from hashlib import sha256
from pathlib import Path
from urllib.parse import quote, urlsplit
from xml.etree import ElementTree as ET

from services import AVAILABILITY, HOME_FAQ, REVIEWED, SERVICES, SERVICE_BY_SLUG
from studio_credits import CREDIT_GROUPS, studio_groups_html

ROOT = Path(__file__).resolve().parent
SITE = "https://www.jeanpierreboutros.com"
NAME = "Jean-Pierre Boutros"
PERSON = SITE + "/#person"
WEBSITE = SITE + "/#website"
DESCRIPTION = ("Jean-Pierre Boutros is a Lebanon-based international sound engineer "
               "specializing in live sound, FOH mixing, concerts, festivals, recording, "
               "studio mixing, mastering, broadcast and audio system integration.")
e = html.escape


def absolute(path):
    return SITE + "/" + path.lstrip("/")


def json_text(value):
    return json.dumps(value, ensure_ascii=False).replace("<", "\\u003c")


def plain(value):
    return " ".join(html.unescape(re.sub(r"<[^>]+>", " ", value)).split())


def root_links(markup):
    """Keep original source HTML usable from any nested static directory."""
    def attribute(match):
        key, value = match.groups()
        if urlsplit(html.unescape(value)).scheme or value.startswith(("/", "//")):
            return match[0]
        return f'{key}="/{value}"'
    markup = re.sub(r'\b(href|src)="([^"]+)"', attribute, markup)
    def srcset(match):
        return 'srcset="' + ", ".join(
            "/" + part.strip() if not part.strip().startswith(("/", "http"))
            else part.strip() for part in match[1].split(",")
        ) + '"'
    return re.sub(r'srcset="([^"]+)"', srcset, markup)


def service_id(slug):
    return absolute(slug + "/#service")


def graph(path, title, description, *, page_type="WebPage", main_entity=None,
          breadcrumbs=None, extra=None):
    url = absolute(path)
    catalog_id = absolute("services/#catalog")
    nodes = [
        {
            "@type": "Person", "@id": PERSON, "name": NAME,
            "alternateName": "Jean Pierre Boutros", "url": absolute("/"),
            "jobTitle": "International sound engineer, FOH engineer, recording and mixing engineer",
            "description": DESCRIPTION, "email": "jp@jeanpierreboutros.com",
            "telephone": "+9613883863",
            "image": absolute("photos/about-portrait.jpg"),
            "homeLocation": {"@type": "Country", "name": "Lebanon"},
            "sameAs": ["https://www.instagram.com/jp.boutros",
                       "https://www.facebook.com/jean.p.boutros"],
            "knowsAbout": ["Live sound engineering", "Front-of-house mixing",
                          "Monitor engineering", "Concert and festival audio",
                          "Orchestra sound", "Recording and tracking", "Studio mixing",
                          "Mastering", "Broadcast audio", "Audio system integration",
                          "Sound design and post-production"],
            "worksFor": {"@id": SITE + "/#studiojpb"},
            "affiliation": [{"@id": SITE + "/#studiojpb"},
                            {"@id": SITE + "/#zynforge"}],
            "hasOfferCatalog": {"@id": catalog_id},
            "contactPoint": {
                "@type": "ContactPoint", "contactType": "Professional project inquiries",
                "email": "jp@jeanpierreboutros.com", "telephone": "+9613883863",
                "url": absolute("/#contact"), "areaServed": "Worldwide"
            }
        },
        {"@type": "Organization", "@id": SITE + "/#studiojpb",
         "name": "StudioJPB", "alternateName": "Studio Jean-Pierre Boutros",
         "foundingDate": "2008", "founder": {"@id": PERSON},
         "url": absolute("projects/studio-jpb/"),
         "location": {"@type": "Place", "name": "Jounieh, Lebanon",
                      "address": {"@type": "PostalAddress",
                                  "addressLocality": "Jounieh", "addressCountry": "LB"}}},
        {"@type": "Organization", "@id": SITE + "/#zynforge", "name": "Zynforge Audio",
         "founder": {"@id": PERSON}, "url": absolute("/#zynforge")},
        {"@type": "WebSite", "@id": WEBSITE, "url": absolute("/"),
         "name": NAME, "description": DESCRIPTION, "inLanguage": "en",
         "publisher": {"@id": PERSON}},
        {"@type": "OfferCatalog", "@id": catalog_id, "name": "Sound engineering services",
         "url": absolute("services/"),
         "itemListElement": [
             {"@type": "Offer", "itemOffered": {"@id": service_id(s["slug"])}}
             for s in SERVICES
         ]},
    ]
    nodes.extend({
        "@type": "Service", "@id": service_id(s["slug"]),
        "name": s["name"], "serviceType": s["name"], "description": s["intro"],
        "url": absolute(s["slug"] + "/"), "provider": {"@id": PERSON},
        "areaServed": "Worldwide", "isRelatedTo": [
            {"@id": service_id(slug)} for slug in s["related"]
        ]
    } for s in SERVICES)
    page = {
        "@type": page_type, "@id": url + "#webpage", "url": url,
        "name": title, "description": description, "inLanguage": "en",
        "isPartOf": {"@id": WEBSITE}, "about": {"@id": PERSON},
        "dateModified": REVIEWED, "mainEntity": main_entity or {"@id": PERSON}
    }
    if breadcrumbs:
        breadcrumb_id = url + "#breadcrumbs"
        page["breadcrumb"] = {"@id": breadcrumb_id}
        nodes.append({
            "@type": "BreadcrumbList", "@id": breadcrumb_id,
            "itemListElement": [
                {"@type": "ListItem", "position": index, "name": label,
                 "item": {"@id": absolute(item_path)}}
                for index, (label, item_path) in enumerate(breadcrumbs, 1)
            ]
        })
    nodes.append(page)
    nodes.extend(extra or [])
    return {"@context": "https://schema.org", "@graph": nodes}


def page_head(path, title, description, *, image="about-portrait.jpg",
              image_alt="Jean-Pierre Boutros, international sound engineer",
              structured=None, preload_image=None, image_sizes="100vw"):
    manifest = json.loads((ROOT / "photos/optimized/manifest.json").read_text())
    fonts = json.loads((ROOT / "fonts/manifest.json").read_text())
    css_version = sha256((ROOT / "styles.css").read_bytes()).hexdigest()[:12]
    js_version = sha256((ROOT / "main.js").read_bytes()).hexdigest()[:12]
    font_version = sha256((ROOT / "fonts/fonts.css").read_bytes()).hexdigest()[:12]
    font_links = "\n".join(
        f'<link rel="preload" href="{e(font)}" as="font" type="font/woff2" crossorigin />'
        for font in fonts["preload"]
    )
    image_preload = ""
    if preload_image:
        variants = manifest[preload_image]["variants"]
        default = next((v for v in variants if v["width"] >= 960), variants[-1])
        srcset = ", ".join(f'/{v["src"]} {v["width"]}w' for v in variants)
        image_preload = (f'<link rel="preload" as="image" href="/{e(default["src"])}" '
                         f'imagesrcset="{e(srcset)}" imagesizes="{e(image_sizes)}" '
                         'fetchpriority="high" />')
    picture = manifest[image]
    url = absolute(path)
    return f'''<meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}" />
  <meta name="author" content="{NAME}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#0b0b0b" />
  <link rel="canonical" href="{e(url)}" />
  <link rel="icon" type="image/png" href="/favicon.png" />
  <link rel="apple-touch-icon" href="/favicon.png" />
  <meta property="og:type" content="website" />
  <meta property="og:url" content="{e(url)}" />
  <meta property="og:site_name" content="{NAME}" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(description)}" />
  <meta property="og:image" content="{absolute("photos/" + image)}" />
  <meta property="og:image:alt" content="{e(image_alt)}" />
  <meta property="og:image:width" content="{picture["width"]}" />
  <meta property="og:image:height" content="{picture["height"]}" />
  <meta property="og:locale" content="en_US" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{e(title)}" />
  <meta name="twitter:description" content="{e(description)}" />
  <meta name="twitter:image" content="{absolute("photos/" + image)}" />
  <meta name="twitter:image:alt" content="{e(image_alt)}" />
  <script type="application/ld+json">{json_text(structured or graph(path, title, description))}</script>
  {font_links}
{image_preload}
  <link rel="stylesheet" href="/fonts/fonts.css?v={font_version}" />
  <link rel="stylesheet" href="/styles.css?v={css_version}" />
  <script src="/main.js?v={js_version}" defer></script>'''


def faq_html(items, heading="Questions before the project."):
    questions = "".join(
        f'<details><summary>{e(question)}</summary><p>{e(answer)}</p></details>'
        for question, answer in items
    )
    return f'<section class="page-section faq-section"><h2>{e(heading)}</h2><div class="faq-list">{questions}</div></section>'


def service_links():
    return "".join(f'<li><a href="/{s["slug"]}/">{e(s["name"])}</a></li>' for s in SERVICES)


def site_links():
    return f'''<nav class="site-directory container" aria-label="Services and project pages">
  <div><p class="eyebrow">Explore the work</p><a href="/services/">All services</a><a href="/projects/">All project details</a><a href="/studio-credits/">Studio credits</a><a href="/international-projects/">International projects</a></div>
  <ul>{service_links()}</ul>
</nav>'''


def inquiry_html(subject="International audio project"):
    return f'''<section class="page-section page-inquiry" id="inquiry" aria-labelledby="inquiry-title">
  <p class="eyebrow">International project inquiries</p>
  <h2 id="inquiry-title">Tell me about<br /><em>the production.</em></h2>
  <p>{e(AVAILABILITY)}</p>
  <p>Include the service, artist or production, location, dates and technical brief.</p>
  <div class="hero-actions"><a class="btn btn-primary" href="mailto:jp@jeanpierreboutros.com?subject={quote(subject)}">Email Jean-Pierre <span aria-hidden="true">↗</span></a><a class="text-link" href="https://wa.me/9613883863" target="_blank" rel="noopener noreferrer">WhatsApp <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a></div>
</section>'''


def render_search_pages(context):
    home = context["home"]
    images = context["image"]
    project_records = context["projects"]
    by_slug = {p[0]: p for p in project_records}
    article_by_slug = dict(zip(by_slug, context["articles"]))
    cards = context["cards"]
    gallery = context["gallery"]
    sources = context["sources"]
    gallery_data = [dict(photo, src="/" + photo["src"].lstrip("/"))
                    for photo in context["gallery_data"]]
    nav = re.search(r'<nav class="nav".*?</dialog>', home, re.S)[0]
    nav = root_links(nav)
    footer = re.search(r'<footer class="footer.*?</footer>', home, re.S)[0]
    footer = root_links(footer).replace('class="back-top" href="/#top"',
                                      'class="back-top" href="#top"')
    lightbox = re.search(r'<dialog class="lightbox".*?</dialog>', home, re.S)[0]
    motion = re.search(r'<button class="motion-toggle".*?</button>', home, re.S)[0]
    generated = []

    def breadcrumbs_html(items):
        return '<nav class="breadcrumbs" aria-label="Breadcrumb"><ol>' + "".join(
            f'<li><a href="{e(item_path)}">{e(label)}</a></li>'
            if index < len(items) - 1 else f'<li aria-current="page">{e(label)}</li>'
            for index, (label, item_path) in enumerate(items)
        ) + "</ol></nav>"

    def intro(eyebrow, heading, text, breadcrumbs, photo=None, alt="", caption=""):
        image_html = ""
        if photo:
            source = sources.get(photo)
            credit = (f' · <a href="{e(source["url"])}" target="_blank" rel="noopener noreferrer">{e(source["name"])}<span class="sr-only"> (opens in a new tab)</span></a>'
                      if source else "")
            image_html = f'<figure class="page-photo">{root_links(images(photo, alt, sizes="(max-width: 760px) 100vw, 45vw", eager=True))}<figcaption>{e(caption)}{credit}</figcaption></figure>'
        return f'''<header class="page-intro">
  {breadcrumbs_html(breadcrumbs)}
  <div class="{"page-intro-grid" if photo else "page-intro-copy"}"><div><p class="eyebrow">{e(eyebrow)}</p><h1 id="page-title">{heading}</h1><p class="lead">{e(text)}</p><p class="page-availability">{e(AVAILABILITY)}</p></div>{image_html}</div>
</header>'''

    def card(slug):
        markup = root_links(cards[slug])
        # A collection page uses normal links, without homepage filter enhancement.
        return re.sub(r'\sdata-project-card="[^"]+"', "", markup)

    def project_grid(slugs):
        return '<div class="portfolio-grid">' + "".join(card(slug) for slug in slugs) + '</div>'

    def write(path, title, description, body, breadcrumbs, *, image="about-portrait.jpg",
              alt="Jean-Pierre Boutros, international sound engineer", page_type="WebPage",
              main_entity=None, extra=None):
        data = graph(path, title, description, page_type=page_type,
                     main_entity=main_entity, breadcrumbs=breadcrumbs, extra=extra)
        output = ROOT / path.strip("/") / "index.html"
        output.parent.mkdir(parents=True, exist_ok=True)
        head = page_head(path, title, description, image=image, image_alt=alt, structured=data)
        document = f'''<!DOCTYPE html>
<html lang="en">
<head>{head}</head>
<body id="top" tabindex="-1">
  <a class="skip-link" href="#main">Skip to content</a><div class="progress" aria-hidden="true"></div>
  {nav}
  <main id="main" tabindex="-1" class="detail-page container">{body}</main>
  {site_links()}
  {footer}
  {motion}
  {lightbox}
  <script type="application/json" id="gallery-data">{json_text(gallery_data)}</script>
</body>
</html>
'''
        output.write_text(document, encoding="utf-8")
        generated.append(path)

    # Each distinct service has a complete, visible HTML explanation and examples.
    for service in SERVICES:
        slug = service["slug"]
        path = "/" + slug + "/"
        crumbs = [("Home", "/"), ("Services", "/services/"), (service["name"], path)]
        body = intro(service["name"], service["h1"], service["intro"], crumbs,
                     service["photo"], service["alt"], service["caption"])
        for heading, paragraphs in service["sections"]:
            body += f'<section class="page-section"><h2>{e(heading)}</h2>' + "".join(
                f'<p>{e(paragraph)}</p>' for paragraph in paragraphs) + '</section>'
        body += '<section class="page-section page-brief"><div><h2>Engineering areas</h2><ul>' + "".join(
            f'<li>{e(item)}</li>' for item in service["capabilities"]
        ) + '</ul></div><div><h2>For your technical brief</h2><ul>' + "".join(
            f'<li>{e(item)}</li>' for item in service["brief"]
        ) + '</ul></div></section>'
        body += '<section class="page-section"><h2>Selected experience</h2>' + project_grid(service["projects"]) + '</section>'
        if slug in ("recording-engineer", "mixing-mastering"):
            body += '<section class="page-section"><h2>Released recordings</h2><p>Explore Jean-Pierre Boutros’s recording, mixing and mastering credits by song and album.</p><a class="text-link" href="/studio-credits/">Browse studio credits <span aria-hidden="true">↗</span></a></section>'
        body += faq_html(service["faq"])
        body += '<section class="page-section"><h2>Related services</h2><ul class="related-links">' + "".join(
            f'<li><a href="/{key}/">{e(SERVICE_BY_SLUG[key]["name"])}</a></li>'
            for key in service["related"]
        ) + '<li><a href="/international-projects/">International projects & availability</a></li></ul></section>'
        body += inquiry_html(service["name"] + " inquiry")
        write(path, service["title"], service["description"], body, crumbs,
              image=service["photo"], alt=service["alt"],
              main_entity={"@id": service_id(slug)})

    # Preserve every full project description, with a genuinely indexable URL.
    orchestra_projects = {"marina-viotti", "cartoon-orchestra", "al-sharq-symphony",
                          "abeer-nehme-qatar", "lebanese-philharmonic-diman", "marcel-khalife-baalbeck"}
    for project in project_records:
        slug, name, production, location, role, category, photo, featured = project
        path = f"/projects/{slug}/"
        filename = gallery[photo][0] if isinstance(photo, int) else photo
        alt = gallery[photo][2] if isinstance(photo, int) else "Studio mixing console and audio equipment"
        article = article_by_slug[slug]
        summary = next((plain(p) for p in re.findall(r'<p(?! class="project-index")[^>]*>(.*?)</p>', article, re.S)
                        if len(plain(p)) > 70), f"{role} · {production} · {location}")
        title = f"{name} · {production} | {role} | {NAME}"
        description = f"{NAME}: {role.lower()} for {name}. {production}. {location}. Project details, photographs and related sound engineering services."
        crumbs = [("Home", "/"), ("Projects", "/projects/"), (name + " · " + production, path)]
        body = intro(role + " · " + location, e(name) + "<br /><em>" + e(production) + "</em>",
                     summary, crumbs)
        article = re.sub(r'\sdata-reveal(?:="[^"]*")?', "", article)
        article = re.sub(r'<h3(\s[^>]*)?>', lambda m: '<h2' + (m[1] or '') + '>', article).replace("</h3>", "</h2>")
        article = root_links(article)
        if "<img" not in article:
            article = f'<figure class="page-photo project-system-photo">{root_links(images(filename, alt, sizes="100vw"))}<figcaption>Studio work · Audio equipment and workflow</figcaption></figure>' + article
        body += '<section class="project-page-record" aria-label="Project record">' + article + '</section>'
        related_services = (["orchestra-sound-engineer", "live-sound-engineer"] if slug in orchestra_projects
                            else ["broadcast-audio-engineer"] if category == "broadcast"
                            else ["studio-system-integration"] if slug == "studio-integration"
                            else ["recording-engineer", "mixing-mastering"] if slug == "studio-jpb"
                            else ["live-sound-engineer", "recording-engineer"] if slug == "marcel-khalife-amman"
                            else ["mixing-mastering"] if slug == "carole-samaha-golden-album"
                            else ["live-sound-engineer"])
        body += '<section class="page-section"><h2>Engineering services</h2><ul class="related-links">' + "".join(
            f'<li><a href="/{key}/">{e(SERVICE_BY_SLUG[key]["name"])}</a></li>'
            for key in related_services
        ) + '</ul><p class="record-provenance">Engineering role confirmed by Jean-Pierre Boutros. Linked production coverage provides event context.</p></section>'
        related_projects = [p[0] for p in project_records if p[5] == category and p[0] != slug][:2]
        if related_projects:
            body += '<section class="page-section"><h2>More from the portfolio</h2>' + project_grid(related_projects) + '</section>'
        body += inquiry_html(name + " / similar production inquiry")
        article_id = absolute(path + "#record")
        image_data = {"@type": "ImageObject", "contentUrl": absolute("photos/" + filename),
                      "caption": alt}
        if filename in sources:
            image_data["creditText"] = sources[filename]["name"]
        record = {
            "@type": "Article", "@id": article_id, "headline": name + " · " + production,
            "description": summary, "articleBody": plain(article),
            "author": {"@id": PERSON}, "publisher": {"@id": PERSON},
            "mainEntityOfPage": {"@id": absolute(path + "#webpage")},
            "inLanguage": "en", "dateModified": REVIEWED, "image": image_data,
            "about": [{"@id": service_id(key)} for key in related_services]
        }
        write(path, title, description, body, crumbs, image=filename, alt=alt,
              main_entity={"@id": article_id}, extra=[record])

    # Index pages expose the complete inventory without a filter or modal.
    path = "/projects/"
    crumbs = [("Home", "/"), ("Projects", path)]
    body = intro("Professional portfolio", "The projects.<br /><em>The actual role.</em>",
                 f"Explore all {len(project_records)} project records: concert and festival FOH, artist monitors, live recording, orchestral performances, broadcast, StudioJPB and audio system integration.",
                 crumbs)
    body += project_grid([p[0] for p in project_records])
    body += inquiry_html()
    item_list = {"@type": "ItemList", "@id": absolute(path + "#projects"),
                 "name": "Professional project records", "numberOfItems": len(project_records),
                 "itemListElement": [
                     {"@type": "ListItem", "position": i, "name": p[1] + " · " + p[2],
                      "url": absolute("projects/" + p[0] + "/")}
                     for i, p in enumerate(project_records, 1)
                 ]}
    write(path, "Sound Engineering Projects | Jean-Pierre Boutros",
          "Explore Jean-Pierre Boutros’s documented FOH, monitor, orchestral, broadcast and studio work, with the actual role, dates, venues and production sources.",
          body, crumbs, page_type="CollectionPage",
          main_entity={"@id": item_list["@id"]}, extra=[item_list])

    path = "/services/"
    crumbs = [("Home", "/"), ("Services", path)]
    body = intro("Sound engineering services", "From the stage<br /><em>to the studio.</em>",
                 DESCRIPTION, crumbs)
    body += '<section class="page-section"><h2>Choose the work you need</h2><div class="service-directory">' + "".join(
        f'<article><h3><a href="/{s["slug"]}/">{e(s["name"])}</a></h3><p>{e(s["intro"])}</p><a class="text-link" href="/{s["slug"]}/">Explore {e(s["name"].lower())} <span aria-hidden="true">↗</span></a></article>'
        for s in SERVICES
    ) + '</div></section>'
    body += faq_html(HOME_FAQ) + inquiry_html()
    write(path, "International Sound Engineering Services | Jean-Pierre Boutros",
          "Live sound, FOH, orchestral mixing, recording, mastering, broadcast and studio integration with Jean-Pierre Boutros. Lebanon-based; worldwide inquiries welcome.",
          body, crumbs, page_type="CollectionPage",
          main_entity={"@id": absolute("services/#catalog")})

    path = "/studio-credits/"
    crumbs = [("Home", "/"), ("Studio credits", path)]
    body = intro("Songs & albums", "On record.<br /><em>Behind the music.</em>",
                 "Jean-Pierre Boutros’s recording, mixing and mastering credits, by song and album.", crumbs)
    body += studio_groups_html() + inquiry_html("Recording / mixing / mastering inquiry")
    works = [(group, work) for group in CREDIT_GROUPS for work in group["works"]]
    item_list = {"@type": "ItemList", "@id": absolute(path + "#credits"),
                 "name": "Recording, mixing and mastering credits", "numberOfItems": len(works),
                 "itemListElement": [
                     {"@type": "ListItem", "position": index, "name": group["name"] + " · " + work["title"] + " · " + work["role"],
                      "url": work.get("url", absolute(path + "#" + group["id"]))}
                     for index, (group, work) in enumerate(works, 1)]}
    write(path, "Recording, Mixing & Mastering Credits | Jean-Pierre Boutros",
          "Explore Jean-Pierre Boutros and StudioJPB recording, mixing and mastering credits for songs and albums by Nancy Ajram, Carole Samaha, Abeer Nehme and more.",
          body, crumbs, page_type="CollectionPage", main_entity={"@id": absolute(path + "#credits")}, extra=[item_list])

    path = "/international-projects/"
    crumbs = [("Home", "/"), ("International projects", path)]
    body = intro("Lebanon-based · Worldwide", "Different stages.<br /><em>The same attention.</em>",
                 "Jean-Pierre Boutros is based in Lebanon and welcomes international concert, festival, touring, recording, mixing, broadcast and studio integration inquiries. Travel and project details are agreed directly.",
                 crumbs)
    regions = [
        ("France", ["nancy-ajram-olympia"]),
        ("Oman", ["marcel-khalife-muscat"]),
        ("Jordan", ["marcel-khalife-amman", "zade-dirani-amman"]),
        ("Qatar", ["abeer-nehme-qatar"]),
        ("Kuwait", ["the-eighties", "cartoon-orchestra"]),
        ("Saudi Arabia", ["baligh-hamdi-night", "warda-night", "night-of-arab-stars"]),
        ("United Arab Emirates", ["nancy-ajram-expo-dubai"]),
        ("Turkey", ["al-sharq-symphony"]),
        ("Lebanon", ["beirut-the-sea-lover", "mazeej-ndu", "nancy-ajram-jounieh", "marcel-khalife-baalbeck", "zade-dirani-dbayeh", "beiteddine-marco-polo", "abeer-nehme-baalbeck", "marina-viotti", "lebanese-philharmonic-diman",
                     "ehdeniyat-abeer-nehme", "ehdeniyat-al-shami", "ehdeniyat-adam",
                     "papal-broadcast", "studio-jpb"]),
    ]
    body += '<section class="page-section"><h2>Locations in the documented portfolio</h2><p>These are locations of named projects. Worldwide availability is discussed for each new engagement.</p><div class="international-list">'
    for country, slugs in regions:
        body += f'<section><h3>{e(country)}</h3><ul>' + "".join(
            f'<li><a href="/projects/{slug}/">{e(by_slug[slug][1])} · {e(by_slug[slug][2])}</a><span>{e(by_slug[slug][4])} · {e(by_slug[slug][3])}</span></li>'
            for slug in slugs
        ) + '</ul></section>'
    body += '</div><p>Studio integration work also includes <a href="/projects/studio-integration/">Merwas Studios in Riyadh and Playsound Studios in Lebanon</a>.</p></section>'
    body += '<section class="page-section"><h2>Planning an international engagement</h2><p>Send the artist or production, service, city and country, rehearsal and performance dates, and available technical brief. Identify your production contact and the responsibilities of the local venue or crew. Availability, travel arrangements and deliverables are confirmed for the engagement.</p><p>Clients in Europe, the Americas, the Middle East, Africa, Asia and Oceania are welcome to inquire. The professional home base remains Lebanon.</p></section>'
    body += faq_html(HOME_FAQ) + inquiry_html()
    write(path, "International Sound Engineer & Projects | Jean-Pierre Boutros",
          "Lebanon-based sound engineer Jean-Pierre Boutros is available worldwide by arrangement. Explore documented projects in Europe and the Middle East and contact him.",
          body, crumbs, page_type="CollectionPage")

    # Only canonical, real HTML pages; the date reflects this content review.
    paths = ["/"] + sorted(generated)
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", namespace)
    sitemap = ET.Element("{" + namespace + "}urlset")
    for path in paths:
        entry = ET.SubElement(sitemap, "{" + namespace + "}url")
        ET.SubElement(entry, "{" + namespace + "}loc").text = absolute(path)
        ET.SubElement(entry, "{" + namespace + "}lastmod").text = REVIEWED
    ET.indent(sitemap, space="  ")
    (ROOT / "sitemap.xml").write_bytes(ET.tostring(sitemap, encoding="utf-8", xml_declaration=True) + b"\n")
    (ROOT / "robots.txt").write_text(f'''# Search discovery and model-training controls are separate.
User-agent: Googlebot
User-agent: bingbot
User-agent: OAI-SearchBot
User-agent: PerplexityBot
Allow: /

# Owner preference: exclude OpenAI model-training crawl; search remains allowed.
User-agent: GPTBot
Disallow: /

# Preserve existing access for other crawlers; this is not a security boundary.
User-agent: *
Allow: /

Sitemap: {SITE}/sitemap.xml
''')
    directory = [
        "# Jean-Pierre Boutros", "",
        "> Lebanon-based international sound engineer. FOH, monitors, recording, mixing, mastering, broadcast and audio system integration. Worldwide projects and travel by arrangement.",
        "", "Professional name: Jean-Pierre Boutros (also written Jean Pierre Boutros).",
        "Contact: jp@jeanpierreboutros.com · WhatsApp +961 3 883 863.",
        "", "## Main pages",
        f"- [Professional profile]({SITE}/): Biography, collaborations, portfolio and contact.",
        f"- [Services]({SITE}/services/): The six documented service areas.",
        f"- [Project records]({SITE}/projects/): All {len(project_records)} projects with role, context and sources.",
        f"- [Studio credits]({SITE}/studio-credits/): Jean-Pierre Boutros’s recording, mixing and mastering roles for released songs and albums.",
        f"- [International projects]({SITE}/international-projects/): Locations of documented work and worldwide availability.",
        "", "## Services",
    ]
    directory.extend(f'- [{s["name"]}]({SITE}/{s["slug"]}/): {s["intro"]}' for s in SERVICES)
    directory.extend(["", "## Project records"])
    directory.extend(f'- [{p[1]} · {p[2]}]({SITE}/projects/{p[0]}/): {p[4]}; {p[3]}.' for p in project_records)
    directory.extend(["", "## Notes",
                      "This is a supplementary directory of public pages, not an indexing requirement.",
                      "Production roles are supplied by Jean-Pierre; linked coverage supports event context.",
                      "English is the maintained website language. No translated site versions are currently published.", ""])
    (ROOT / "llms.txt").write_text("\n".join(directory), encoding="utf-8")
    return paths
