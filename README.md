# Yuhang Yang — Personal Homepage

[Live site](https://yyh030806.github.io)

## Theme

Mercedes-inspired neutral silver and graphite with teal accents (palette A).
Light mode uses white and silver surfaces with dark teal links; dark mode uses
neutral black and grey surfaces with bright teal accents. The
profile image is `antonelli-helmet.png` (Kimi Antonelli helmet).

This repository is a prebuilt Next.js static export. Theme overrides are at
the end of `_next/static/css/ac0dd3ad75c272eb.css`. Profile markup is mirrored
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
