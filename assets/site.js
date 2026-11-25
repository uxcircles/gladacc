/* Glad Accountancy concept: menu, lazy map, enquiry form (no backend). */
(() => {
  const zh = document.documentElement.lang.startsWith('zh');

  // menu
  const btn = document.querySelector('.menu-btn');
  const menu = document.getElementById('menu');
  if (btn && menu) {
    const set = (open) => {
      btn.setAttribute('aria-expanded', String(open));
      menu.hidden = !open;
      document.body.classList.toggle('menu-open', open);
    };
    btn.addEventListener('click', () => set(menu.hidden));
    document.addEventListener('keydown', (e) => { if (e.key === 'Escape' && !menu.hidden) { set(false); btn.focus(); } });
    window.matchMedia('(min-width: 981px)').addEventListener('change', (m) => { if (m.matches) set(false); });
  }

  // map: load MapLibre only when the map nears the screen
  const box = document.querySelector('[data-map]');
  if (box && 'IntersectionObserver' in window) {
    const load = (src, tag) => new Promise((ok, no) => {
      const el = document.createElement(tag);
      if (tag === 'link') { el.rel = 'stylesheet'; el.href = src; } else { el.src = src; }
      el.onload = ok; el.onerror = no; document.head.appendChild(el);
    });
    const io = new IntersectionObserver((entries) => {
      if (!entries.some((e) => e.isIntersecting)) return;
      io.disconnect();
      Promise.all([load(box.dataset.css, 'link'), load(box.dataset.src, 'script')])
        .then(() => load(box.dataset.mapjs, 'script'))
        .then(() => { try { window.gladMap(box); } catch (err) { /* fallback stays visible */ } })
        .catch(() => {});
    }, { rootMargin: '300px' });
    io.observe(box);
  }

  // enquiry form -> WhatsApp or email
  const form = document.getElementById('enquiry');
  if (form) {
    const err = form.querySelector('.form-err');
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const f = new FormData(form);
      const name = (f.get('name') || '').trim();
      const contact = (f.get('contact') || '').trim();
      if (!name || !contact) { err.hidden = false; form.querySelector(name ? '[name=contact]' : '[name=name]').focus(); return; }
      err.hidden = true;
      const svc = f.getAll('svc').join(', ');
      const msg = (f.get('msg') || '').trim();
      const lines = zh
        ? ['你好，Glad Accountancy。', `姓名：${name}`, `聯絡：${contact}`, svc && `需要：${svc}`, msg && `業務：${msg}`]
        : ['Hello Glad Accountancy,', `Name: ${name}`, `Contact: ${contact}`, svc && `Help with: ${svc}`, msg && `About my business: ${msg}`];
      const text = lines.filter(Boolean).join('\n');
      const via = e.submitter ? e.submitter.value : 'wa';
      if (via === 'email') {
        const subj = zh ? '網站查詢' : 'Enquiry from the website';
        window.location.href = `mailto:${form.dataset.email}?subject=${encodeURIComponent(subj)}&body=${encodeURIComponent(text)}`;
      } else {
        window.open(`${form.dataset.wa}?text=${encodeURIComponent(text)}`, '_blank', 'noopener');
      }
    });
  }
})();
