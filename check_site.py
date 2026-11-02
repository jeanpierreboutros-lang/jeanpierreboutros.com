#!/usr/bin/env python3
"""Dependency-free checks for the static URL inventory, metadata and graph.

Optional --vocabulary PATH checks types, properties, domains and ranges against
the official Schema.org JSON-LD vocabulary, without a network call during tests.
"""
import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit
from urllib.robotparser import RobotFileParser
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
SITE = "https://www.jeanpierreboutros.com"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__(convert_charrefs=True)
        self.ids = []
        self.refs = []
        self.meta = {}
        self.canonical = []
        self.titles = []
        self.h1 = 0
        self.json = []
        self.labels = []
        self.cards = []
        self.dialogs = []
        self.gallery_links = []
        self.images = []
        self.downloads = []
        self.mode = None
        self.buffer = []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        self.labels.extend(a.get("aria-labelledby", "").split())
        self.labels.extend(a.get("aria-controls", "").split())
        if tag == "meta":
            self.meta[a.get("name", a.get("property"))] = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical":
            self.canonical.append(a["href"])
        if tag == "h1":
            self.h1 += 1
        for attr in ("href", "src"):
            if a.get(attr):
                self.refs.append(a[attr])
        if "srcset" in a:
            self.refs.extend(part.strip().split()[0] for part in a["srcset"].split(","))
        if tag == "img" and "src" in a:
            self.images.append(a)
        if "download" in a:
            self.downloads.append(a["href"])
        if "data-project-card" in a:
            self.cards.append(a)
        if "data-project-dialog" in a:
            self.dialogs.append(a)
        if "data-gallery-index" in a:
            self.gallery_links.append(a)
        if tag == "title":
            self.mode, self.buffer = "title", []
        if tag == "script" and a.get("type") in ("application/ld+json", "application/json"):
            self.mode, self.buffer = a["type"], []

    def handle_data(self, data):
        if self.mode:
            self.buffer.append(data)

    def handle_endtag(self, tag):
        if tag not in ("title", "script") or not self.mode:
            return
        value = "".join(self.buffer)
        if self.mode == "title":
            self.titles.append(value)
        elif self.mode == "application/ld+json":
            self.json.append(json.loads(value))
        self.mode, self.buffer = None, []


def local_target(ref, source):
    url = urlsplit(ref)
    if url.scheme and (url.scheme != "https" or url.netloc not in
                       ("www.jeanpierreboutros.com", "jeanpierreboutros.com")):
        return None
    if url.netloc and url.netloc not in ("www.jeanpierreboutros.com", "jeanpierreboutros.com"):
        return None
    path = unquote(url.path)
    target = (ROOT / path.lstrip("/")) if path.startswith("/") else source.parent / path
    if not path:
        target = source
    if target.is_dir():
        target = target / "index.html"
    return target, unquote(url.fragment)


