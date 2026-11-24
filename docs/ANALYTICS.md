# Inquiry and traffic measurement

Documentation reconciled **24 November 2026**. Current deployed runtime is
`252b41f` with 42 canonical pages. SEO, gallery and domain migration preserve
`analytics.js` and existing consent behavior; the 24 November consent/analytics
tests pass and live runtime bytes match. Account configuration and real GA4
event receipt below were verified on **16 November 2026**; no new GA4 account
or reporting-receipt test is claimed. See the [final closeout](SESSION-CLOSEOUT-2026-11-24.md)
and [final recheck](domain-migration-recheck-2026-11-24.json).

Google Analytics account and property were created on 16 November 2026 after
the owner approved Google's Analytics Terms and Data Processing Terms. The
website stream is `G-KHS391KEP1`, for `https://www.jeanpierreboutros.com`.
This measurement ID is public configuration, not an account credential.

The owner chose Google's default account sharing: products/services off,
modeling/business insights on, technical support on and recommendations on.
No optional promotional email subscription was selected. Account settings and
website visitor consent are separate choices. The property uses Lebanon reporting
time and US dollars.

## Collection and visitor controls

`analytics.js` uses basic consent behavior: the Google tag is not loaded until
the visitor allows optional analytics. Rejecting consent sends no Analytics
events. The footer's Privacy & analytics section explains collection and lets
the visitor change the choice. The choice lasts up to 180 days in localStorage.
Analytics cookies are configured for 180 days, including global configuration
before destination initialization. The final browser cookie table confirmed
this expiry. Browser Do Not Track and Global
Privacy Control preferences keep this site's optional analytics off.

On withdrawal, the implementation disables the Google tag, clears visible `_ga`
cookies for the relevant domain scopes and stops its interaction events. Consent
changes synchronize between tabs. If browser storage is unavailable, a choice
still applies to the current page without promising persistence.

The implementation runs only on jeanpierreboutros.com and its www hostname.
Local previews and requests served on other hostnames do not send data.
The retired StudioJPB website now returns server redirects; after arrival
on the primary domain, normal visitor consent controls analytics there.
Advertising storage, user data and personalization consent remain denied;
Google Signals and ad personalization are not enabled by this implementation.

GA4 Enhanced measurement was turned off in the stream after the owner's
explicit approval. This avoids additional automatic outbound-link, download,
scroll, video and history events beyond the intended collection.

## Events and interpretation

| Event | Meaning | Parameters sent by this implementation |
| --- | --- | --- |
| `page_view` | A page viewed after analytics consent | Page URL without query/fragment; referral origin only |
| `contact_click` | Email or WhatsApp link clicked | `contact_method` (email/whatsapp), `page_path`, `link_location` |
| `profile_download` | Professional-profile PDF link clicked | `page_path`, `link_location` |

Custom events also explicitly supply the sanitized page URL, referral origin
and an optional debug hint. Global page settings apply before destination
initialization. The table lists the service-specific event fields.

`link_location` is a fixed label: hero, about, contact, inquiry or other. Message
contents, email subjects, full outbound URLs and user-entered form values are
not included in these custom event payloads. Normal GA4 service processing still
applies to consented visits; see the public privacy section and Google's policy.

A click is intent, not proof of a sent message, received inquiry, completed
download or booking. Use a private inquiry log for actual qualified discussions
and bookings. Copy [the blank template](inquiry-log-template.csv) to a private
location before filling it; do not commit client information to the repository.

## Reporting

Use GA4 Realtime/DebugView to validate installation. The `analytics_debug=1`
query option supplies the debug-mode hint for a consented test page; the query
itself is removed from the page URL. Realtime receipt was verified; independent
DebugView filtering was not confirmed. This hint does not automatically exclude
tests from normal reports. Label test visits as QA in release notes and account
for them when assessing real demand.

Standard reporting can take time to populate. Inspect `contact_click` by
`contact_method` and `link_location`, and compare page/country/referral reports
over rolling 28-day periods. The event-scoped custom dimensions **Contact method**
(`contact_method`) and **Link location** (`link_location`) were created in GA4
Admin on 16 November 2026. Do not sum
page views and contact clicks as though they were booked projects.

Consent refusal, privacy signals, ad blockers, app referrers and cross-device
behavior limit measurement. Some AI visits can be identified by referrer origin;
this is not a complete count of Claude, ChatGPT, Grok, Gemini or other citations.
Removing query strings also intentionally limits campaign-parameter attribution.

Search visibility belongs in Search Console and Bing Webmaster Tools. The
observed [search baseline](growth-search-baseline-2026-11-16.json) distinguishes
reports still processing from actual zero values. No organic-growth claim is
made before data is available.

## Maintenance and validation

Edit the confirmed stream ID in `measurement.py`, then rebuild the website if
the stream changes. Keep the same value in the site checker. Rebuild after
editing analytics.js, so its content hash changes. The deployment manifest copies
only the runtime script, not the Python configuration or unit test.

Run `node test_analytics.js`, `python3 check_site.py` and the production build.
The tests cover consent gating, refusal, expiry, browser opt-outs, withdrawal,
payload sanitization, click semantics and hostname isolation without contacting
Google. Verify the real production network and reporting separately after a
release; unit tests alone do not establish collection.

Production verification on 16 November 2026 confirmed consent gating, sanitized
contact/PDF event URLs, one configured page view, 180-day cookies, cookie removal
on withdrawal and Realtime event receipt. See
[the analytics verification](growth-analytics-verification-2026-11-16.json).
Standard GA4 session/engagement events may also be generated after consent.

Official references checked on 16 November 2026:

- [Basic consent mode](https://developers.google.com/tag-platform/security/concepts/consent-mode)
- [Consent implementation](https://developers.google.com/tag-platform/security/guides/consent)
- [Privacy settings and programmatic opt-out](https://developers.google.com/tag-platform/security/guides/privacy)
- [GA4 configuration](https://developers.google.com/analytics/devguides/collection/ga4/reference/config)
- [Events and verification](https://developers.google.com/analytics/devguides/collection/ga4/events)
