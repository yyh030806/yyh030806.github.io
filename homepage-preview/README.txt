Yuhang Yang — local homepage preview

Preview from the repository root:
  python -m http.server 8793 --bind 127.0.0.1
  http://localhost:8793/homepage-preview/

For a remote SSH workspace, forward port 8793 in VS Code's Ports panel,
then open the forwarded localhost URL. The preview is not deployed.
You can also open index.html directly; clipboard access may use the manual
selection fallback when served as a local file.

Editable files:
  index.template.html   Page content and structure
  publications.json     Shared publication records (all six papers)
  assets/style.css      Responsive light/dark design
  assets/main.js        Theme, language, figures, citations and GSAP entrance

Regenerate index.html after editing the template or publication records:
  python homepage-preview/build.py
The build uses Python's standard library. No npm installation is needed.

Scope:
  This is a static design prototype. The Full CV link opens the existing
  site's CV. Paper titles, abstracts and citations retain their original
  English text in either interface language. No production files are changed.

Design:
  Content-first academic layout; neutral silver/graphite surfaces;
  #00D2BE teal and restrained Antonelli-inspired blue accents; real helmet
  avatar and existing research figures. Homepage shows two selected papers;
  an explicit button reveals the other four. The image modal preserves the
  complete research figure. Abstract and BibTeX use the same theme tokens.

Skill references:
  https://github.com/Leonxlnx/taste-skill
  https://github.com/greensock/gsap-skills
  Taste informs composition, consistent spacing and screenshot review.
  Its full commercial-site generator/gate was not executed: the approved
  academic brief uses content-sized sections, real contact details, existing
  colors, and no link underlines instead of its commercial defaults.
  GSAP core guidance is used for the entrance sequence, transform/opacity
  animation and prefers-reduced-motion. Remaining interactions use CSS.

Dependencies:
  Vendored GSAP 3.14.2; its original license notice is retained in the file.
  https://gsap.com/standard-license/
  Inter and JetBrains Mono fonts are reused from this repository.
  A Noto Sans SC subset covers the Chinese interface strings in this prototype.
  Font families are distributed under the SIL Open Font License.

Future source migration can move these tokens, data and components into Astro
after the visual direction is approved.
