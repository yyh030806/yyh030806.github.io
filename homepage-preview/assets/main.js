(() => {
  'use strict';
  const root = document.documentElement;
  const $ = (s, el = document) => el.querySelector(s);
  const $$ = (s, el = document) => [...el.querySelectorAll(s)];
  const save = (key, value) => { try { localStorage.setItem(key, value); } catch (_) {} };
  let locale = 'en';
  const themeButton = $('[data-theme-toggle]');
  const systemTheme = matchMedia('(prefers-color-scheme: dark)');
  const updateThemeLabel = () => {
    const dark = root.dataset.theme === 'dark';
    themeButton.setAttribute('aria-label', locale === 'zh' ? (dark ? '切换浅色模式' : '切换深色模式') : `Switch to ${dark ? 'light' : 'dark'} mode`);
    $('meta[name="theme-color"]').content = dark ? '#101213' : '#f5f5f5';
  };
  if (!root.dataset.theme) root.dataset.theme = systemTheme.matches ? 'dark' : 'light';
  themeButton.addEventListener('click', () => {
    root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
    save('yyh-preview-theme', root.dataset.theme);
    updateThemeLabel();
  });
  systemTheme.addEventListener('change', (event) => {
    let saved = null; try { saved = localStorage.getItem('yyh-preview-theme'); } catch (_) {}
    if (!saved) { root.dataset.theme = event.matches ? 'dark' : 'light'; updateThemeLabel(); }
  });

  const englishBio = $('[data-biography]').innerHTML;
  const chineseBio = '我目前是<a href="https://en.ustc.edu.cn/" target="_blank" rel="noopener">中国科学技术大学</a>计算机科学与技术学院的硕士研究生，导师为<a href="http://staff.ustc.edu.cn/~cheneh/" target="_blank" rel="noopener">陈恩红教授</a>和<a href="https://faculty.ustc.edu.cn/zhangkai123/zh_CN/index.htm" target="_blank" rel="noopener">张凯教授</a>。2025 年于中国科学技术大学获得工学学士学位。';
  const moreButton = $('[data-show-all]');
  const morePapers = $('#other-publications');
  function updateMoreLabel() {
    const open = moreButton.getAttribute('aria-expanded') === 'true';
    $('span', moreButton).textContent = locale === 'zh' ? (open ? '仅显示精选' : '查看全部 6 篇') : (open ? 'Show selected only' : 'View all 6 papers');
    $('span[aria-hidden]', moreButton).textContent = open ? '−' : '↗';
  }
  function setLanguage(lang) {
    locale = lang === 'zh' ? 'zh' : 'en';
    root.lang = locale === 'zh' ? 'zh-CN' : 'en';
    $$('[data-en][data-zh]').forEach(el => { el.textContent = el.dataset[locale]; });
    $('[data-biography]').innerHTML = locale === 'zh' ? chineseBio : englishBio;
    $('[data-language]').textContent = locale === 'zh' ? 'EN' : '中';
    $('[data-language]').setAttribute('aria-label', locale === 'zh' ? 'Switch to English' : '切换中文');
    updateMoreLabel(); updateThemeLabel();
    save('yyh-preview-locale', locale);
  }
  let initialLocale = 'en'; try { initialLocale = localStorage.getItem('yyh-preview-locale') || 'en'; } catch (_) {}
  setLanguage(initialLocale);
  $('[data-language]').addEventListener('click', () => setLanguage(locale === 'en' ? 'zh' : 'en'));

  moreButton.addEventListener('click', () => {
    const open = moreButton.getAttribute('aria-expanded') !== 'true';
    moreButton.setAttribute('aria-expanded', String(open));
    morePapers.hidden = !open;
    updateMoreLabel();
  });
  $$('[data-panel]').forEach(button => button.addEventListener('click', () => {
    const panel = document.getElementById(button.dataset.panel);
    const open = button.getAttribute('aria-expanded') !== 'true';
    button.setAttribute('aria-expanded', String(open));
    panel.hidden = !open;
  }));

  let toastTimer;
  function notify(message) {
    clearTimeout(toastTimer);
    const toast = $('.toast');
    toast.textContent = message; toast.hidden = false;
    toastTimer = setTimeout(() => { toast.hidden = true; }, 3500);
  }
  $$('[data-copy]').forEach(button => button.addEventListener('click', async () => {
    const pre = $('pre', button.closest('.bib-panel'));
    button.disabled = true;
    let success = false;
    try { await navigator.clipboard.writeText(pre.textContent); success = true; } catch (_) {
      const input = document.createElement('textarea');
      input.value = pre.textContent;
      input.style.cssText = 'position:fixed;left:-9999px;top:0';
      document.body.append(input); input.select();
      try { success = document.execCommand('copy'); } catch (_) {}
      input.remove();
    }
    button.disabled = false; button.focus({preventScroll:true});
    if (success) notify(locale === 'zh' ? '引用已复制' : 'Citation copied to clipboard');
    else {
      const selection = getSelection(); const range = document.createRange();
      range.selectNodeContents(pre); selection.removeAllRanges(); selection.addRange(range);
      const shortcut = /Mac|iPhone|iPad/.test(navigator.platform) ? '⌘C' : 'Ctrl+C';
      notify(locale === 'zh' ? `已选中引用，请按 ${shortcut} 复制` : `Citation selected. Press ${shortcut} to copy.`);
    }
  }));

  const dialog = $('.lightbox');
  $$('[data-image]').forEach(button => button.addEventListener('click', () => {
    const source = $('img', button);
    $('img', dialog).src = source.src;
    $('img', dialog).alt = source.alt;
    $('.lightbox-caption', dialog).textContent = $('h3', button.closest('.paper')).textContent;
    dialog.showModal();
    document.body.style.overflow = 'hidden';
  }));
  $('[data-close]', dialog).addEventListener('click', () => dialog.close());
  dialog.addEventListener('click', event => {
    if (event.target !== dialog) return;
    const rect = dialog.getBoundingClientRect();
    if (event.clientX < rect.left || event.clientX > rect.right || event.clientY < rect.top || event.clientY > rect.bottom) dialog.close();
  });
  dialog.addEventListener('close', () => { document.body.style.overflow = ''; });

  let scheduled = false;
  function setActiveNavigation() {
    scheduled = false;
    let active = 'about';
    ['publications', 'cv'].forEach(id => { if (document.getElementById(id).getBoundingClientRect().top <= 180) active = id; });
    $$('[data-nav]').forEach(a => {
      if (a.dataset.nav === active) a.setAttribute('aria-current', 'page');
      else a.removeAttribute('aria-current');
    });
  }
  addEventListener('scroll', () => { if (!scheduled) { scheduled = true; requestAnimationFrame(setActiveNavigation); } }, {passive:true});
  setActiveNavigation();
  $('[data-year]').textContent = new Date().getFullYear();

  // Content is visible by default, including when GSAP or JavaScript is unavailable.
  if (window.gsap) {
    const media = gsap.matchMedia();
    media.add('(prefers-reduced-motion: no-preference)', () => {
      gsap.from('.enter', {y:10, opacity:0, duration:.48, stagger:.055, ease:'power2.out', clearProps:'transform,opacity'});
    });
  }
})();
