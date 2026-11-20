"""Generate the local preview from a template and shared publication data. No dependencies."""
from pathlib import Path
from html import escape
import json

root = Path(__file__).resolve().parent
papers = json.loads((root / 'publications.json').read_text())

def render(p):
    key = escape(p['id'], quote=True)
    links = ''.join(f'<a href="{escape(a["href"], quote=True)}" target="_blank" rel="noopener">{escape(a["label"])} <span aria-hidden="true">↗</span></a>' for a in p['links'])
    return f'''<article class="paper" id="paper-{key}">
      <button class="paper-figure" type="button" data-image aria-label="Enlarge figure: {escape(p['title'], quote=True)}"><img src="{escape(p['image'], quote=True)}" alt="{escape(p['title'], quote=True)} — overview figure" loading="lazy" decoding="async"><span class="enlarge" aria-hidden="true">↗</span></button>
      <div class="paper-content"><p class="venue">{escape(p['venue'])}</p><h3>{escape(p['title'])}</h3><p class="authors">{p['authors_html']}</p><p class="paper-summary">{escape(p['summary'])}</p>
        <div class="paper-actions">{links}<button type="button" data-panel="abstract-{key}" aria-controls="abstract-{key}" aria-expanded="false" data-en="Abstract" data-zh="摘要">Abstract</button><button type="button" data-panel="bib-{key}" aria-controls="bib-{key}" aria-expanded="false">BibTeX</button></div>
        <div class="paper-panel" id="abstract-{key}" hidden><p>{escape(p['abstract'])}</p></div>
        <div class="paper-panel bib-panel" id="bib-{key}" hidden><div class="bib-toolbar"><span>BIBTEX</span><button type="button" data-copy data-en="Copy citation" data-zh="复制引用">Copy citation</button></div><pre tabindex="0">{escape(p['bibtex'])}</pre></div>
      </div>
    </article>'''

page = (root / 'index.template.html').read_text()
page = page.replace('{{SELECTED_PUBLICATIONS}}', '\n'.join(render(p) for p in papers if p['selected']))
page = page.replace('{{OTHER_PUBLICATIONS}}', '\n'.join(render(p) for p in papers if not p['selected']))
(root / 'index.html').write_text(page)
print(f'Built {root / "index.html"}: {len(papers)} publications')
