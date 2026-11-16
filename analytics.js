(function () {
  'use strict';

  var config = document.querySelector('meta[name="ga-measurement-id"]');
  var id = config && config.content;
  if (!/^G-[A-Z0-9]+$/.test(id || '') ||
      !/^(www\.)?jeanpierreboutros\.com$/.test(window.location.hostname)) return;

  var key = 'jpb.analytics.choice.v1';
  var lifetime = 180 * 24 * 60 * 60 * 1000;
  var panel = document.querySelector('.analytics-choice');
  var details = document.getElementById('privacy-details');
  var status = document.querySelector('[data-analytics-status]');
  var settings = document.querySelector('[data-analytics-settings]');
  var reject = document.querySelector('[data-analytics-reject]');
  var accept = document.querySelector('[data-analytics-accept]');
  if (!panel || !settings || !reject || !accept) return;
  var loaded = false;
  var enabled = false;
  var openedFromSettings = false;
  var privacySignal = navigator.globalPrivacyControl === true ||
    navigator.doNotTrack === '1' || window.doNotTrack === '1';

  function savedChoice() {
    try {
      var value = JSON.parse(window.localStorage.getItem(key));
      return value && typeof value.expires === 'number' && value.expires > Date.now() &&
        (value.choice === 'allow' || value.choice === 'reject') ? value.choice : null;
    } catch (error) { return null; }
  }

  function remember(choice) {
    try { window.localStorage.setItem(key, JSON.stringify({choice: choice, expires: Date.now() + lifetime})); }
    catch (error) { /* A browser without storage still respects this page's choice. */ }
  }

  function referrerOrigin() {
    try { return document.referrer ? new URL(document.referrer).origin : ''; }
    catch (error) { return ''; }
  }

  function tag() {
    window.dataLayer = window.dataLayer || [];
    window.dataLayer.push(arguments);
  }

  function clearAnalyticsCookies() {
    document.cookie.split(';').forEach(function (item) {
      var name = item.trim().split('=')[0];
      if (!/^_ga(?:_|$)/.test(name)) return;
      ['', window.location.hostname, '.jeanpierreboutros.com', 'jeanpierreboutros.com'].forEach(function (domain) {
        document.cookie = name + '=; Max-Age=0; path=/; SameSite=Lax; Secure' +
          (domain ? '; domain=' + domain : '');
      });
    });
  }

  function updateStatus() {
    if (status) status.textContent = privacySignal ?
      'Optional analytics are off because of your browser privacy preference.' :
      'Optional analytics are ' + (enabled ? 'on.' : 'off.');
  }

  function activate() {
    enabled = true;
    window['ga-disable-' + id] = false;
    if (!loaded) {
      loaded = true;
      window.gtag = tag;
      tag('consent', 'default', {analytics_storage: 'denied', ad_storage: 'denied',
        ad_user_data: 'denied', ad_personalization: 'denied'});
      tag('js', new Date());
      tag('consent', 'update', {analytics_storage: 'granted', ad_storage: 'denied',
        ad_user_data: 'denied', ad_personalization: 'denied'});
      tag('config', id, {send_page_view: false, allow_google_signals: false,
        allow_ad_personalization_signals: false, cookie_expires: lifetime / 1000,
        cookie_flags: 'SameSite=Lax;Secure',
        page_location: window.location.origin + window.location.pathname,
        page_referrer: referrerOrigin(),
        debug_mode: new URLSearchParams(window.location.search).get('analytics_debug') === '1'});
      tag('event', 'page_view', {page_location: window.location.origin + window.location.pathname,
        page_referrer: referrerOrigin()});
      var script = document.createElement('script');
      script.async = true;
      script.src = 'https://www.googletagmanager.com/gtag/js?id=' + id;
      document.head.appendChild(script);
    } else {
      tag('consent', 'update', {analytics_storage: 'granted'});
    }
    updateStatus();
  }

  function disable() {
    enabled = false;
    window['ga-disable-' + id] = true;
    if (loaded) tag('consent', 'update', {analytics_storage: 'denied'});
    clearAnalyticsCookies();
    updateStatus();
  }

  function choose(choice) {
    remember(choice);
    if (choice === 'allow' && !privacySignal) activate(); else disable();
    panel.hidden = true;
    if (openedFromSettings) settings.focus();
    openedFromSettings = false;
  }

  reject.addEventListener('click', function () { choose('reject'); });
  accept.addEventListener('click', function () { choose('allow'); });
  settings.hidden = false;
  settings.addEventListener('click', function () {
    openedFromSettings = true;
    panel.hidden = false;
    reject.focus();
  });
  document.querySelectorAll('a[href="#privacy-details"]').forEach(function (link) {
    link.addEventListener('click', function () { if (details) details.open = true; });
  });
  accept.disabled = privacySignal;
  var initial = savedChoice();
  if (initial === 'allow' && !privacySignal) activate(); else disable();
  panel.hidden = !!initial || privacySignal;

  window.addEventListener('storage', function (event) {
    if (event.key !== key) return;
    if (savedChoice() === 'allow' && !privacySignal) activate(); else disable();
    panel.hidden = !!savedChoice() || privacySignal;
  });

  document.addEventListener('click', function (event) {
    if (!enabled || event.isTrusted === false || (event.button != null && event.button !== 0)) return;
    var link = event.target.closest && event.target.closest('a[href]');
    if (!link) return;
    var url;
    try { url = new URL(link.href, window.location.href); } catch (error) { return; }
    var location = link.closest('#contact') ? 'contact' : link.closest('#inquiry') ? 'inquiry' :
      link.closest('.hero') ? 'hero' : link.closest('#about') ? 'about' : 'other';
    var params = {page_path: window.location.pathname, link_location: location};
    if (url.protocol === 'mailto:') {
      params.contact_method = 'email';
      tag('event', 'contact_click', params);
    } else if (url.protocol === 'https:' && url.hostname === 'wa.me') {
      params.contact_method = 'whatsapp';
      tag('event', 'contact_click', params);
    } else if (url.origin === window.location.origin &&
               url.pathname === '/output/pdf/jean-pierre-boutros-profile.pdf') {
      tag('event', 'profile_download', params);
    }
  });
}());
