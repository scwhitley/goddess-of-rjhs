#!/usr/bin/env python3
"""Builds every page of the Goddess of RJHS concepts.

All client wording is copied word for word from goddessofrjhs.com and her Square booking page.
Run from anywhere:  python3 tools/build.py
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
T = json.loads((ROOT / "tools/testimonials.json").read_text(encoding="utf8"))

# ---- site.js: inject testimonials into the template ----
js = (ROOT / "tools/site.template.js").read_text(encoding="utf8")
js = js.replace("/*TESTIMONIALS*/[]", json.dumps(T, ensure_ascii=False, indent=1))
(ROOT / "assets/js/site.js").write_text(js, encoding="utf8")

# ---- shared pieces ----
FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>\n'
         '  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600&display=swap">')

MARK_SVG = ('<svg viewBox="0 0 40 40" aria-hidden="true"><path d="M8 36V18a12 12 0 0 1 24 0v18" fill="none" stroke="currentColor" stroke-width="1.5"/>'
            '<path d="M20 12.5l1.7 5.8 5.8 1.7-5.8 1.7L20 27.5l-1.7-5.8-5.8-1.7 5.8-1.7z" fill="#b88a4f"/>'
            '<path d="M4 36h32" stroke="currentColor" stroke-width="1.5"/></svg>')

def mark(href, s=38):
    return (f'<a class="mark" href="{href}" style="--s:{s}px" aria-label="Goddess of RJHS home">{MARK_SVG}'
            '<span><b>Goddess <i>of</i> RJHS</b><small>Holistic Healing &amp; Wellness</small></span></a>')

SPARK = '<svg class="spark" viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2l2.2 7.8L22 12l-7.8 2.2L12 22l-2.2-7.8L2 12l7.8-2.2z" fill="currentColor"/></svg>'

RING = ('<svg class="ring" viewBox="0 0 120 120" aria-hidden="true"><defs><path id="c" d="M60 60m-46 0a46 46 0 1 1 92 0a46 46 0 1 1-92 0"/></defs>'
        '<circle cx="60" cy="60" r="58" fill="#2b1a33"/>'
        '<text font-family="DM Sans, sans-serif" font-size="10" fill="#f1e8f5"><textPath href="#c" textLength="286" lengthAdjust="spacing">WHERE HEALING MEETS SPIRIT ✦ RJHS HOLISTIC HEALING ✦</textPath></text>'
        '<path d="M60 47l2.6 10.4L73 60l-10.4 2.6L60 73l-2.6-10.4L47 60l10.4-2.6z" fill="#e4c793"/></svg>')

MODALITIES = ["End of Life Doula", "Usui/Holy Fire III Reiki Master Teacher", "Shamanic Practitioner",
              "Intuitive Spiritual Coach", "Angelic Reiki®", "Healing", "Clarity", "Spiritual Alignment"]

CREDS = ["Shamanic Practitioner", "Intuitive Coach", "Certified End-of-Life (EOL) Doula", "Angelic Reiki®",
         "Usui/Holy Fire III Reiki Master-Teacher (RMT)"]

CONCEPT_BAR = '<div class="concept-bar">Website refresh concept for Goddess of RJHS, made by <a href="https://distortedbrands.com/web/">Distorted Web</a> · <a href="{up}">see all 3 versions</a></div>'


def head(title, desc, up, extra_css=""):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{desc}">
  <meta name="robots" content="noindex">
  <meta name="theme-color" content="#2b1a33">
  {FONTS}
  <link rel="stylesheet" href="{up}assets/css/base.css">
  {extra_css}
</head>"""


# ---------- content blocks (client text, verbatim) ----------
HERO_QUOTE = ("“Whether you’re navigating grief, emotional overwhelm, spiritual awakening, or simply seeking peace, "
              "this space was created to support your healing journey.”")

