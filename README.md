# Yuhang Yang — Personal Homepage

[Live site](https://yyh030806.github.io)

## Theme

Mercedes-inspired neutral silver and graphite with teal accents (palette A).
Both modes use the same bright teal (`#00D2BE`) for links, hover states and
decorative accents, with neutral white/silver or black/grey surfaces. The
profile image is `antonelli-helmet.png` (Kimi Antonelli helmet).
Research interests use compact tags below a divider. Publication controls have
transparent borders and subtle hover/selected backgrounds. Paragraph links
use bright teal text without underlines in both modes.
Small blue accents inspired by the Antonelli cap reference highlight news dates,
research tags, section markers, and the avatar stripe. Navigation selection
keeps the same bright teal as links. Blue is
`#1B5CCB` in light mode and `#77A7FF` for readable details in dark mode.

This repository is a prebuilt Next.js static export. Theme overrides are at
the end of `_next/static/css/844648a0feaa1485.css`. Profile markup is mirrored
in `index.html` and the homepage JavaScript chunk; profile data also appears
in `index.txt`. Keep these in sync when editing the export, and update asset
filenames and their references when changing cached CSS or JavaScript.

Preview locally with `python -m http.server 8765`, then open
`http://localhost:8765`.

## Publication panels

Abstract and BibTeX panels share theme rules at the end of the stylesheet.
The copy button implementation is kept in `scripts/citation-copy.js.template`
and mirrored into publication module 6669 and homepage module 2038. The
template's `REACT` and `COPY_ICON` placeholders use each module's existing
React and icon imports. It handles clipboard rejection, provides a legacy
copy fallback, and selects the citation for manual copying if both fail.
