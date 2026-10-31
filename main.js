(function () {
  'use strict';

  var nav = document.getElementById('nav');
  var progress = document.querySelector('.progress');
  var menu = document.getElementById('mobileMenu');
  var burger = document.querySelector('.nav-burger');
  var lightbox = document.getElementById('lightbox');
  var modalSupported = menu && typeof menu.showModal === 'function';
  var links = Array.prototype.slice.call(document.querySelectorAll('.nav-links a'));
  var sections = Array.prototype.slice.call(document.querySelectorAll('main > section[id]'));
  var reducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)');
  var root = document.documentElement;
  var hero = document.querySelector('.hero');
  var motionButton = document.getElementById('motionToggle');
  var motionPaused = false;
  var imageAnimation = null;
  var revealObserver = null;
  var mobileLayout = window.matchMedia('(max-width: 980px)');
  var gallery = JSON.parse(document.getElementById('gallery-data').textContent);
  var currentImage = 0;
  var galleryTrigger = null;

  // Keep every section and navigation link usable when JavaScript is unavailable.
  if (modalSupported) document.documentElement.classList.add('js-enabled');

  function syncScrollLock() {
    document.body.classList.toggle('has-modal', !!document.querySelector('dialog[open]'));
  }

  function closeMenu(destination) {
    if (!menu || !menu.open) return;
    menu.close();
    burger.setAttribute('aria-expanded', 'false');
    syncScrollLock();
    if (destination) destination.focus({ preventScroll: true });
  }

  if (modalSupported) {
    burger.addEventListener('click', function () {
      menu.showModal();
      burger.setAttribute('aria-expanded', 'true');
      syncScrollLock();
    });
    menu.addEventListener('close', function () {
      burger.setAttribute('aria-expanded', 'false');
      syncScrollLock();
    });
    menu.querySelectorAll('a').forEach(function (link, index) {
      link.style.setProperty('--menu-delay', index * 45 + 'ms');
      link.addEventListener('click', function () {
        closeMenu(document.querySelector(link.getAttribute('href')));
      });
    });
    mobileLayout.addEventListener('change', function (event) {
      if (!event.matches) closeMenu();
    });
  }

  // Native modal dialogs provide focus containment, Escape and background inertness.
  document.querySelectorAll('dialog').forEach(function (dialog) {
    dialog.querySelector('[data-close]').addEventListener('click', function () {
      dialog.close();
    });
    dialog.addEventListener('click', function (event) {
      if (event.target === dialog) dialog.close();
    });
    dialog.addEventListener('close', syncScrollLock);
  });

  function showImage(index) {
    currentImage = (index + gallery.length) % gallery.length;
    var photo = gallery[currentImage];
    var img = lightbox.querySelector('.lightbox-img');
    img.src = photo.src;
    img.alt = photo.alt;
    img.width = photo.width;
    img.height = photo.height;
    img.hidden = false;
    document.getElementById('lightbox-caption').textContent = photo.caption;
    document.getElementById('lightbox-count').textContent = (currentImage + 1) + ' / ' + gallery.length;
  }

  function motionAllowed() {
    return !reducedMotion.matches && !motionPaused;
  }

  lightbox.querySelector('.lightbox-img').addEventListener('load', function (event) {
    if (imageAnimation) imageAnimation.cancel();
    if (motionAllowed() && lightbox.open && typeof event.target.animate === 'function') {
      imageAnimation = event.target.animate([{ opacity: .45 }, { opacity: 1 }], {
        duration: 220, easing: 'ease-out'
      });
    }
  });

  if (modalSupported && gallery.length) {
    document.querySelectorAll('[data-gallery-index]').forEach(function (link) {
      link.addEventListener('click', function (event) {
        // Preserve opening a photograph in a separate tab with modifier keys.
        if (event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        galleryTrigger = link;
        showImage(Number(link.getAttribute('data-gallery-index')));
        lightbox.showModal();
        syncScrollLock();
      });
    });
    lightbox.querySelector('.lightbox-prev').addEventListener('click', function () { showImage(currentImage - 1); });
    lightbox.querySelector('.lightbox-next').addEventListener('click', function () { showImage(currentImage + 1); });
    lightbox.addEventListener('keydown', function (event) {
      if (event.key === 'ArrowRight' || event.key === 'ArrowLeft') {
        event.preventDefault();
        showImage(currentImage + (event.key === 'ArrowRight' ? 1 : -1));
      }
    });
    lightbox.addEventListener('close', function () {
      if (galleryTrigger && galleryTrigger.isConnected) galleryTrigger.focus({ preventScroll: true });
    });
  }

  var ticking = false;
  function updateScroll() {
    var y = window.scrollY;
    var max = document.documentElement.scrollHeight - window.innerHeight;
    if (progress) progress.style.width = (max > 0 ? Math.min(100, y / max * 100) : 0) + '%';
    nav.classList.toggle('scrolled', y > 24);
    if (hero) {
      var heroRect = hero.getBoundingClientRect();
      root.classList.toggle('hero-in-view', heroRect.bottom > 0 && heroRect.top < window.innerHeight);
    }
    var current = '';
    sections.forEach(function (section) {
      var rect = section.getBoundingClientRect();
      if (rect.top <= 180 && rect.bottom > 180) current = section.id;
    });
    links.forEach(function (link) {
      if (link.getAttribute('href') === '#' + current) link.setAttribute('aria-current', 'location');
      else link.removeAttribute('aria-current');
    });
    ticking = false;
  }
  function scheduleScroll() {
    if (!ticking) {
      window.requestAnimationFrame(updateScroll);
      ticking = true;
    }
  }
  window.addEventListener('scroll', scheduleScroll, { passive: true });
  window.addEventListener('resize', scheduleScroll);
  window.addEventListener('load', scheduleScroll);
  updateScroll();

  // Stagger each visible row, rather than delaying an entire long grid.
  document.querySelectorAll('[data-reveal-group]').forEach(function (group) {
    var columns = getComputedStyle(group).gridTemplateColumns;
    var count = columns && columns !== 'none' ? columns.split(' ').length : 1;
    Array.prototype.forEach.call(group.children, function (child, index) {
      child.setAttribute('data-reveal', '');
      child.style.setProperty('--reveal-delay', Math.min(index % count * 75, 225) + 'ms');
    });
  });
  var reveals = Array.prototype.slice.call(document.querySelectorAll('[data-reveal]'));
  if ('IntersectionObserver' in window) {
    revealObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          revealObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.04, rootMargin: '0px 0px -20px 0px' });
  }

  function updateMotion() {
    var enabled = motionAllowed();
    root.classList.toggle('motion-enabled', enabled);
    root.classList.toggle('motion-paused', !enabled);
    root.classList.toggle('has-reveals', enabled && !!revealObserver);
    if (motionButton) {
      motionButton.hidden = reducedMotion.matches;
      motionButton.setAttribute('aria-label', motionPaused ? 'Resume animations' : 'Pause animations');
      motionButton.querySelector('.motion-label').textContent = motionPaused ? 'Resume motion' : 'Pause motion';
      motionButton.querySelector('.motion-icon').textContent = motionPaused ? '▶' : 'Ⅱ';
    }
    if (revealObserver) {
      revealObserver.disconnect();
      if (enabled) reveals.forEach(function (element) {
        if (!element.classList.contains('is-visible')) revealObserver.observe(element);
      });
    }
    if (!enabled && imageAnimation) imageAnimation.cancel();
  }

  if (motionButton) motionButton.addEventListener('click', function () {
    motionPaused = !motionPaused;
    updateMotion();
  });
  reducedMotion.addEventListener('change', updateMotion);
  document.addEventListener('focusin', function (event) {
    var element = event.target.closest('[data-reveal]');
    if (element) {
      element.classList.add('is-visible');
      if (revealObserver) revealObserver.unobserve(element);
    }
  });
  document.addEventListener('visibilitychange', function () {
    root.classList.toggle('page-hidden', document.hidden);
  });
  root.classList.toggle('page-hidden', document.hidden);
  updateMotion();
})();