ABOUT_PARAS = [
    "Through grief, life transitions, and spiritual awakening, I learned what it truly means to heal while still showing up for others. That journey inspired me to create a space where people can feel seen, supported, and safe while navigating their own healing process.",
    "Whether you are seeking energetic support, spiritual guidance, emotional balance, grief support, or simply a moment to breathe and reconnect, my intention is to meet you exactly where you are with compassion, authenticity, and care.",
]
ABOUT_PULL = "You do not have to navigate healing, grief, or spiritual growth alone."
ABOUT_CLOSE = "This space was created for healing, growth, grounding, and transformation. I invite you to look around, explore the offerings, and trust whatever guided you here in the first place."
ABOUT_INTRO = "I’m Janee, Goddess Of RJHS, an End of Life Doula, Usui/Holy Fire III Reiki Master Teacher, Shamanic Practitioner, and Intuitive Spiritual Coach dedicated to helping people reconnect with themselves through healing, clarity, and spiritual alignment."

PRIVACY_INTRO = "The foundation of the RJHS platform begins and ends with trust and we pride ourselves in protecting the information of all clients. Our company embodies two main values as we strive to develop and maintain relationships with each client."
PRIVACY_TRUST = "We want you to trust that anything discussed between you and any of our staff members will not be discussed externally. We respect, and value your privacy. We understand your information belongs to you!"
PRIVACY_SEC = "We will not share/release your personal information with any outside/third party vendor unless consent is received from the client or legally mandated by the court of law. When we are legally required to share your personal information, we will tell you in advance, unless we are legally forbidden by a judge or court mandated documents."

SESS_INTRO = "Take your time to explore our offerings and discover all the ways we can support your healing journey. We encourage you to learn about the various sessions we provide."
SESS_EMAIL = 'If you don’t see an available time slot for your preferred date and time, please feel free to reach out to me at <a data-biz="email" href="#"></a>. I’m here to assist you!'
SESS_CLOSE = "We hope you enjoy your visit to our site! If you have any questions or need assistance, don’t hesitate to reach out."


def hero(links):
    return f"""
  <section class="hero">
    <div class="wrap hero-grid">
      <div>
        <span class="eyebrow">RJHS Holistic Healing &amp; Wellness</span>
        <h1 style="margin-top:22px">Where Healing <em>Meets Spirit...</em></h1>
        <blockquote>{HERO_QUOTE}<cite>- Janee, Goddess Of RJHS</cite></blockquote>
        <div class="ctas">
          <a class="btn btn-gold" data-biz="booking" href="#" target="_blank" rel="noopener"><span data-icon="cal"></span>Book Your Individual Session Today!</a>
          <a class="btn btn-ghost" href="{links['about']}">Meet Janee</a>
        </div>
      </div>
      <div class="hero-photo">
        <div class="arch"><img src="{links['up']}assets/img/hero.jpg" alt="Janee, Goddess Of RJHS" width="993" height="1400"></div>
        {RING}
        <div class="hero-badge"><b>Janee H Paige</b>{', '.join(CREDS[:3])}</div>
      </div>
    </div>
  </section>
  <div class="ribbon" aria-hidden="true"><div class="ribbon-track">{''.join(f'<span>{m}</span>' for m in MODALITIES * 2)}</div></div>"""


def about(up, full=True, more_href=None):
    paras = ABOUT_PARAS if full else ABOUT_PARAS[:1]
    rest = f"""
          <p class="pull">{ABOUT_PULL}</p>
          <p>{ABOUT_CLOSE}</p>
          <p class="sig">Your healing is sacred.<small>— Janee, Goddess Of RJHS</small></p>""" if full else f"""
          <p class="pull">{ABOUT_PULL}</p>
          <div><a class="btn btn-plum" href="{more_href}">Meet Janee</a></div>"""
    return f"""
  <section class="sec" id="meet-janee">
    <div class="wrap about">
      <div class="about-photo"><div class="arch"><img src="{up}assets/img/janee.jpg" alt="Janee leaning against a brick wall" loading="lazy" width="1050" height="1400"></div></div>
      <div class="about-copy">
        <span class="eyebrow">Meet Janee</span>
        <h2 style="font-size:clamp(40px,5.4vw,64px)">Welcome to RJHS <em>Holistic Healing &amp; Wellness.</em></h2>
        <p class="lead">{ABOUT_INTRO}</p>
        <div class="creds">{''.join(f'<span>{c}</span>' for c in CREDS)}</div>
        {''.join(f'<p>{p}</p>' for p in paras)}{rest}
      </div>
    </div>
  </section>"""


