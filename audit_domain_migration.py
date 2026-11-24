#!/usr/bin/env python3
"""Read-only live domain-migration checks, with real response-header evidence."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
from pathlib import Path
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

from audit_live import fetch
from check_site import Page, ROOT, SITE


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    mapping = json.loads((ROOT / "hosting/domain-migration.json").read_text())
    paths = [urlsplit(e.findtext("{*}loc")).path
             for e in ET.parse(ROOT / "sitemap.xml").findall("{*}url")]
    tasks = []

    def add(url, group, destination, status=200, agent="JPB-Domain-Migration-Audit/1.0",
            location=None, expected_hash=None):
        tasks.append({"url": url, "group": group, "destination": destination,
                      "expected_status": status, "agent": agent,
                      "expected_location": location, "expected_hash": expected_hash})

    for host in ("studiojpb.com", "www.studiojpb.com", "jeanpierreboutros.com", "www.jeanpierreboutros.com"):
        for scheme in ("http", "https"):
            origin = scheme + "://" + host
            for path in paths:
                destination = SITE + path
                digest = sha256((ROOT / path.strip("/") / "index.html").read_bytes()).hexdigest()
                add(origin + path, "canonical-page-matrix", destination,
                    location=destination if origin != SITE else None, expected_hash=digest)

    query = "utm_source=studiojpb&ref=one%20two&ref=a%2Fb&literal=%26%23"
    for host in mapping["source_hosts"]:
        for scheme in ("http", "https"):
            origin = scheme + "://" + host
            for item in mapping["legacy_pages"]:
                target = item["destination"]
                path, separator, fragment = target.partition("#")
                destination = SITE + path + "?" + query + (separator + fragment if separator else "")
                add(origin + item["source_path"] + "?" + query, "legacy-mapping", destination,
                    location=destination)
                add(origin + item["source_path"], "legacy-mapping-clean", SITE + target, location=SITE + target)
            for source, target in (("/index.html", "/"),
                                   ("/live-sound-engineer", "/live-sound-engineer/"),
                                   ("/projects/nancy-ajram-olympia/index.html", "/projects/nancy-ajram-olympia/")):
                destination = SITE + target + "?" + query
                add(origin + source + "?" + query, "single-hop-normalization", destination, location=destination)
            for path in ("/migration-audit-unmatched-20261124/", "/missing%20photo%23name.jpg",
                         "/studiojpb.com/Gallery_files/rss.xml", "/construction.png"):
                destination = SITE + path + "?" + query
                add(origin + path + "?" + query, "unmatched-real-404", destination, status=404, location=destination)
            # A direct robots response avoids imposing cross-host REP redirect
            # handling on crawlers; it retains the existing search/training split.
            add(origin + "/robots.txt", "old-robots", origin + "/robots.txt",
                expected_hash=sha256((ROOT / "robots.txt").read_bytes()).hexdigest())
            for path in ("/cpanel", "/webmail"):
                add(origin + path, "hosting-and-mail-entry", origin + path)
            for path in ("/.well-known/acme-challenge/migration-audit-missing-20261124",
                         "/.well-known/pki-validation/migration-audit-missing-20261124"):
                add(origin + path, "certificate-path-exception", origin + path, status=404)
            for path in ("/sitemap.xml", "/llms.txt"):
                add(origin + path, "discovery", SITE + path, location=SITE + path,
                    expected_hash=sha256((ROOT / path.lstrip("/")).read_bytes()).hexdigest())
            for agent in ("Googlebot", "bingbot", "OAI-SearchBot", "Claude-SearchBot", "PerplexityBot",
                          "ChatGPT-User", "Claude-User", "Perplexity-User", "Applebot", "Googlebot-Image"):
                add(origin + "/projects/studio-jpb/", "search-and-ai-agents", SITE + "/projects/studio-jpb/",
                    agent=agent, location=SITE + "/projects/studio-jpb/")

    def run(task):
        result = fetch((task["url"], task["agent"], task["expected_hash"]))
        errors = []
        hops = [h for h in result["redirects"] if h.get("location")]
        if result["curl_exit"]: errors.append("curl/TLS error")
        if result["status"] != task["expected_status"]: errors.append("final status")
        if result["effective_url"] != task["destination"]: errors.append("final URL")
        if task["expected_location"]:
            if len(hops) != 1: errors.append("expected exactly one redirect")
            elif hops[0]["status"].split()[1] != "301" or hops[0]["location"] != task["expected_location"]:
                errors.append("301 Location mismatch")
        elif hops: errors.append("unexpected redirect")
        if result.get("matches_local_bytes") is False: errors.append("body hash")
        return {"group": task["group"], "expected_location": task["expected_location"],
                "expected_final_url": task["destination"], "expected_status": task["expected_status"],
                "errors": errors, **result}

    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(run, tasks))
    metadata_errors = []
    for path in paths:
        page = ROOT / path.strip("/") / "index.html"
        text = page.read_text()
        if "studiojpb.com" in text.lower(): metadata_errors.append(str(page.relative_to(ROOT)))
        parsed = Page(text)
        if parsed.canonical != [SITE + path]: metadata_errors.append("canonical: " + path)
    failures = [r for r in results if r["errors"]]
    report = {"checked": "2026-11-24", "canonical_pages": len(paths),
              "scope": "Live public GETs with normal TLS certificate verification; actual headers and final body hashes. A single network vantage. User-agent tests do not prove operator-IP access, indexing or authority transfer.",
              "requests": len(results), "failed_requests": len(failures),
              "active_metadata_errors": metadata_errors, "results": results}
    args.output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({k: report[k] for k in ("requests", "failed_requests", "active_metadata_errors")}))
    for r in failures[:10]: print(r["url"], r["errors"], r["redirects"])
    if failures or metadata_errors: raise SystemExit(1)


if __name__ == "__main__":
    main()
