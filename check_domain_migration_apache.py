#!/usr/bin/env python3
"""Test migration rules against an isolated Apache fixture, never production.

The fixture must contain the generated site and the managed fragment installed
with install-seo.sh. Operational fixture files and a denied sentinel test that
exempting mail/validation paths does not skip pre-existing access controls.
"""
import argparse
import json
from urllib.error import HTTPError
from urllib.request import Request, build_opener, HTTPRedirectHandler
from xml.etree import ElementTree as ET

from check_site import ROOT, SITE


class StopRedirects(HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", default="http://127.0.0.1:8789")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    if not args.base.startswith("http://127.0.0.1:"):
        parser.error("Use the isolated localhost Apache fixture")
    opener = build_opener(StopRedirects)
    rows = []

    def check(path, host, expected=301, location=None):
        try:
            response = opener.open(Request(args.base + path, headers={"Host": host}), timeout=10)
        except HTTPError as error:
            response = error
        response.read()
        result = {"path": path, "host": host, "status": response.status,
                  "location": response.headers.get("Location")}
        rows.append(result)
        assert response.status == expected, result
        assert result["location"] == location, result

    paths = [e.findtext("{*}loc").removeprefix(SITE)
             for e in ET.parse(ROOT / "sitemap.xml").findall("{*}url")]
    for path in paths:
        check(path, "localhost", 200)
        for host in ("studiojpb.com", "www.studiojpb.com", "jeanpierreboutros.com", "www.jeanpierreboutros.com"):
            check(path, host, location=SITE + path)
    mapping = json.loads((ROOT / "hosting/domain-migration.json").read_text())
    query = "utm_source=old&ref=one%20two&encoded=a%2Fb&literal=%26%23"
    for host in ("studiojpb.com", "www.studiojpb.com", "STUDIOJPB.COM", "studiojpb.com:80"):
        for item in mapping["legacy_pages"]:
            path, separator, fragment = item["destination"].partition("#")
            location = SITE + path + "?" + query + (separator + fragment if separator else "")
            check(item["source_path"] + "?" + query, host, location=location)
            check(item["source_path"], host, location=SITE + item["destination"])
        for source, target in (("/index.html", "/"), ("/projects/studio-jpb", "/projects/studio-jpb/"),
                               ("/projects/studio-jpb/index.html", "/projects/studio-jpb/"),
                               ("/missing%20photo%23name.jpg", "/missing%20photo%23name.jpg"),
                               ("/unmatched/", "/unmatched/"), ("/sitemap.xml", "/sitemap.xml"),
                               ("/photos/ry-x-backstage-portrait-2026.jpg", "/photos/ry-x-backstage-portrait-2026.jpg")):
            check(source + "?" + query, host, location=SITE + target + "?" + query)
        for path in ("/robots.txt", "/.well-known/acme-challenge/migration-probe",
                     "/webmail/migration-probe", "/autodiscover/migration-probe",
                     "/google1234567890abcdef.html", "/BingSiteAuth.xml"):
            check(path, host, 200)
        check("/webmail/migration-protected.txt", host, 403)
    for host in ("mail.studiojpb.com", "webmail.studiojpb.com", "unrelated.example",
                 "studiojpb.com.evil.example", "jeanpierreboutros.com.evil.example"):
        check("/", host, 200)
    check("/unmatched/", "localhost", 404)
    report = {"checked": "2026-11-24", "scope": "Isolated real Apache HTTP fixture; production TLS and redirects are validated separately.",
              "checks": len(rows), "passed": True, "results": rows}
    with open(args.output, "w") as handle:
        json.dump(report, handle, indent=2)
        handle.write("\n")
    print("PASS:", len(rows), "real Apache checks; mappings, queries, escaping, operational exceptions and host isolation")


if __name__ == "__main__":
    main()