def sessions(form=True):
    right = """
        <div class="card">
          <h3>Lets Connect</h3>
          <div data-render="connect-form"></div>
        </div>""" if form else ""
    return f"""
  <section class="sec tint" id="sessions">
    <div class="wrap">
      <div class="sec-head">
        <span class="eyebrow">Individual Sessions</span>
        <h2>Welcome! <em>We're So Glad You're Here!</em></h2>
      </div>
      <div class="sessions">
        <div class="intro">
          <p style="font-size:18px">{SESS_INTRO}</p>
          <p>{SESS_EMAIL}</p>
          <div class="card">
            <h3>Important Booking Information:</h3>
            <ul class="booking-info" data-render="booking-info"></ul>
          </div>
          <p class="muted">{SESS_CLOSE}</p>
          <div><a class="btn btn-gold" data-biz="booking" href="#" target="_blank" rel="noopener"><span data-icon="cal"></span>Book Your Individual Session Today!</a></div>
        </div>
        <div class="intro">
          <div class="packages" data-render="packages"></div>{right}
        </div>
      </div>
    </div>
  </section>"""


def testimonials_carousel(all_href=None):
    link = f'<a class="btn btn-ghost" href="{all_href}">All testimonials</a>' if all_href else ""
    return f"""
  <section class="sec" id="testimonials">
    <div class="wrap">
      <div class="sec-head row">
        <div><span class="eyebrow">Testimonials</span><h2>Empower Your Spirit <em>with Janee</em></h2></div>
        <div style="display:flex;gap:12px;align-items:center">{link}<div class="car-nav"><button type="button" data-dir="-1" aria-label="Previous"></button><button type="button" data-dir="1" aria-label="Next"></button></div></div>
      </div>
      <div class="carousel"><div class="track" data-render="testimonial-cards"></div></div>
    </div>
  </section>"""


def privacy():
    return f"""
  <section class="sec privacy" id="privacy">
    <div class="wrap">
      <div class="sec-head">
        <span class="eyebrow">RJHS</span>
        <h2>Our Privacy <em>Promise</em></h2>
        <p>{PRIVACY_INTRO}</p>
      </div>
      <div class="pillars">
        <div class="pillar"><span data-icon="shield"></span><h3>Trust</h3><p>{PRIVACY_TRUST}</p></div>
        <div class="pillar"><span data-icon="lock"></span><h3>Information Security</h3><p>{PRIVACY_SEC}</p></div>
      </div>
    </div>
  </section>"""


def connect(form=True):
    second = """
      <div class="card">
        <span class="eyebrow">Lets Connect</span>
        <h2>Lets <em>Connect</em></h2>
        <div data-render="connect-form"></div>
      </div>""" if form else ""
    return f"""
  <section class="sec lav" id="connect">
    <div class="wrap connect" style="{'' if form else 'grid-template-columns:1fr;max-width:760px'}">
      <div class="card">
        <span class="eyebrow">Stay connected</span>
        <h2>Stay <em>connected</em></h2>
        <div data-render="subscribe-form"></div>
        <div class="contact-lines">
          <a data-biz="phone" href="#"><span data-icon="phone"></span><span>984-268-8660</span></a>
          <a data-biz="email" href="#"><span data-icon="mail"></span><span>goddessofrjhs@rjhsinc.com</span></a>
          <a data-biz="map" href="#" target="_blank" rel="noopener"><span data-icon="pin"></span><span>620 Dr.Calvin Jones Highway Suite 204, Wake Forest, NC 27587</span></a>
        </div>
        <div class="socials" data-render="socials"></div>
      </div>{second}
    </div>
  </section>"""


