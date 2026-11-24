"""Exercise dry-run safety and fail-closed publication checks without networking."""
from contextlib import redirect_stdout
from hashlib import sha256
from io import StringIO
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import indexnow


class IndexNowSafety(unittest.TestCase):
    def test_dry_run_preserves_key_and_makes_no_requests(self):
        original = indexnow.KEY_FILE.read_bytes()
        with patch("sys.argv", ["indexnow.py", "--prepare"]), patch.object(indexnow, "urlopen") as network:
            with redirect_stdout(StringIO()) as output:
                indexnow.main()
            self.assertIn("No HTTP requests", output.getvalue())
            network.assert_not_called()
        self.assertEqual(original, indexnow.KEY_FILE.read_bytes())

    def test_foreign_unlisted_and_query_urls_are_rejected(self):
        for url in ("https://example.org/", indexnow.SITE + "/missing/", indexnow.SITE + "/?q=test"):
            with self.subTest(url=url), self.assertRaises(ValueError):
                indexnow.prepare_payload([url])

    def test_wrong_live_key_aborts_before_fetching_pages(self):
        payload = indexnow.prepare_payload([indexnow.SITE + "/"])
        with patch.object(indexnow, "get", return_value=b"wrong-key") as fetch:
            with self.assertRaisesRegex(ValueError, "ownership key"):
                indexnow.verify_live(payload)
            self.assertEqual(fetch.call_count, 1)

    def test_stale_live_html_prevents_submission(self):
        payload = indexnow.prepare_payload([indexnow.SITE + "/"])
        with patch("sys.argv", ["indexnow.py", "--submit", "--url", indexnow.SITE + "/"]), \
             patch.object(indexnow, "get", side_effect=[payload["key"].encode(), b"old-release"]), \
             patch.object(indexnow, "urlopen") as network:
            with self.assertRaises(SystemExit) as error:
                indexnow.main()
            self.assertEqual(error.exception.code, 1)
            network.assert_not_called()

    def test_matching_key_and_exact_html_pass_publication_gate(self):
        payload = indexnow.prepare_payload([indexnow.SITE + "/"])
        with patch.object(indexnow, "get", side_effect=[payload["key"].encode(), (indexnow.ROOT / "index.html").read_bytes()]):
            indexnow.verify_live(payload)


if __name__ == "__main__":
    unittest.main()
