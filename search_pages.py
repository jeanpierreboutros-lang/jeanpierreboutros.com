"""Static search landing pages, shared metadata and connected Schema.org entities."""
import html
import json
import re
from hashlib import sha256
from functools import lru_cache
from pathlib import Path
from urllib.parse import quote, urlsplit
from xml.etree import ElementTree as ET

from services import AVAILABILITY, HOME_FAQ, REVIEWED, SERVICES, SERVICE_BY_SLUG
from studio_credits import CREDIT_GROUPS, studio_groups_html
from measurement import measurement_head, measurement_markup
from seo_content import CASE_STUDIES, PRODUCTS, PROJECT_METADATA

ROOT = Path(__file__).resolve().parent
SITE = "https://www.jeanpierreboutros.com"
NAME = "Jean-Pierre Boutros"
PERSON = SITE + "/#person"
WEBSITE = SITE + "/#website"
DESCRIPTION = ("Lebanon-based international sound engineer Jean-Pierre Boutros: "
               "FOH for concerts and festivals, recording, mixing, mastering, broadcast "
               "and studio integration. Available worldwide by arrangement.")
HOME_DESCRIPTION = ("Jean-Pierre Boutros: Lebanon-based FOH, live, orchestra, recording and mixing "
                    "engineer, and audio software developer. Available for worldwide projects.")
e = html.escape
PAGE_REVIEW_DATES = {
    path: "2026-11-16" for path in (
        "/", "/projects/", "/projects/tarteeb-shareet-doha/",
        "/live-sound-engineer/", "/international-projects/",
    )
}
PAGE_REVIEW_DATES.update({
    path: "2026-11-23" for path in (
        "/", "/projects/", "/projects/ry-x-qatar-philharmonic-doha/",
        "/live-sound-engineer/", "/orchestra-sound-engineer/", "/international-projects/",
    )
})
# Shared identity and metadata reviewed in this release. This is deliberately
# fixed, rather than a build timestamp. Production dates remain unchanged.
PAGE_REVIEW_DATES.update({path: "2026-11-24" for path in (
    "/", "/services/", "/projects/", "/international-projects/", "/studio-credits/",
    "/audio-software-developer/", *("/" + s["slug"] + "/" for s in SERVICES),
    *("/projects/" + slug + "/" for slug in PROJECT_METADATA),
)})


def absolute(path):
    return SITE + "/" + path.lstrip("/")


@lru_cache(maxsize=None)
def asset_url(path):
    """Version local image URLs so immutable caching cannot retain stale images."""
    return path + "?v=" + sha256((ROOT / path).read_bytes()).hexdigest()[:12]


