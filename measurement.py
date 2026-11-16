"""Confirmed GA4 configuration and progressive, optional analytics controls."""
from hashlib import sha256
from pathlib import Path

MEASUREMENT_ID = "G-KHS391KEP1"
ROOT = Path(__file__).resolve().parent


def measurement_head():
    version = sha256((ROOT / "analytics.js").read_bytes()).hexdigest()[:12]
    return (f'<meta name="ga-measurement-id" content="{MEASUREMENT_ID}" />'
            f'\n  <script src="/analytics.js?v={version}" defer></script>')


def measurement_markup():
    return '''<details class="privacy-details container" id="privacy-details">
  <summary>Privacy &amp; analytics</summary>
  <div class="privacy-copy"><h2>Website privacy and your choices</h2>
    <p>This professional website is operated by Jean-Pierre Boutros, based in Lebanon. For privacy questions, email <a href="mailto:jp@jeanpierreboutros.com">jp@jeanpierreboutros.com</a>.</p>
    <p>Optional Google Analytics helps us understand page visits, referral sources, devices, general geographic information and clicks on email, WhatsApp and the professional-profile download. A contact-link click does not mean a message was sent or a booking was made.</p>
    <p>The Google Analytics tag loads only after you allow optional analytics. We do not send email or WhatsApp message contents to Analytics. Page addresses sent by this implementation exclude query strings and fragments; referral addresses are reduced to their origin. Email and WhatsApp services process messages under their own policies.</p>
    <p>Your analytics choice is remembered in this browser for up to 180 days. If you allow analytics, Google Analytics may set cookies for up to 180 days. You can change your choice here; withdrawing permission stops this site's future analytics events and clears its Google Analytics cookies. Browser Do Not Track and Global Privacy Control signals keep optional analytics off.</p>
    <p>The hosting provider also handles ordinary web requests and server logs to deliver and protect the website. Information you send in a project inquiry is used to respond to that inquiry. Google's processing is explained in <a href="https://policies.google.com/technologies/partner-sites" target="_blank" rel="noopener noreferrer">How Google uses information from sites that use its services<span class="sr-only"> (opens in a new tab)</span></a>. This site's analytics are not configured for advertising personalization.</p>
    <p class="analytics-status" data-analytics-status></p>
    <button class="text-link privacy-change" type="button" data-analytics-settings hidden>Change analytics choice</button>
  </div>
</details>
<section class="analytics-choice" aria-labelledby="analytics-choice-title" hidden>
  <h2 id="analytics-choice-title">Optional analytics</h2>
  <p>Allow Google Analytics to help measure visits and contact-link usage? The Google tag stays off unless you allow it.</p>
  <div class="analytics-actions"><button type="button" data-analytics-reject>Reject analytics</button><button type="button" data-analytics-accept>Allow analytics</button><a href="#privacy-details" data-analytics-details>Details</a></div>
</section>'''
