/* Matrix — interaksi: header, menu, reveal, parallax, hitung angka, kutipan, galeri, lightbox, formulir WhatsApp */
(function () {
  'use strict';
  var d = document, root = d.documentElement;
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  var $ = function (s, c) { return (c || d).querySelector(s); };
  var $$ = function (s, c) { return Array.prototype.slice.call((c || d).querySelectorAll(s)); };

  /* Header: solid setelah scroll, sembunyi saat scroll turun */
  var hd = $('.hd'), lastY = 0, ticking = false;
  function onScroll() {
    var y = window.scrollY;
    if (hd) {
      hd.classList.toggle('solid', y > 40);
      var open = root.classList.contains('menu-open');
      hd.classList.toggle('hide', !open && y > 320 && y > lastY + 4);
      if (y < lastY - 4) hd.classList.remove('hide');
    }
    lastY = y;
    if (!reduce) {
      $$('[data-par]').forEach(function (el) {
        var r = el.parentNode.getBoundingClientRect();
        if (r.bottom < -100 || r.top > window.innerHeight + 100) return;
        var sp = parseFloat(el.getAttribute('data-par')) || .1;
        var off = (r.top + r.height / 2 - window.innerHeight / 2) * sp * -1;
        el.style.transform = 'translate3d(0,' + off.toFixed(1) + 'px,0) scale(1.12)';
      });
      var hm = $('.hero-media');
      if (hm && y < window.innerHeight * 1.2) hm.style.transform = 'translate3d(0,' + Math.min(y * .18, 120).toFixed(1) + 'px,0)';
    }
    ticking = false;
  }
  window.addEventListener('scroll', function () { if (!ticking) { ticking = true; requestAnimationFrame(onScroll); } }, { passive: true });
  onScroll();

  /* Menu mobile */
  var burger = $('.burger'), mm = $('.mm');
  function setMenu(open) {
    root.classList.toggle('menu-open', open);
    if (burger) { burger.setAttribute('aria-expanded', open); burger.setAttribute('aria-label', open ? 'Tutup menu' : 'Buka menu'); }
    if (mm) mm.setAttribute('aria-hidden', !open);
    d.body.style.overflow = open ? 'hidden' : '';
    if (hd && open) hd.classList.add('solid');
  }
  if (burger) {
    burger.addEventListener('click', function () { setMenu(!root.classList.contains('menu-open')); });
    $$('a', mm).forEach(function (a) { a.addEventListener('click', function () { setMenu(false); }); });
    window.addEventListener('resize', function () { if (window.innerWidth >= 1100) setMenu(false); });
  }
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && root.classList.contains('menu-open')) { setMenu(false); burger.focus(); } });

  /* Reveal saat scroll */
  var rv = $$('.rv,.rvi');
  if ('IntersectionObserver' in window && !reduce) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { threshold: .12, rootMargin: '0px 0px -6% 0px' });
    rv.forEach(function (el) { io.observe(el); });
  } else rv.forEach(function (el) { el.classList.add('in'); });

  /* Hitung angka */
  $$('[data-count]').forEach(function (el) {
    var to = parseFloat(el.getAttribute('data-count')), dec = parseInt(el.getAttribute('data-dec') || '0', 10);
    var fmt = function (v) { return v.toFixed(dec).replace('.', ','); };
    if (reduce) { el.textContent = fmt(to); return; }
    var started = false;
    function run() {
      if (started) return; started = true;
      var t0 = performance.now(), dur = 1600;
      (function step(t) {
        var p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 3);
        el.textContent = fmt(to * e);
        if (p < 1) requestAnimationFrame(step);
      })(t0);
    }
    if ('IntersectionObserver' in window) {
      var o = new IntersectionObserver(function (es) { if (es[0].isIntersecting) { setTimeout(run, 700); o.disconnect(); } });
      o.observe(el);
    } else run();
  });

  /* Marquee: gandakan isi agar berputar mulus */
  $$('.marq-t').forEach(function (t) {
    Array.prototype.slice.call(t.children).forEach(function (c) { var k = c.cloneNode(true); k.setAttribute('aria-hidden', 'true'); k.setAttribute('alt', ''); t.appendChild(k); });
  });

  /* Rotasi kutipan */
  var qs = $$('.q'), dots = $$('.dots button'), qi = 0, qt;
  function showQ(i) {
    qi = (i + qs.length) % qs.length;
    qs.forEach(function (q, n) { q.classList.toggle('on', n === qi); q.setAttribute('aria-hidden', n !== qi); });
    dots.forEach(function (b, n) { b.setAttribute('aria-current', n === qi); });
  }
  if (qs.length) {
    dots.forEach(function (b, n) { b.addEventListener('click', function () { showQ(n); play(); }); });
    var box = $('.quotes');
    function play() { clearInterval(qt); if (!reduce) qt = setInterval(function () { showQ(qi + 1); }, 7000); }
    if (box) { box.addEventListener('mouseenter', function () { clearInterval(qt); }); box.addEventListener('mouseleave', play); }
    showQ(0); play();
  }

  /* Galeri: filter + lightbox */
  var items = $$('.gi');
  if (items.length) {
    $$('.filters button').forEach(function (b) {
      b.addEventListener('click', function () {
        var f = b.getAttribute('data-f');
        $$('.filters button').forEach(function (x) { x.setAttribute('aria-pressed', x === b); });
        items.forEach(function (it) { it.hidden = !(f === 'all' || it.getAttribute('data-c') === f); });
        var s = $('.g-status'); if (s) s.textContent = 'Menampilkan ' + items.filter(function (i) { return !i.hidden; }).length + ' foto';
      });
    });
    var lb = d.createElement('div');
    lb.className = 'lb'; lb.setAttribute('role', 'dialog'); lb.setAttribute('aria-modal', 'true'); lb.setAttribute('aria-label', 'Tampilan foto');
    lb.innerHTML = '<button class="x" aria-label="Tutup foto">&#10005;</button><button class="pv" aria-label="Foto sebelumnya">&#8249;</button><button class="nx" aria-label="Foto berikutnya">&#8250;</button><div class="lb-img"><img alt=""></div><p></p>';
    d.body.appendChild(lb);
    var li = $('.lb-img img', lb), lc = $('p', lb), cur = 0, opener = null;
    function vis() { return items.filter(function (i) { return !i.hidden; }); }
    function show(n) {
      var v = vis(); if (!v.length) return;
      cur = (n + v.length) % v.length;
      var b = $('button', v[cur]), im = $('img', b);
      li.src = b.getAttribute('data-full'); li.alt = im.alt; lc.textContent = $('figcaption', v[cur]).textContent;
    }
    function open(it) { opener = it; show(vis().indexOf(it.parentNode)); lb.classList.add('open'); d.body.style.overflow = 'hidden'; $('.x', lb).focus(); }
    function close() { lb.classList.remove('open'); d.body.style.overflow = ''; if (opener) opener.focus(); }
    items.forEach(function (it) { $('button', it).addEventListener('click', function (e) { open(e.currentTarget); }); });
    $('.x', lb).addEventListener('click', close);
    $('.pv', lb).addEventListener('click', function () { show(cur - 1); });
    $('.nx', lb).addEventListener('click', function () { show(cur + 1); });
    lb.addEventListener('click', function (e) { if (e.target === lb || e.target.className === 'lb-img') close(); });
    d.addEventListener('keydown', function (e) {
      if (!lb.classList.contains('open')) return;
      if (e.key === 'Escape') close();
      if (e.key === 'ArrowLeft') show(cur - 1);
      if (e.key === 'ArrowRight') show(cur + 1);
      if (e.key === 'Tab') { var f = $$('button', lb), a = f[0], z = f[f.length - 1]; if (e.shiftKey && d.activeElement === a) { e.preventDefault(); z.focus(); } else if (!e.shiftKey && d.activeElement === z) { e.preventDefault(); a.focus(); } }
    });
    var sx = 0;
    lb.addEventListener('touchstart', function (e) { sx = e.touches[0].clientX; }, { passive: true });
    lb.addEventListener('touchend', function (e) { var dx = e.changedTouches[0].clientX - sx; if (Math.abs(dx) > 50) show(cur + (dx < 0 ? 1 : -1)); });
  }

  /* Formulir konsultasi -> WhatsApp */
  var form = $('#form-konsultasi');
  if (form) {
    var NUM = '6281252595566';
    var qp = new URLSearchParams(location.search).get('program');
    if (qp && form.kebutuhan) { for (var i = 0; i < form.kebutuhan.options.length; i++) if (form.kebutuhan.options[i].value === qp) form.kebutuhan.selectedIndex = i; }
    function err(f, m) { var e = $('#e-' + f.name); f.setAttribute('aria-invalid', !!m); if (e) e.textContent = m || ''; return !m; }
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var f = form.elements, ok = true, phone = f.hp.value.replace(/[^\d+]/g, '');
      ok = err(f.nama, f.nama.value.trim().length < 2 ? 'Tuliskan nama orang tua atau siswa.' : '') && ok;
      ok = err(f.hp, phone.replace(/\D/g, '').length < 9 ? 'Tuliskan nomor WhatsApp yang valid, misalnya 0812xxxxxxx.' : '') && ok;
      ok = err(f.kebutuhan, !f.kebutuhan.value ? 'Pilih kebutuhan belajar.' : '') && ok;
      if (!ok) { var bad = $('[aria-invalid="true"]', form); if (bad) bad.focus(); return; }
      var L = ['Halo Matrix Bimbingan Belajar Dan Etika, saya ingin berkonsultasi.', '',
        'Nama: ' + f.nama.value.trim(), 'Nomor WhatsApp: ' + f.hp.value.trim()];
      if (f.kelas.value.trim()) L.push('Jenjang/Kelas: ' + f.kelas.value.trim());
      L.push('Kebutuhan belajar: ' + f.kebutuhan.value);
      if (f.pesan.value.trim()) L.push('Pesan tambahan: ' + f.pesan.value.trim());
      L.push('', 'Terima kasih.');
      var url = 'https://wa.me/' + NUM + '?text=' + encodeURIComponent(L.join('\n'));
      var s = $('.status', form);
      s.innerHTML = 'Membuka WhatsApp… Jika tidak terbuka otomatis, <a class="link" target="_blank" rel="noopener" href="' + url + '">klik di sini</a>.';
      var w = window.open(url, '_blank', 'noopener');
      if (!w) location.href = url;
    });
    $$('input,select,textarea', form).forEach(function (el) { el.addEventListener('input', function () { if (el.getAttribute('aria-invalid') === 'true') err(el, ''); }); });
  }

  var y = $('#yr'); if (y) y.textContent = new Date().getFullYear();
})();
