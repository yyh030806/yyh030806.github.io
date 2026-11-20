"""Build the classic-layout preview. Uses only the Python standard library."""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parent
papers = json.loads((ROOT / 'publications.json').read_text())

def read(name):
    return (ROOT / name).read_text()

def paper(p, with_figure=False):
    key = escape(p['id'])
    links = ''.join(f'<a href="{escape(a["href"], quote=True)}" target="_blank" rel="noopener">{escape(a["label"])} <span aria-hidden="true">↗</span></a>' for a in p['links'])
    figure = f'<button class="paper-figure" type="button" data-image aria-label="Enlarge figure: {escape(p["title"], quote=True)}"><img src="{p["image"]}" alt="{escape(p["title"], quote=True)} — overview figure" loading="lazy"><span class="enlarge" aria-hidden="true">↗</span></button>' if with_figure else ''
    return f'''<article class="paper {'paper-with-figure' if with_figure else ''}" id="paper-{key}" data-selected="{str(p['selected']).lower()}">
      {figure}<div class="paper-content"><h3>{escape(p['title'])}</h3><p class="authors">{p['authors_html']}</p><p class="venue">{escape(p['venue'])}</p>
      <div class="paper-actions">{links}<button type="button" data-panel="abstract-{key}" aria-controls="abstract-{key}" aria-expanded="false" data-en="Abstract" data-zh="摘要">Abstract</button><button type="button" data-panel="bib-{key}" aria-controls="bib-{key}" aria-expanded="false">BibTeX</button></div>
      <div class="paper-panel" id="abstract-{key}" hidden><p>{escape(p['abstract'])}</p></div>
      <div class="paper-panel bib-panel" id="bib-{key}" hidden><div class="bib-toolbar"><span>BIBTEX</span><button type="button" data-copy data-en="Copy citation" data-zh="复制引用">Copy citation</button></div><pre tabindex="0">{escape(p['bibtex'])}</pre></div>
      </div></article>'''

def page(kind, title, content):
    header = read('header.html').replace(f'data-nav="{kind}"', f'data-nav="{kind}" aria-current="page"')
    return f'''<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="description" content="Yuhang Yang — AI for Science and computational biology at USTC."><meta name="theme-color" content="#f5f5f5">
<title>{title} — Yuhang Yang</title><link rel="icon" href="favicon.svg"><link rel="preload" href="assets/fonts/inter-latin-wght-normal.woff2" as="font" type="font/woff2" crossorigin>
<script>try{{document.documentElement.dataset.theme=localStorage.getItem('yyh-preview-theme')||(matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light')}}catch(e){{}}</script>
<link rel="stylesheet" href="assets/chinese-font.css"><link rel="stylesheet" href="assets/style.css"><link rel="stylesheet" href="assets/classic.css">
<script src="assets/vendor/gsap.min.js" defer></script><script src="assets/main.js" defer></script></head>
<body data-page="{kind}"><a class="skip" href="#main">Skip to content</a>{header}
{content}
<footer class="wrap footer"><p>© <span data-year>2026</span> Yuhang Yang</p><a href="#main" data-en="Back to top ↑" data-zh="回到顶部 ↑">Back to top ↑</a></footer>
<dialog class="lightbox" aria-label="Research figure"><div class="lightbox-bar"><span data-en="Research figure" data-zh="研究示意图">Research figure</span><button class="icon-button" type="button" data-close aria-label="Close image">×</button></div><img alt=""><p class="lightbox-caption"></p></dialog>
<div class="toast" role="status" aria-live="polite" hidden></div></body></html>'''