def footer(links):
    nav = "".join(f'<li><a href="{h}">{n}</a></li>' for n, h in links["nav"])
    return f"""
  <footer class="foot">
    <div class="wrap">
      <div class="foot-grid">
        <div style="display:grid;gap:18px;align-content:start">
          {mark(links['home'], 44).replace('class="mark"', 'class="mark" style="color:#fff;--s:44px"')}
          <p style="max-width:34ch">RJHS Holistic Healing &amp; Wellness</p>
          <div class="socials" data-render="socials"></div>
        </div>
        <div><h4>Explore</h4><ul>{nav}<li><a data-biz="terms" href="#" target="_blank" rel="noopener">Terms and Conditions</a></li></ul></div>
        <div><h4>Visit</h4><ul>
          <li><a data-biz="map" href="#" target="_blank" rel="noopener">620 Dr.Calvin Jones Highway Suite 204, Wake Forest, NC 27587</a></li>
          <li><a data-biz="phone" href="#">984-268-8660</a></li>
          <li><a data-biz="email" href="#">goddessofrjhs@rjhsinc.com</a></li>
        </ul></div>
      </div>
      <div class="foot-base"><span>Copyright © 2022 RJHS,llc - All Rights Reserved.</span><span>Site by <a href="https://distortedbrands.com/web/">Distorted Web</a></span></div>
    </div>
  </footer>"""


QUOTE_POP = """
  <dialog class="pop" id="quote-pop" aria-labelledby="quote-pop-title">
    <div class="pop-head"><h2 id="quote-pop-title">Testimonial</h2><button class="pop-close" type="button" aria-label="Close"></button></div>
    <div class="pop-body"></div>
  </dialog>"""


def header(links, current=None):
    items = "".join(
        f'<a href="{h}"{" aria-current=\"page\"" if n == current else ""}>{n}</a>' for n, h in links["nav"])
    return f"""
  <header class="top">
    <div class="wrap">
      {mark(links['home'])}
      <nav class="nav" aria-label="Main">{items}<a class="btn btn-gold" data-biz="booking" href="#" target="_blank" rel="noopener">Book a Session</a></nav>
      <button class="nav-toggle" type="button" aria-label="Menu" aria-expanded="false"><span></span><span></span><span></span></button>
    </div>
  </header>"""


def write(path, html):
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(html, encoding="utf8")
    print("wrote", path)


# =====================================================================
# One-pager
# =====================================================================
op_links = {"up": "../", "home": "#top", "about": "#meet-janee",
            "nav": [("Meet Janee", "#meet-janee"), ("Individual Sessions", "#sessions"),
                    ("Testimonials", "#testimonials"), ("Lets Connect", "#connect")]}
write("one-page/index.html", f"""{head("Goddess of RJHS | RJHS Holistic Healing & Wellness", "Where Healing Meets Spirit. Reiki, shamanic healing, end of life doula support and intuitive spiritual coaching with Janee in Wake Forest, NC.", "../", '<link rel="stylesheet" href="../assets/css/pages.css">')}
<body id="top">
  {CONCEPT_BAR.format(up="../")}
  {header(op_links)}
  <main>
  {hero(op_links)}
  {about("../")}
  {sessions(form=False)}
  {testimonials_carousel()}
  {privacy()}
  {connect()}
  </main>
  {footer(op_links)}
  {QUOTE_POP}
  <script src="../assets/js/site.js"></script>
</body>
</html>
""")

# =====================================================================
# Full site (5 pages, same structure as her current site)
# =====================================================================
fs = {"up": "../", "home": "index.html", "about": "meet-janee.html",
      "nav": [("RJHS", "index.html"), ("Meet Janee", "meet-janee.html"), ("Individual Sessions", "sessions.html"),
              ("Events", "events.html"), ("Testimonials", "testimonials.html")]}
