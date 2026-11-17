# Changelog

## v2.1 — GitHub distribution of the existing Notion release

- Preserved the original 12 colors and 24 SillyTavern UI theme JSON files without editing their settings or custom CSS.
- Added stable downloads (complete ZIP and one ZIP per color), individual JSON paths, preview assets, and English/Korean instructions.
- Archived the original Notion v2.1 ZIPs under `archive/v2.1/` for rollback.
- This is a **distribution/packaging change**, not a new theme version or a visual redesign.

Future fixes should edit the affected source JSONs in `themes/`, rebuild stable ZIPs with `python3 tools/build_downloads.py`, verify all 24 variants, and document the change before publishing.