profile = '''<aside class="profile enter" aria-label="Personal profile">
  <div class="portrait-frame"><img src="assets/img/antonelli-helmet.webp" width="720" height="720" alt="Kimi Antonelli’s helmet — Yuhang Yang’s avatar" fetchpriority="high"></div>
  <div class="profile-name"><h1>Yuhang Yang<span class="name-dot">.</span></h1><p class="profile-role" data-en="MS Student" data-zh="硕士研究生">MS Student</p><p class="affiliation" data-en="University of Science and Technology of China" data-zh="中国科学技术大学">University of Science and Technology of China</p></div>
  <div class="profile-links">
    <a href="mailto:yyh20030806@mail.ustc.edu.cn" aria-label="Email" title="Email"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg></a>
    <a href="https://scholar.google.com/citations?&amp;user=IlgLh1wAAAAJ" target="_blank" rel="noopener" aria-label="Google Scholar" title="Google Scholar"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="m2 9 10-5 10 5-10 5L2 9Zm4 2v6c4 3 8 3 12 0v-6M22 9v7"/></svg></a>
    <a href="https://orcid.org/0009-0001-0349-7230" target="_blank" rel="noopener" aria-label="ORCID" title="ORCID"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M8 10v7M8 7v.01M12 17v-7h2a3.5 3.5 0 0 1 0 7h-2Z"/></svg></a>
    <a href="https://github.com/yyh030806" target="_blank" rel="noopener" aria-label="GitHub" title="GitHub"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 22v-4c-4.5 1-4.5-2-6-2m12 6v-4a5 5 0 0 0-1-3.5c3 0 6-2 6-5.5a5 5 0 0 0-1-3.5 5 5 0 0 0 0-3.5s-1 0-3 1.5a13 13 0 0 0-8 0C6 2 5 2 5 2a5 5 0 0 0 0 3.5A5 5 0 0 0 4 9c0 3.5 3 5.5 6 5.5A5 5 0 0 0 9 18"/></svg></a>
  </div>
  <p class="profile-location"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M19 10c0 5-7 11-7 11S5 15 5 10a7 7 0 0 1 14 0Z"/><circle cx="12" cy="10" r="2"/></svg><span data-en="Hefei, China" data-zh="中国 · 合肥">Hefei, China</span></p>
  <div class="profile-interests"><h2 data-en="Research Interests" data-zh="研究方向">Research Interests</h2><ul><li>AI for Science</li><li>Generative AI</li><li>Bioinformatics</li><li>Computational Biology</li></ul></div>
</aside>'''

home = f'''<main id="main" class="wrap home-layout">{profile}<div class="content-column">
<section class="about-section enter" id="about" aria-labelledby="about-title"><div class="section-heading"><h2 id="about-title" data-en="About" data-zh="关于">About</h2></div><div class="about-copy">{read('about-content.html')}</div></section>
{read('news.html')}
<section class="publications section" id="publications" aria-labelledby="publications-title"><div class="section-heading publication-heading"><h2 id="publications-title" data-en="Selected Publications" data-zh="精选论文">Selected Publications</h2><a class="text-button" href="publications.html"><span data-en="View all" data-zh="查看全部">View all</span> <span aria-hidden="true">↗</span></a></div><div class="publication-list">{''.join(paper(p) for p in papers if p['selected'])}</div></section>
</div></main>'''

pubs = f'''<main id="main" class="wrap page-main"><div class="page-heading enter"><h1 data-en="Publications" data-zh="论文">Publications<span class="name-dot">.</span></h1><p data-en="A collection of my research work." data-zh="研究论文">A collection of my research work.</p></div>
<div class="publication-tools"><label class="search-field"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="10" cy="10" r="6"/><path d="m15 15 6 6"/></svg><span class="sr-only" data-en="Search publications" data-zh="查看论文">Search publications</span><input type="search" data-search placeholder="Search publications..." aria-label="Search publications"></label><button type="button" class="filter-button" data-filter aria-pressed="false" data-en="Selected only" data-zh="仅显示精选">Selected only</button></div>
<div class="publication-meta"><p class="publication-legend" data-en="* Equal contribution · † Corresponding author" data-zh="* 共同贡献 · † 通讯作者">* Equal contribution · † Corresponding author</p><span data-count role="status">6 papers</span></div>
<div class="publication-list">{''.join(paper(p, True) for p in papers)}</div><p class="empty-results" hidden data-empty data-en="No matching publications." data-zh="没有找到相关论文。">No matching publications.</p></main>'''

cv = f'''<main id="main" class="wrap page-main cv-main"><div class="page-heading enter"><h1>CV<span class="name-dot">.</span></h1><p data-en="Education, research interests, and skills." data-zh="教育与经历">Education, research interests, and skills.</p></div><div class="cv-copy">{read('cv-content.html')}</div></main>'''

for name, kind, title, body in [('index.html','about','About',home),('publications.html','publications','Publications',pubs),('cv.html','cv','CV',cv)]:
    (ROOT / name).write_text(page(kind,title,body))
print('Built classic-layout preview: index.html, publications.html, cv.html')
