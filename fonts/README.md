# Self-hosted typefaces

Reviewed 16 November 2026. Fraunces normal/italic (400, 500) and Hanken Grotesk
(400, 500, 600) retain the existing Google Fonts typefaces and Unicode ranges.
The ten WOFF2 files are unmodified downloads from fonts.gstatic.com. The original
stylesheet request and source-to-local file mapping are recorded in
[manifest.json](manifest.json); subset definitions and `font-display: swap` are
in [fonts.css](fonts.css). Repeated declarations now use their existing variable
weight ranges (Hanken 400–600; Fraunces 400–500), reducing 24 declarations to ten
without changing the font binaries or supported subsets. The production folio uses Hanken Grotesk for display
and body text and system monospace for metadata. Only the Hanken Latin face is
preloaded; other subsets load when needed. Fraunces remains available for earlier
designs. Normal page requests use the self-hosted files.

The original licenses are retained in [fraunces-OFL.txt](fraunces-OFL.txt) and
[hankengrotesk-OFL.txt](hankengrotesk-OFL.txt). When replacing a font, update the
manifest, CSS, preloads and license/provenance records together, rebuild the
site, and verify the referenced files and delivery headers.
