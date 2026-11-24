#!/usr/bin/env python3
"""Read-only public delivery audit. No account access or search submissions."""
import argparse
from concurrent.futures import ThreadPoolExecutor
from hashlib import sha256
import json
from pathlib import Path
import subprocess
import tempfile
from urllib.parse import urlsplit
from xml.etree import ElementTree as ET

from check_site import Page, ROOT, SITE


def fetch(task):
    url, agent, expected_hash = task
    with tempfile.TemporaryDirectory() as directory:
        body, headers = Path(directory) / "body", Path(directory) / "headers"
        command = ["curl", "--silent", "--show-error", "--compressed", "--location",
                   "--max-redirs", "5", "--max-time", "25", "--max-filesize", "6000000",
                   "--user-agent", agent, "--dump-header", str(headers),
                   "--output", str(body), "--write-out", "%{json}", url]
        result = subprocess.run(command, capture_output=True, text=True)
        try:
            timing = json.loads(result.stdout)
        except ValueError:
            timing = {}
        blocks = []
        if headers.exists():
            for block in headers.read_text(errors="replace").strip().split("\n\n"):
                lines = block.splitlines()
                if lines and lines[0].startswith("HTTP/"):
                    values = dict(line.split(":", 1) for line in lines[1:] if ":" in line)
                    blocks.append({"status": lines[0], **{
                        k.lower(): v.strip() for k, v in values.items()
                        if k.lower() not in ("set-cookie", "authentication-info", "www-authenticate")
                    }})
        data = body.read_bytes() if body.exists() else b""
        record = {"url": url, "agent": agent, "curl_exit": result.returncode,
                  "status": timing.get("http_code"), "effective_url": timing.get("url_effective"),
                  "redirects": blocks, "ttfb_seconds": timing.get("time_starttransfer"),
                  "total_seconds": timing.get("time_total"), "transfer_bytes": timing.get("size_download"),
                  "decoded_bytes": len(data), "sha256": sha256(data).hexdigest()}
        if expected_hash:
            record["matches_local_bytes"] = record["sha256"] == expected_hash
        if result.returncode:
            record["error"] = result.stderr.strip()
        return record


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    parser.add_argument("--external", action="store_true")
    args = parser.parse_args()
    urls = [entry.findtext("{*}loc") for entry in ET.parse(ROOT / "sitemap.xml").findall("{*}url")]
    tasks, assets, external = [], set(), set()
    for url in urls:
        file = ROOT / url.removeprefix(SITE).strip("/") / "index.html"
        tasks.append((url, "JPB-ReadOnly-SEO-Audit/1.0", sha256(file.read_bytes()).hexdigest()))
        for ref in Page(file.read_text()).refs:
            parsed = urlsplit(ref)
            if parsed.scheme == "https" and parsed.netloc != urlsplit(SITE).netloc:
                external.add(ref.split("#")[0])
            elif ref.startswith("/") and not ref.startswith("//") and not parsed.path.endswith("/"):
                assets.add(SITE + ref.split("#")[0])
    for asset in sorted(assets):
        path = ROOT / urlsplit(asset).path.lstrip("/")
        if path.is_file():
            tasks.append((asset, "JPB-ReadOnly-SEO-Audit/1.0", sha256(path.read_bytes()).hexdigest()))
    for path in ("robots.txt", "sitemap.xml", "llms.txt"):
        tasks.append((SITE + "/" + path, "JPB-ReadOnly-SEO-Audit/1.0", sha256((ROOT / path).read_bytes()).hexdigest()))
    for url in ("http://jeanpierreboutros.com/", "http://www.jeanpierreboutros.com/",
                "https://jeanpierreboutros.com/", SITE + "/live-sound-engineer",
                SITE + "/projects/nancy-ajram-olympia/index.html", SITE + "/seo-audit-missing-20261124/"):
        tasks.append((url, "JPB-ReadOnly-SEO-Audit/1.0", None))
    for agent in ("Googlebot", "bingbot", "OAI-SearchBot", "Claude-SearchBot", "PerplexityBot",
                  "ChatGPT-User", "Claude-User", "Perplexity-User", "Googlebot-Image", "Applebot"):
        for path in ("/", "/projects/ry-x-qatar-philharmonic-doha/", "/robots.txt"):
            tasks.append((SITE + path, agent, None))
    if args.external:
        tasks.extend((url, "Mozilla/5.0 (compatible; JPB-Link-Audit/1.0)", None) for url in sorted(external))
    with ThreadPoolExecutor(max_workers=4) as pool:
        results = list(pool.map(fetch, tasks))
    report = {"checked": "2026-11-24", "scope": "Single local network vantage; public GET requests only. User agents are spoofable; this does not prove verified operator IP access or global latency.",
              "canonical_pages": len(urls), "external_destinations": len(external), "results": results}
    Path(args.output).write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"requests": len(results), "canonical_200": sum(r["status"] == 200 for r in results[:len(urls)]),
                      "local_byte_mismatches": sum(r.get("matches_local_bytes") is False for r in results),
                      "unresolved": sum(bool(r["curl_exit"]) or r["status"] >= 400 for r in results)}))


if __name__ == "__main__":
    main()
