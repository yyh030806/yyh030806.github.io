(() => {
  const root = document.documentElement;

  // Theme: follows the system until the visitor picks one.
  const themeBtn = document.querySelector('[data-theme-toggle]');
  const systemDark = () => window.matchMedia('(prefers-color-scheme: dark)').matches;
  const current = () => root.dataset.theme || (systemDark() ? 'dark' : 'light');
  root.dataset.theme = current();
  themeBtn?.addEventListener('click', () => {
    const next = current() === 'dark' ? 'light' : 'dark';
    root.dataset.theme = next;
    try { localStorage.setItem('theme', next); } catch (e) {}
  });

  // Top bar border after scrolling.
  const bar = document.querySelector('.topbar');
  const onScroll = () => bar.classList.toggle('scrolled', window.scrollY > 8);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  // Highlight the menu item for the section in view.
  const links = [...document.querySelectorAll('.menu a[href^="#"]')];
  const sections = links.map((a) => document.querySelector(a.getAttribute('href'))).filter(Boolean);
  if ('IntersectionObserver' in window) {
    const spy = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (!e.isIntersecting) return;
        links.forEach((a) => a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id));
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    sections.forEach((s) => spy.observe(s));

    const reveal = new IntersectionObserver((entries) => {
      entries.forEach((e) => {
        if (e.isIntersecting) { e.target.classList.add('in'); reveal.unobserve(e.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    document.querySelectorAll('.reveal').forEach((el) => reveal.observe(el));
  } else {
    document.querySelectorAll('.reveal').forEach((el) => el.classList.add('in'));
  }

  // Publication filter.
  const pubs = [...document.querySelectorAll('.pub')];
  document.querySelectorAll('.filters button').forEach((btn, _, all) => {
    btn.addEventListener('click', () => {
      all.forEach((b) => b.setAttribute('aria-pressed', String(b === btn)));
      const f = btn.dataset.filter;
      pubs.forEach((p) => { p.hidden = f !== 'all' && !p.dataset.tags.split(' ').includes(f); });
    });
  });

  // Copy BibTeX.
  document.querySelectorAll('.copy').forEach((btn) => {
    btn.addEventListener('click', async () => {
      const pre = btn.parentElement.querySelector('pre');
      const text = pre.textContent;
      let ok = false;
      try { await navigator.clipboard.writeText(text); ok = true; } catch (e) {
        const range = document.createRange();
        range.selectNodeContents(pre);
        const sel = getSelection();
        sel.removeAllRanges();
        sel.addRange(range);
        try { ok = document.execCommand('copy'); } catch (err) {}
      }
      btn.textContent = ok ? 'Copied' : 'Press Ctrl+C';
      setTimeout(() => { btn.textContent = 'Copy'; }, 1600);
    });
  });

  // Image preview.
  const box = document.querySelector('.lightbox');
  const boxImg = box?.querySelector('img');
  document.querySelectorAll('.thumb').forEach((t) => {
    t.addEventListener('click', () => {
      const img = t.querySelector('img');
      boxImg.src = img.src;
      boxImg.alt = img.alt;
      box.showModal();
    });
  });
  box?.addEventListener('click', (e) => { if (e.target === box || e.target.closest('button')) box.close(); });

  const year = document.querySelector('[data-year]');
  if (year) year.textContent = new Date().getFullYear();
})();
