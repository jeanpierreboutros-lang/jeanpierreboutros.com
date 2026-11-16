'use strict';
// Privacy boundaries and event semantics; no browser or Google requests are made.
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(__dirname + '/analytics.js', 'utf8');
const id = 'G-KHS391KEP1';
const key = 'jpb.analytics.choice.v1';

function fixture(options = {}) {
  const elements = {};
  const element = () => ({hidden: false, disabled: false, listeners: {},
    addEventListener(type, fn) { this.listeners[type] = fn; }, focus() { this.focused = true; }});
  ['.analytics-choice', '[data-analytics-status]', '[data-analytics-settings]',
    '[data-analytics-reject]', '[data-analytics-accept]'].forEach(s => { elements[s] = element(); });
  const meta = {content: options.id || id};
  const details = element();
  const privacyLink = element();
  const scripts = [];
  const cookies = [];
  const documentEvents = {};
  const windowEvents = {};
  const values = new Map();
  if (options.saved !== undefined) values.set(key, options.saved);
  const document = {
    referrer: options.referrer || 'https://chatgpt.com/c/private?email=private@example.com',
    querySelector(s) { return s === 'meta[name="ga-measurement-id"]' ? meta : elements[s]; },
    getElementById() { return details; }, querySelectorAll() { return [privacyLink]; },
    createElement() { return {}; }, head: {appendChild(script) { scripts.push(script); }},
    addEventListener(type, fn) { documentEvents[type] = fn; }
  };
  Object.defineProperty(document, 'cookie', {
    get() { return '_ga=one; _ga_KHS391KEP1=two; important_preference=keep'; },
    set(value) { cookies.push(value); }
  });
  const window = {location: new URL(options.url || 'https://www.jeanpierreboutros.com/live-sound-engineer/?email=private@example.com#private'),
    localStorage: {getItem(k) { if (options.storageBlocked) throw Error('blocked'); return values.get(k) || null; },
      setItem(k, v) { if (options.storageBlocked) throw Error('blocked'); values.set(k, v); }},
    addEventListener(type, fn) { windowEvents[type] = fn; }};
  vm.runInNewContext(source, {window, document, navigator: {
    globalPrivacyControl: !!options.gpc, doNotTrack: options.dnt || '0'}, Date, URL, URLSearchParams});
  function click(selector) { elements[selector].listeners.click(); }
  function link(href, region = '#contact', trusted = true) {
    const anchor = {href, closest(s) { return s === region ? {} : null; }};
    documentEvents.click({isTrusted: trusted, button: 0, target: {closest() { return anchor; }}});
  }
  function commands() { return (window.dataLayer || []).map(x => Array.from(x)); }
  function events(name) { return commands().filter(x => x[0] === 'event' && (!name || x[1] === name)); }
  return {elements, details, privacyLink, scripts, cookies, window, values,
    windowEvents, click, link, commands, events};
}

const fresh = fixture();
assert.equal(fresh.scripts.length, 0, 'No Google request before consent');
assert.equal(fresh.elements['.analytics-choice'].hidden, false);
fresh.link('mailto:jp@jeanpierreboutros.com');
assert.equal(fresh.events().length, 0, 'No interaction events before consent');
fresh.click('[data-analytics-reject]');
assert.equal(fresh.scripts.length, 0, 'Rejecting never loads the tag');
assert.equal(JSON.parse(fresh.values.get(key)).choice, 'reject');
assert.ok(fresh.cookies.every(x => !x.startsWith('important_preference=')));

