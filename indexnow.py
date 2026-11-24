#!/usr/bin/env python3
"""Prepare IndexNow locally; submit only with --submit after exact live checks.

The key file is public ownership proof, not a credential. Building the site
never submits URLs. No request is made without the explicit --submit flag.
"""
import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import secrets
from urllib.error import HTTPError, URLError
from urllib.parse import urlsplit
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
SITE = "https://www.jeanpierreboutros.com"
KEY_FILE = ROOT / "indexnow-key.txt"
ENDPOINT = "https://api.indexnow.org/indexnow"


def prepare_payload(selected=None):
    key = KEY_FILE.read_text().strip()
    if not re.fullmatch(r"[a-f0-9]{32}", key):
        raise ValueError("IndexNow key must be exactly 32 lowercase hexadecimal characters")
    inventory = [e.findtext("{*}loc") for e in ET.parse(ROOT / "sitemap.xml").findall("{*}url")]
    urls = list(dict.fromkeys(selected or inventory))
    if not urls or len(urls) > 10000 or any(url not in inventory for url in urls):
        raise ValueError("Use 1–10,000 canonical URLs from the generated sitemap")
    return {"host": urlsplit(SITE).netloc, "key": key,
            "keyLocation": SITE + "/indexnow-key.txt", "urlList": urls}


def get(url):
    request = Request(url, headers={"User-Agent": "JPB-IndexNow-Verification/1.0"})
    with urlopen(request, timeout=30) as response:
        if response.status != 200 or response.url != url:
            raise ValueError("Expected a direct HTTP 200 for " + url)
        return response.read()


def verify_live(payload):
    if get(payload["keyLocation"]).decode("utf-8").strip() != payload["key"]:
        raise ValueError("Live ownership key does not match the prepared key")
    for url in payload["urlList"]:
        path = ROOT / url.removeprefix(SITE).strip("/") / "index.html"
        if sha256(get(url)).digest() != sha256(path.read_bytes()).digest():
            raise ValueError("Live page differs from the reviewed local build: " + url)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--prepare", action="store_true", help="Create a key once, preserving an existing valid key")
    parser.add_argument("--url", action="append", help="Changed canonical URL; repeat for a batch")
    parser.add_argument("--output", help="Write the dry-run payload to this local JSON file")
    parser.add_argument("--submit", action="store_true", help="Verify live key and exact published HTML, then submit")
    args = parser.parse_args()
    try:
        if args.prepare and not KEY_FILE.exists():
            KEY_FILE.write_text(secrets.token_hex(16) + "\n", encoding="utf-8")
        payload = prepare_payload(args.url)
        if args.output:
            Path(args.output).write_text(json.dumps(payload, indent=2) + "\n")
        if not args.submit:
            print(f"Prepared {len(payload['urlList'])} URLs. No HTTP requests or submissions made.")
            return
        verify_live(payload)
        request = Request(ENDPOINT, data=json.dumps(payload).encode(),
                          headers={"Content-Type": "application/json; charset=utf-8"}, method="POST")
        with urlopen(request, timeout=30) as response:
            print(f"IndexNow HTTP {response.status}; {len(payload['urlList'])} URLs sent. Indexing is not guaranteed.")
    except (OSError, ValueError, HTTPError, URLError) as error:
        parser.exit(1, f"IndexNow stopped: {error}\n")


if __name__ == "__main__":
    main()