def vocabulary_check(documents, path):
    vocabulary = json.loads(Path(path).read_text())
    def name(value):
        return value.replace("https://schema.org/", "").replace("http://schema.org/", "").replace("schema:", "")
    definitions = {name(item["@id"]): item for item in vocabulary["@graph"]}
    def values(value):
        return value if isinstance(value, list) else [value]
    def ids(value):
        return [name(v["@id"]) for v in values(value) if isinstance(v, dict) and "@id" in v]
    def ancestors(kind, visited=None):
        visited = set() if visited is None else visited
        if kind in visited:
            return visited
        visited.add(kind)
        for parent in ids(definitions.get(kind, {}).get("rdfs:subClassOf", [])):
            ancestors(parent, visited)
        return visited
    count = 0
    for document in documents:
        entities = {item["@id"]: item for item in document["@graph"] if "@id" in item}
        def inspect(node):
            nonlocal count
            if not isinstance(node, dict):
                return
            types = values(node.get("@type", []))
            inherited = set().union(*(ancestors(kind) for kind in types)) if types else set()
            for kind in types:
                assert kind in definitions, f"Unknown Schema.org type: {kind}"
            for prop, value in node.items():
                if prop.startswith("@"):
                    continue
                assert prop in definitions, f"Unknown Schema.org property: {prop}"
                definition = definitions[prop]
                domains = set(ids(definition.get("schema:domainIncludes", [])))
                assert not domains or not inherited or domains & inherited, (types, prop, "domain")
                ranges = set(ids(definition.get("schema:rangeIncludes", [])))
                for item in values(value):
                    if isinstance(item, dict):
                        target = entities.get(item.get("@id"), item)
                        item_types = values(target.get("@type", []))
                        item_ancestors = set().union(*(ancestors(t) for t in item_types)) if item_types else set()
                        assert not ranges or not item_ancestors or ranges & item_ancestors, (types, prop, item_types, "range")
                        inspect(item)
                    elif isinstance(item, bool):
                        assert not ranges or "Boolean" in ranges, (prop, "boolean")
                    elif isinstance(item, (int, float)):
                        assert not ranges or ranges & {"Integer", "Number", "Float"}, (prop, "number")
                    elif isinstance(item, str):
                        assert not ranges or ranges & {"Text", "URL", "Date", "DateTime", "Time", "Duration"}, (prop, ranges, "text")
                count += 1
        for node in document["@graph"]:
            inspect(node)
    return count


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--vocabulary")
    args = parser.parse_args()
    tree = ET.parse(ROOT / "sitemap.xml")
    entries = tree.findall("{*}url")
    urls = [entry.findtext("{*}loc") for entry in entries]
    assert len(urls) == len(set(urls)) == 39, "Expected 39 unique canonical pages"
    pages = {}
    for url in urls:
        assert url.startswith(SITE + "/") and url.endswith("/") and "?" not in url
        path = ROOT / url.removeprefix(SITE).strip("/") / "index.html"
        assert path.is_file(), path
        text = path.read_text()
        page = Page(text)
        assert page.canonical == [url], (path, "canonical")
        assert page.h1 == 1, (path, "H1")
        assert len(page.titles) == 1 and page.titles[0].strip(), (path, "title")
        assert page.meta.get("description", "").strip(), (path, "description")
        assert "noindex" not in page.meta.get("robots", ""), path
        assert page.meta["og:url"] == url and page.meta["og:title"] == page.titles[0]
        assert page.meta["twitter:title"] == page.titles[0]
        assert len(page.ids) == len(set(page.ids)), (path, "duplicate IDs")
        assert all(label in page.ids for label in page.labels), (path, "ARIA reference")
        assert all(all(k in img for k in ("alt", "width", "height")) for img in page.images)
        assert len(page.json) == 1 and page.json[0].get("@graph"), (path, "JSON-LD")
        identity = next(item for item in page.json[0]["@graph"] if item.get("@type") == "Person")
        assert identity["@id"] == SITE + "/#person" and identity["name"] == "Jean-Pierre Boutros"
        pages[path] = page
        for ref in page.refs + [page.meta["og:image"], page.meta["twitter:image"]]:
            target = local_target(ref, path)
            if target:
                assert target[0].is_file(), (path, ref, "missing local target")
    assert len({page.titles[0] for page in pages.values()}) == 39, "Duplicate titles"
    assert len({page.meta["description"] for page in pages.values()}) == 39, "Duplicate descriptions"
    incoming = Counter()
    for source, page in pages.items():
        for ref in page.refs:
            target = local_target(ref, source)
            if not target or target[0] not in pages:
                continue
            assert not target[1] or target[1] in pages[target[0]].ids, (source, ref, "fragment")
            if target[0] != source:
                incoming[target[0]] += 1
    assert all(incoming[path] for path in pages if path != ROOT / "index.html"), "Orphan page"
    home = pages[ROOT / "index.html"]
    assert len(home.cards) == len(home.dialogs) == 28
    assert sum("data-featured" in card for card in home.cards) == 6
    assert Counter(card["data-category"] for card in home.cards) == {"foh": 16, "monitors": 6, "broadcast": 1, "studio": 3, "technical": 2}
    gallery = json.loads(re.search(r'id="gallery-data">(.*?)</script>', (ROOT / "index.html").read_text(), re.S)[1])
    assert len(gallery) == 34
    assert all(link["href"] == gallery[int(link["data-gallery-index"])]["src"] for link in home.gallery_links)
    assert len(home.downloads) == 3 and len(set(home.downloads)) == 1
    for slug, role in {
        "baligh-hamdi-night": "Monitor engineer for Nancy Ajram",
        "warda-night": "Monitor engineer for Nancy Ajram",
        "night-of-arab-stars": "Monitor engineer for Nancy Ajram",
        "nancy-ajram-expo-dubai": "Monitor engineer for Nancy Ajram",
        "ehdeniyat-adam": "Monitor engineer for Adam",
        "nancy-ajram-olympia": "FOH engineer",
        "ehdeniyat-abeer-nehme": "FOH engineer",
        "ehdeniyat-al-shami": "FOH engineer",
        "marcel-khalife-amman": "Monitor &amp; recording engineer",
        "abeer-nehme-baalbeck": "FOH engineer",
        "beiteddine-marco-polo": "Audio technical supervision",
        "carole-samaha-golden-album": "Mixing &amp; mastering engineer",
        "zade-dirani-dbayeh": "FOH engineer",
        "zade-dirani-amman": "FOH engineer",
        "marcel-khalife-baalbeck": "FOH engineer",
        "nancy-ajram-jounieh": "FOH engineer",
        "mazeej-ndu": "FOH engineer",
        "beirut-the-sea-lover": "3D sound mixing",
    }.items():
        assert role in (ROOT / "projects" / slug / "index.html").read_text(), (slug, role)
    robots = RobotFileParser()
    robots.parse((ROOT / "robots.txt").read_text().splitlines())
    for bot in ("Googlebot", "bingbot", "OAI-SearchBot", "PerplexityBot"):
        assert all(robots.can_fetch(bot, url) for url in urls), bot
    assert not robots.can_fetch("GPTBot", SITE + "/"), "Owner's training exclusion"
    assert robots.site_maps() == [SITE + "/sitemap.xml"]
    assert "class=\"selected-credits" not in (ROOT / "index.html").read_text()
    if args.vocabulary:
        checked = vocabulary_check([p.json[0] for p in pages.values()], args.vocabulary)
        print(f"PASS: {checked} Schema.org property/domain/range checks against official vocabulary")
    print("PASS: 39 pages; unique metadata/H1s; canonical URLs; local assets, fragments and ARIA references; no orphan pages; preserved project/gallery counts and specific roles; search access and GPTBot exclusion.")


if __name__ == "__main__":
    main()