const allowed = fixture();
allowed.click('[data-analytics-accept]');
assert.equal(allowed.scripts.length, 1);
assert.equal(allowed.scripts[0].src, 'https://www.googletagmanager.com/gtag/js?id=' + id);
assert.equal(allowed.events('page_view').length, 1, 'Exactly one page view on activation');
const config = allowed.commands().find(x => x[0] === 'config')[2];
assert.equal(config.send_page_view, false);
const globalSettings = allowed.commands().find(x => x[0] === 'set')[1];
assert.equal(globalSettings.page_location, 'https://www.jeanpierreboutros.com/live-sound-engineer/');
assert.equal(globalSettings.page_referrer, 'https://chatgpt.com');
assert.equal(config.page_location, 'https://www.jeanpierreboutros.com/live-sound-engineer/');
assert.equal(config.page_referrer, 'https://chatgpt.com');
assert.equal(config.allow_google_signals, false);
assert.equal(config.allow_ad_personalization_signals, false);
assert.equal(config.cookie_expires, 15552000);
allowed.link('mailto:jp@jeanpierreboutros.com?subject=private%20message');
allowed.link('https://wa.me/9613883863?text=private%20message', '#inquiry');
allowed.link('https://www.jeanpierreboutros.com/output/pdf/jean-pierre-boutros-profile.pdf?v=abc', '.hero');
allowed.link('https://www.linkedin.com/in/jeanpierreboutros/');
allowed.link('mailto:jp@jeanpierreboutros.com', '#contact', false);
assert.equal(allowed.events('contact_click').length, 2);
assert.equal(allowed.events('profile_download').length, 1);
assert.equal(allowed.events('contact_click')[0][2].contact_method, 'email');
assert.equal(allowed.events('contact_click')[1][2].contact_method, 'whatsapp');
assert.equal(allowed.events('contact_click')[1][2].link_location, 'inquiry');
for (const event of allowed.events()) {
  assert.equal(event[2].page_location, 'https://www.jeanpierreboutros.com/live-sound-engineer/');
  assert.equal(event[2].page_referrer, 'https://chatgpt.com');
}
const debug = fixture({url: 'https://www.jeanpierreboutros.com/?analytics_debug=1&secret=private'});
debug.click('[data-analytics-accept]');
debug.link('mailto:jp@jeanpierreboutros.com');
assert.ok(debug.events().every(x => x[2].debug_mode === true));
assert.ok(!JSON.stringify(debug.commands()).includes('secret'));
assert.ok(!JSON.stringify(allowed.commands()).includes('private'), 'No query, fragment, full referrer or message text sent');
allowed.click('[data-analytics-settings]');
allowed.click('[data-analytics-reject]');
assert.equal(allowed.window['ga-disable-' + id], true);
assert.ok(allowed.elements['[data-analytics-settings]'].focused);
allowed.link('mailto:jp@jeanpierreboutros.com');
assert.equal(allowed.events('contact_click').length, 2, 'Revocation stops future interaction events');
allowed.click('[data-analytics-accept]');
assert.equal(allowed.scripts.length, 1, 'Re-enabling does not load a second tag');
assert.equal(allowed.events('page_view').length, 1);

for (const option of [{gpc: true}, {dnt: '1'}]) {
  const browserOptOut = fixture({...option, saved: JSON.stringify({choice: 'allow', expires: Date.now() + 10000})});
  assert.equal(browserOptOut.scripts.length, 0);
  assert.equal(browserOptOut.elements['[data-analytics-accept]'].disabled, true);
  browserOptOut.click('[data-analytics-accept]');
  assert.equal(browserOptOut.scripts.length, 0, 'Browser opt-out remains effective');
}
const returning = fixture({saved: JSON.stringify({choice: 'allow', expires: Date.now() + 10000})});
assert.equal(returning.scripts.length, 1);
assert.equal(returning.elements['.analytics-choice'].hidden, true);
const expired = fixture({saved: JSON.stringify({choice: 'allow', expires: Date.now() - 1})});
assert.equal(expired.scripts.length, 0);
assert.equal(expired.elements['.analytics-choice'].hidden, false);
assert.equal(fixture({saved: 'broken JSON'}).scripts.length, 0);
const noStorage = fixture({storageBlocked: true});
noStorage.click('[data-analytics-accept]');
assert.equal(noStorage.scripts.length, 1, 'Consent still works if persistence is unavailable');
const synced = fixture();
synced.values.set(key, JSON.stringify({choice: 'allow', expires: Date.now() + 10000}));
synced.windowEvents.storage({key});
assert.equal(synced.scripts.length, 1);
synced.values.set(key, JSON.stringify({choice: 'reject', expires: Date.now() + 10000}));
synced.windowEvents.storage({key});
assert.equal(synced.window['ga-disable-' + id], true);
assert.equal(fixture({id: 'not-a-real-id'}).scripts.length, 0);
assert.equal(fixture({url: 'https://studiojpb.com/'}).scripts.length, 0, 'Other shared-root host is excluded');
assert.equal(fixture({url: 'http://localhost:8000/'}).scripts.length, 0, 'Local previews do not send Analytics');
console.log('PASS: consent gating, refusal, persistence/expiry, privacy signals, revocation, safe payloads, interaction semantics and hostname isolation.');