def json_text(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def search_image(filename):
    """Reuse the full-composition derivative; retain every original photograph."""
    manifest = json.loads((ROOT / "photos/optimized/manifest.json").read_text())
    return manifest[filename]["variants"][-1]


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
            "jobTitle": "International sound engineer, FOH engineer, recording and mixing engineer, audio software developer",
            "description": DESCRIPTION, "email": "jp@jeanpierreboutros.com",
            "telephone": "+9613883863",
            "image": absolute(asset_url(search_image("about-portrait.jpg")["src"])),
            "homeLocation": {"@type": "Country", "name": "Lebanon"},
            "sameAs": ["https://www.instagram.com/jp.boutros",
                       "https://www.facebook.com/jean.p.boutros",
                       "https://x.com/JPbboutros",
                       "https://www.linkedin.com/in/jeanpierreboutros/"],
            "knowsAbout": ["Live sound engineering", "Front-of-house mixing",
                          "Monitor engineering", "Concert and festival audio",
                          "Orchestra sound", "Recording and tracking", "Studio mixing",
                          "Mastering", "Broadcast audio", "Audio system integration",
                          "Sound design and post-production", "Audio software development"],
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
         "founder": {"@id": PERSON}, "url": absolute("audio-software-developer/")},
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
        "dateModified": PAGE_REVIEW_DATES.get(path, REVIEWED), "mainEntity": main_entity or {"@id": PERSON}
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
              structured=None, preload_image=None, image_sizes="100vw", og_type="website"):
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
        srcset = ", ".join(f'/{asset_url(v["src"])} {v["width"]}w' for v in variants)
        image_preload = (f'<link rel="preload" as="image" href="/{e(asset_url(default["src"]))}" '
                         f'imagesrcset="{e(srcset)}" imagesizes="{e(image_sizes)}" '
                         'fetchpriority="high" />')
    picture = search_image(image)
    picture_url = absolute(asset_url(picture["src"]))
    url = absolute(path)
    return f'''<meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{e(title)}</title>
  <meta name="description" content="{e(description)}" />
  <meta name="author" content="{NAME}" />
  <meta name="robots" content="index, follow, max-image-preview:large" />
  <meta name="theme-color" content="#191e1c" />
  <link rel="canonical" href="{e(url)}" />
  <link rel="icon" type="image/png" href="/{asset_url('favicon.png')}" />
  <link rel="apple-touch-icon" href="/favicon.png" />
  <meta property="og:type" content="{e(og_type)}" />
  <meta property="og:url" content="{e(url)}" />
  <meta property="og:site_name" content="{NAME}" />
  <meta property="og:title" content="{e(title)}" />
  <meta property="og:description" content="{e(description)}" />
  <meta property="og:image" content="{picture_url}" />
  <meta property="og:image:type" content="image/webp" />
  <meta property="og:image:alt" content="{e(image_alt)}" />
  <meta property="og:image:width" content="{picture["width"]}" />
  <meta property="og:image:height" content="{picture["height"]}" />
  <meta property="og:locale" content="en_US" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:title" content="{e(title)}" />
  <meta name="twitter:description" content="{e(description)}" />
  <meta name="twitter:image" content="{picture_url}" />
  <meta name="twitter:image:alt" content="{e(image_alt)}" />
  <script type="application/ld+json">{json_text(structured or graph(path, title, description))}</script>
  {font_links}
{image_preload}
  <link rel="stylesheet" href="/fonts/fonts.css?v={font_version}" />
  <link rel="stylesheet" href="/styles.css?v={css_version}" />
  <script src="/main.js?v={js_version}" defer></script>
  {measurement_head()}'''


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
  <div><p class="eyebrow">Explore the work</p><a href="/services/">All services</a><a href="/projects/">All project details</a><a href="/studio-credits/">Studio credits</a><a href="/international-projects/">International projects</a><a href="/audio-software-developer/">Zynforge audio software</a></div>
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
    article_by_slug = dict(zip((p[0] for p in project_records), context["articles"]))
    project_records = sorted(project_records, key=lambda p: context["project_order"].index(p[0]))
    by_slug = {p[0]: p for p in project_records}
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

    def project_grid(slugs, *, group_years=False):
        slugs = sorted(slugs, key=context["project_order"].index)
        markup, previous_year = [], None
        for slug in slugs:
            year = context["project_years"][slug]
            if group_years and year != previous_year:
                label = "Studio & systems" if year == "ongoing" else year
                markup.append(f'<h2 class="portfolio-year">{e(label)}</h2>')
                previous_year = year
            markup.append(card(slug))
        return '<div class="portfolio-grid">' + ''.join(markup) + '</div>'

    def write(path, title, description, body, breadcrumbs, *, image="about-portrait.jpg",
              alt="Jean-Pierre Boutros, international sound engineer", page_type="WebPage",
              main_entity=None, extra=None, preload_image=None, og_type="website"):
        data = graph(path, title, description, page_type=page_type,
                     main_entity=main_entity, breadcrumbs=breadcrumbs, extra=extra)
        output = ROOT / path.strip("/") / "index.html"
        output.parent.mkdir(parents=True, exist_ok=True)
        head = page_head(path, title, description, image=image, image_alt=alt, structured=data,
                         preload_image=preload_image,
                         image_sizes="(max-width: 760px) 100vw, 45vw", og_type=og_type)
        document = f'''<!DOCTYPE html>
<html lang="en">
<head>{head}</head>
<body id="top" tabindex="-1">
  <a class="skip-link" href="#main">Skip to content</a><div class="progress" aria-hidden="true"></div>
  {nav}
  <main id="main" tabindex="-1" class="detail-page container">{body}</main>
  {site_links()}
  {footer}
  {measurement_markup()}
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
            body += '<section class="page-section"><h2>Released recordings</h2><p>Named releases show the specific engineering work behind the service:</p><ul class="related-links">'
            for group_id, work_title in service["credit_examples"]:
                group = next(g for g in CREDIT_GROUPS if g["id"] == group_id)
                work = next(w for w in group["works"] if w["title"] == work_title)
                body += (f'<li><a href="/studio-credits/#{e(group_id)}">'
                         f'{e(group["name"])} · {e(work_title)} · {e(work["role"])}</a></li>')
            body += '</ul><a class="text-link" href="/studio-credits/">Browse all studio credits <span aria-hidden="true">↗</span></a></section>'
        body += faq_html(service["faq"])
        body += '<section class="page-section"><h2>Related services</h2><ul class="related-links">' + "".join(
            f'<li><a href="/{key}/">{e(SERVICE_BY_SLUG[key]["name"])}</a></li>'
            for key in service["related"]
        ) + '<li><a href="/international-projects/">International projects & availability</a></li></ul></section>'
        if slug in ("recording-engineer", "studio-system-integration", "live-sound-engineer"):
            body += '<p><a class="text-link" href="/audio-software-developer/">Explore Jean-Pierre’s Zynforge audio software <span aria-hidden="true">↗</span></a></p>'
        body += inquiry_html(service["name"] + " inquiry")
        write(path, service["title"], service["description"], body, crumbs,
              image=service["photo"], alt=service["alt"],
              main_entity={"@id": service_id(slug)}, preload_image=service["photo"])

    # Preserve every full project description, with a genuinely indexable URL.
    orchestra_projects = {"ry-x-qatar-philharmonic-doha", "marina-viotti", "cartoon-orchestra", "al-sharq-symphony",
                          "abeer-nehme-qatar", "lebanese-philharmonic-diman", "marcel-khalife-baalbeck"}
    for project in project_records:
        slug, name, production, location, role, category, photo, featured = project
        path = f"/projects/{slug}/"
        filename = gallery[photo][0] if isinstance(photo, int) else photo
        alt = next((entry[2] for entry in gallery if entry[0] == filename),
                   "Studio audio equipment used in Jean-Pierre Boutros’s engineering work")
        article = article_by_slug[slug]
        summary = next((plain(p) for p in re.findall(r'<p(?! class="project-index")[^>]*>(.*?)</p>', article, re.S)
                        if len(plain(p)) > 70), f"{role} · {production} · {location}")
        title, description = PROJECT_METADATA[slug]
        crumbs = [("Home", "/"), ("Projects", "/projects/"), (name + " · " + production, path)]
        body = intro(role + " · " + location, e(name) + "<br /><em>" + e(production) + "</em>",
                     summary, crumbs)
        article = re.sub(r'\sdata-reveal(?:="[^"]*")?', "", article)
        article = re.sub(r'<h3(\s[^>]*)?>', lambda m: '<h2' + (m[1] or '') + '>', article).replace("</h3>", "</h2>")
        article = root_links(article)
        if slug in CASE_STUDIES:
            heading, context_text, brief = CASE_STUDIES[slug]
            article += (f'<section class="page-section"><h2>{e(heading)}</h2>'
                        f'<p>{e(context_text)}</p><h3>Planning a comparable production</h3>'
                        f'<p>{e(brief)}</p></section>')
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
        if slug == "studio-jpb":
            body += '<section class="page-section"><h2>Selected released engineering work</h2><ul class="related-links">'
            for group_id, work_title in [("nancy-ajram", "Warana Eh"), ("nancy-ajram", "Men Nazra"),
                                         ("carole-samaha", "Golden Album")]:
                group = next(g for g in CREDIT_GROUPS if g["id"] == group_id)
                work = next(w for w in group["works"] if w["title"] == work_title)
                body += (f'<li><a href="/studio-credits/#{e(group_id)}">'
                         f'{e(group["name"])} · {e(work_title)} · {e(work["role"])}</a></li>')
            body += '</ul></section>'
        related_by_project = {
            "nancy-ajram-olympia": ["baligh-hamdi-night", "warda-night"],
            "marcel-khalife-amman": ["marcel-khalife-muscat", "marcel-khalife-baalbeck"],
            "studio-jpb": ["carole-samaha-golden-album", "marcel-khalife-amman"],
        }
        related_projects = related_by_project.get(slug,
            [p[0] for p in project_records if p[5] == category and p[0] != slug][:2])
        if related_projects:
            body += '<section class="page-section"><h2>More from the portfolio</h2>' + project_grid(related_projects) + '</section>'
        body += inquiry_html(name + " / similar production inquiry")
        article_id = absolute(path + "#record")
        picture = search_image(filename)
        image_data = {"@type": "ImageObject", "contentUrl": absolute(asset_url(picture["src"])),
                      "caption": alt}
        if filename in sources:
            image_data["creditText"] = sources[filename]["name"]
        record = {
            "@type": "Article", "@id": article_id, "headline": name + " · " + production,
            "description": summary, "articleBody": plain(article),
            "author": {"@id": PERSON}, "publisher": {"@id": PERSON},
            "mainEntityOfPage": {"@id": absolute(path + "#webpage")},
            "inLanguage": "en", "dateModified": PAGE_REVIEW_DATES.get(path, REVIEWED), "image": image_data,
            "about": [{"@id": service_id(key)} for key in related_services]
        }
        if slug in context["project_dates"]:
            # This is the production date, never an invented article-publication date.
            record["temporalCoverage"] = context["project_dates"][slug][0]
        write(path, title, description, body, crumbs, image=filename, alt=alt,
              main_entity={"@id": article_id}, extra=[record], og_type="article")

    # Index pages expose the complete inventory without a filter or modal.
    path = "/projects/"
    crumbs = [("Home", "/"), ("Projects", path)]
    body = intro("Professional portfolio", "The projects.<br /><em>The actual role.</em>",
                 f"Explore all {len(project_records)} project records: concert and festival FOH, artist monitors, live recording, orchestral performances, broadcast, StudioJPB and audio system integration.",
                 crumbs)
    body += '<p class="portfolio-order"><span>By year</span><span>Newest first ↓</span></p>'
    body += project_grid([p[0] for p in project_records], group_years=True)
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
        ("Qatar", ["ry-x-qatar-philharmonic-doha", "tarteeb-shareet-doha", "abeer-nehme-qatar"]),
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
    body += '<section class="page-section"><h2>Planning an international engagement</h2><p>Send the artist or production, service, city and country, rehearsal and performance dates, and available technical brief. Identify your production contact and the responsibilities of the local venue or crew. Availability, travel arrangements and deliverables are confirmed for the engagement.</p><p>Inquiries are welcome from Lebanon, Qatar, Kuwait, the United Arab Emirates (UAE), Saudi Arabia, Europe, North America and worldwide. The professional home base remains Lebanon; project locations above describe past engagements.</p><p>Explore <a href="/services/">sound engineering services</a>, the <a href="/#about">professional biography</a> and <a href="/audio-software-developer/">Zynforge audio software</a> to choose the relevant area of work.</p></section>'
    body += faq_html(HOME_FAQ) + inquiry_html()
    write(path, "International Sound Engineer & Projects | Jean-Pierre Boutros",
          "Lebanon-based sound engineer Jean-Pierre Boutros is available worldwide by arrangement. Explore documented projects in Europe and the Middle East and contact him.",
          body, crumbs, page_type="CollectionPage")

    path = "/audio-software-developer/"
    crumbs = [("Home", "/"), ("Audio software", path)]
    body = intro("Jean-Pierre Boutros · Zynforge Audio", "Audio software.<br /><em>Built from the work.</em>",
                 "Jean-Pierre Boutros is a sound engineer and audio software developer based in Lebanon. Through Zynforge Audio, he builds tools for live performance, recording and production planning.", crumbs)
    body += '<section class="page-section"><h2>From engineering practice to audio tools</h2><p>Jean-Pierre’s work spans front-of-house and monitor engineering, recording, mixing and studio system integration. Alongside StudioJPB, which he founded in 2008, Zynforge Audio connects his software development with practical stage and studio production requirements.</p><p>Explore the <a href="/projects/">professional project records</a>, <a href="/recording-engineer/">recording practice</a> and <a href="/studio-system-integration/">studio integration experience</a> behind this work.</p></section>'
    applications = []
    for product_slug, filename, name, category, description in PRODUCTS:
        body += (f'<section class="page-section" id="{product_slug}"><p class="eyebrow">{e(category)}</p>'
                 f'<h2>{e(name)}</h2>{root_links(images(filename, name + " application icon", css="zyn-icon", sizes="64px"))}'
                 f'<p>{e(description)}</p></section>')
        applications.append({"@type": "SoftwareApplication", "@id": absolute(path + "#" + product_slug),
                             "name": name, "description": description, "applicationCategory": "MultimediaApplication",
                             "url": absolute(path + "#" + product_slug), "creator": {"@id": PERSON},
                             "publisher": {"@id": SITE + "/#zynforge"}})
    body += '<section class="page-section"><h2>Discuss the tools and your production</h2><p>For current availability, compatibility and product details, contact Jean-Pierre and identify the Zynforge tool you are interested in. For engineering work, include your production, venue, country, dates and required role.</p><p><a href="/live-sound-engineer/">Live sound and FOH engineering</a> · <a href="/recording-engineer/">Recording and tracking</a> · <a href="/#about">About Jean-Pierre</a></p></section>'
    body += inquiry_html("Zynforge Audio product inquiry")
    software_list = {"@type": "ItemList", "@id": absolute(path + "#tools"),
                     "name": "Zynforge Audio tools", "numberOfItems": len(applications),
                     "itemListElement": [{"@type": "ListItem", "position": i, "item": {"@id": app["@id"]}}
                                         for i, app in enumerate(applications, 1)]}
    write(path, "Audio Software Developer & Zynforge | Jean-Pierre Boutros",
          "Jean-Pierre Boutros develops Zynforge Audio tools for live performance, multitrack recording and stage planning. Explore the software and engineering background.",
          body, crumbs, main_entity={"@id": software_list["@id"]}, extra=[software_list, *applications])

    # Only canonical, real HTML pages; the date reflects this content review.
    paths = ["/"] + sorted(generated)
    namespace = "http://www.sitemaps.org/schemas/sitemap/0.9"
    ET.register_namespace("", namespace)
    sitemap = ET.Element("{" + namespace + "}urlset")
    for path in paths:
        entry = ET.SubElement(sitemap, "{" + namespace + "}url")
        ET.SubElement(entry, "{" + namespace + "}loc").text = absolute(path)
        ET.SubElement(entry, "{" + namespace + "}lastmod").text = PAGE_REVIEW_DATES.get(path, REVIEWED)
    ET.indent(sitemap, space="  ")
    (ROOT / "sitemap.xml").write_bytes(ET.tostring(sitemap, encoding="utf-8", xml_declaration=True) + b"\n")
    (ROOT / "robots.txt").write_text(f'''# Search discovery and model-training controls are separate.
User-agent: Googlebot
User-agent: bingbot
User-agent: OAI-SearchBot
User-agent: Claude-SearchBot
User-agent: PerplexityBot
Allow: /

# Fetching public pages in response to an AI user's request.
User-agent: ChatGPT-User
User-agent: Claude-User
User-agent: Perplexity-User
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
        f"- [Audio software developer and Zynforge]({SITE}/audio-software-developer/): Jean-Pierre’s software work and three audio production tools.",
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
