# Self-hosted typefaces

Reviewed 3 November 2026. Fraunces normal/italic (400, 500) and Hanken Grotesk
(400, 500, 600) retain the existing Google Fonts typefaces and Unicode ranges.
The ten WOFF2 files are unmodified downloads from fonts.gstatic.com. The original
stylesheet request and source-to-local file mapping are recorded in
[manifest.json](manifest.json); subset definitions and `font-display: swap` are
in [fonts.css](fonts.css). Three Latin faces are preloaded; other subsets load
when needed. Normal page requests use the self-hosted files.

The original licenses are retained in [fraunces-OFL.txt](fraunces-OFL.txt) and
[hankengrotesk-OFL.txt](hankengrotesk-OFL.txt). When replacing a font, update the
manifest, CSS, preloads and license/provenance records together, rebuild the
site, and verify the referenced files and delivery headers.
