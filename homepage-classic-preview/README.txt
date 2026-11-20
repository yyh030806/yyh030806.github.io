Classic layout / refreshed visual style — local preview

Open http://localhost:8793/homepage-classic-preview/
The earlier full-width design remains at /homepage-preview/ for comparison.
For an SSH workspace, forward port 8793 in VS Code's Ports panel.

Start a server from the repository root if needed:
  python -m http.server 8793 --bind 127.0.0.1

Pages:
  index.html          Original two-column homepage layout
  publications.html   Full publication list with search and selected filter
  cv.html             Original CV content with refreshed styling

The homepage keeps the avatar, name, affiliation, social links and research
interests on the left, and About, News and selected publication cards on the
right. Small screens stack the profile above the content. Publication figures
appear on the separate Publications page. Header navigation changes pages.

Edit build.py, header.html, about-content.html, news.html, cv-content.html,
publications.json or the assets, then run:
  python homepage-classic-preview/build.py

Styles: assets/style.css contains the shared visual system from the previous
preview; assets/classic.css defines the classic layouts. assets/main.js handles
theme and interface language persistence, citation copy with fallback, search,
filtering, figure dialogs and a reduced-motion-aware GSAP entrance.

The academic paper content and CV retain their original English text; interface
labels and the homepage biography have Chinese translations. Fonts and GSAP
are served locally. Font licenses are in assets/fonts/licenses/. GSAP's license
notice is preserved in assets/vendor/gsap.min.js.

This is an independent preview. Production files, existing staged changes and
the previous preview have not been modified. Nothing has been deployed.
