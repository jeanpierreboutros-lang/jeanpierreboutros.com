(function () {
  'use strict';

  var nav = document.getElementById('nav');
  var progress = document.querySelector('.progress');
  var heroBg = document.querySelector('.hero-bg img');
  var navLinks = Array.prototype.slice.call(document.querySelectorAll('.nav-links a'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('section[id], header[id]'));

  /* ── Scroll: progress bar, nav state, hero parallax, active link ── */
  var ticking = false;
  function onScroll() {
    var y = window.scrollY || window.pageYOffset;
    var doc = document.documentElement;
    var max = (doc.scrollHeight - window.innerHeight) || 1;

    if (progress) progress.style.width = Math.min(100, (y / max) * 100) + '%';

    if (nav) nav.classList.toggle('scrolled', y > 24);

    if (heroBg && y < window.innerHeight) {
      heroBg.style.transform = 'translateY(' + (y * 0.3) + 'px) scale(1.12)';
    }

    var current = '';
    sections.forEach(function (sec) {
      var r = sec.getBoundingClientRect();
      if (r.top <= 140 && r.bottom > 140) current = sec.id;
    });
    navLinks.forEach(function (a) {
      var href = (a.getAttribute('href') || '').replace('#', '');
      a.classList.toggle('active', href === current);
    });
    ticking = false;
  }
  window.addEventListener('scroll', function () {
    if (!ticking) { window.requestAnimationFrame(onScroll); ticking = true; }
  }, { passive: true });
  onScroll();

  /* ── Mobile menu ── */
  var burger = document.querySelector('.nav-burger');
  var menu = document.getElementById('mobileMenu');
  function setMenu(open) {
    if (!menu || !burger) return;
    menu.classList.toggle('open', open);
    burger.setAttribute('aria-expanded', open ? 'true' : 'false');
    document.body.style.overflow = open ? 'hidden' : '';
  }
  if (burger) burger.addEventListener('click', function () {
    setMenu(!menu.classList.contains('open'));
  });
  if (menu) menu.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () { setMenu(false); });
  });

  /* ── Reveal on scroll ── */
  var reveals = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { en.target.classList.add('is-visible'); io.unobserve(en.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -8% 0px' });
    reveals.forEach(function (el) { io.observe(el); });
  } else {
    reveals.forEach(function (el) { el.classList.add('is-visible'); });
  }

  /* ── Name wall popovers ── */
  var cells = Array.prototype.slice.call(document.querySelectorAll('.namewall-cell'));
  function closeAllCells() { cells.forEach(function (c) { c.classList.remove('active'); c.setAttribute('aria-expanded', 'false'); }); }
  cells.forEach(function (cell) {
    cell.addEventListener('click', function (e) {
      // clicks inside the popover (other than close) shouldn't toggle
      if (e.target.closest('.namewall-pop') && !e.target.closest('.namewall-pop-close')) return;
      if (e.target.closest('.namewall-pop-close')) { cell.classList.remove('active'); cell.setAttribute('aria-expanded', 'false'); return; }
      var willOpen = !cell.classList.contains('active');
      closeAllCells();
      if (willOpen) { cell.classList.add('active'); cell.setAttribute('aria-expanded', 'true'); }
    });
  });
  document.addEventListener('click', function (e) {
    if (!e.target.closest('.namewall-cell')) closeAllCells();
  });

  /* ── Lightbox ── */
  var gallery = window.__GALLERY__ || [];
  var lb = document.getElementById('lightbox');
  var lbImg = lb ? lb.querySelector('.lightbox-img') : null;
  var idx = -1;
  function showImg(i) {
    if (!gallery.length) return;
    idx = (i + gallery.length) % gallery.length;
    lbImg.src = gallery[idx];
  }
  function openLb(i) { showImg(i); lb.classList.add('open'); lb.setAttribute('aria-hidden', 'false'); document.body.style.overflow = 'hidden'; }
  function closeLb() { lb.classList.remove('open'); lb.setAttribute('aria-hidden', 'true'); document.body.style.overflow = ''; idx = -1; }

  document.querySelectorAll('.gallery-item').forEach(function (item) {
    item.addEventListener('click', function () {
      openLb(parseInt(item.getAttribute('data-index'), 10) || 0);
    });
  });
  if (lb) {
    lb.addEventListener('click', function (e) { if (e.target === lb) closeLb(); });
    lb.querySelector('.lightbox-close').addEventListener('click', closeLb);
    lb.querySelector('.lightbox-prev').addEventListener('click', function (e) { e.stopPropagation(); showImg(idx - 1); });
    lb.querySelector('.lightbox-next').addEventListener('click', function (e) { e.stopPropagation(); showImg(idx + 1); });
    if (lbImg) lbImg.addEventListener('click', function (e) { e.stopPropagation(); });
  }

  /* ── Keyboard ── */
  document.addEventListener('keydown', function (e) {
    if (idx !== -1) {
      if (e.key === 'Escape') closeLb();
      else if (e.key === 'ArrowRight') showImg(idx + 1);
      else if (e.key === 'ArrowLeft') showImg(idx - 1);
    } else if (e.key === 'Escape') {
      closeAllCells();
      setMenu(false);
    }
  });
})();