CSS2 = '<link rel="stylesheet" href="../assets/css/pages.css">'


def page(file, title, current, body):
    write(f"full/{file}", f"""{head(title, "Where Healing Meets Spirit. RJHS Holistic Healing & Wellness with Janee, Goddess Of RJHS, in Wake Forest, NC.", "../", CSS2)}
<body>
  {CONCEPT_BAR.format(up="../")}
  {header(fs, current)}
  <main>{body}
  </main>
  {footer(fs)}
  {QUOTE_POP}
  <script src="../assets/js/site.js"></script>
</body>
</html>
""")


SESS_TEASER = f"""
  <section class="sec tint">
    <div class="wrap cta-band">
      <span class="eyebrow">Individual Sessions</span>
      <h2>Welcome! <em>We're So Glad You're Here!</em></h2>
      <p class="muted" style="max-width:620px;font-size:18px">{SESS_INTRO}</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center">
        <a class="btn btn-gold" data-biz="booking" href="#" target="_blank" rel="noopener"><span data-icon="cal"></span>Book Your Individual Session Today!</a>
        <a class="btn btn-ghost" href="sessions.html">Important Booking Information</a>
      </div>
    </div>
  </section>"""

page("index.html", "Goddess of RJHS | RJHS Holistic Healing & Wellness", "RJHS",
     hero(fs) + about("../", full=False, more_href="meet-janee.html") + SESS_TEASER
     + testimonials_carousel("testimonials.html") + privacy() + connect(form=False))

page("meet-janee.html", "Meet Janee | Goddess of RJHS", "Meet Janee",
     f"""
  <section class="page-hero"><span class="eyebrow">Meet Janee</span><h1>Your healing <em>is sacred.</em></h1></section>"""
     + about("../").replace('<section class="sec" id="meet-janee">', '<section class="sec" id="meet-janee" style="padding-top:20px">')
     + f"""
  <section class="sec lav"><div class="wrap cta-band">{SPARK}<h2>You do not have to navigate healing, grief, or spiritual growth <em>alone.</em></h2>
    <a class="btn btn-gold" data-biz="booking" href="#" target="_blank" rel="noopener"><span data-icon="cal"></span>Book Your Individual Session Today!</a></div></section>""")

page("sessions.html", "Individual Sessions | Goddess of RJHS", "Individual Sessions",
     """
  <section class="page-hero"><span class="eyebrow">RJHS Holistic Healing &amp; Wellness</span><h1>Individual <em>Sessions</em></h1></section>"""
     + sessions(form=True).replace('class="sec tint" id="sessions"', 'class="sec" id="sessions" style="padding-top:20px"'))

page("events.html", "Events | Goddess of RJHS", "Events",
     """
  <section class="page-hero"><span class="eyebrow">RJHS Holistic Healing &amp; Wellness</span><h1><em>Events</em></h1></section>
  <section class="sec" style="padding-top:10px"><div class="wrap">
    <div class="card empty">
      <span data-icon="cal"></span>
      <h2>Events</h2>
      <p class="muted">Upcoming events will show here.</p>
      <h3 style="font-size:26px;margin-top:10px">Stay connected</h3>
      <div style="width:min(520px,100%)" data-render="subscribe-form"></div>
    </div>
  </div></section>""")

page("testimonials.html", "Testimonials | Goddess of RJHS", "Testimonials",
     """
  <section class="page-hero"><span class="eyebrow">Testimonials</span><h1>Empower Your Spirit <em>with Janee</em></h1></section>
  <section class="sec" style="padding-top:10px"><div class="wrap"><div class="quote-grid" data-render="testimonial-full"></div></div></section>
  <section class="sec lav"><div class="wrap cta-band"><h2>Book Your Individual Session <em>Today!</em></h2>
    <a class="btn btn-gold" data-biz="booking" href="#" target="_blank" rel="noopener"><span data-icon="cal"></span>Book a Session</a></div></section>""")

print("done")
