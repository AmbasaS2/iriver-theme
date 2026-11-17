# Changelog

## v2.1.1 — iPad portrait top-bar width (2026-11-17)

- Fixed Safari/WebKit tablet widths of 768–1000px: the `#top-bar` background now retains SillyTavern's full viewport width instead of shrinking to `--sheldWidth`, matching the actual top menu button holder.
- Preserved the existing `--sheldWidth` behavior at widths of 1001px and above, and left the phone layout unchanged.
- Made this local CSS adjustment in all 24 theme JSONs; palette values, dialogue styles, and unrelated CSS remain unchanged.
- Rebuilt all 13 stable download ZIPs (12 color ZIPs and the complete ZIP). Verified source JSON changes, compressed JSON payload round trips, CRC-32 values, ZIP entry names and archive structure. The original `archive/v2.1/` release remains intact.
- Static/package verification completed. Physical iPad Safari visual testing is still pending.

## v2.1 — GitHub distribution of the existing Notion release

- Preserved the original 12 colors and 24 SillyTavern UI theme JSON files without editing their settings or custom CSS.
- Added stable downloads (complete ZIP and one ZIP per color), individual JSON paths, preview assets, and English/Korean instructions.
- Archived the original Notion v2.1 ZIPs under `archive/v2.1/` for rollback.
- This is a **distribution/packaging change**, not a new theme version or a visual redesign.

Future fixes should edit the affected source JSONs in `themes/`, rebuild stable ZIPs with `python3 tools/build_downloads.py`, verify all 24 variants, and document the change before publishing.
