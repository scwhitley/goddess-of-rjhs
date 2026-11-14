# Goddess of RJHS: website refresh concepts

Refresh mockups by Distorted Web for **RJHS Holistic Healing & Wellness** (Janee, Goddess Of RJHS), Wake Forest, NC.
Current site: https://goddessofrjhs.com/ (GoDaddy Website Builder). Brief: a completely new modern look, keeping every word, image and testimonial the same.

Plain HTML and CSS, no build needed to view. Deploy the repo root as-is (Netlify, GitHub Pages, etc).

| Path | Concept | Price |
| --- | --- | --- |
| `/` | Chooser page linking all three | n/a |
| `/link/` | Link page with pop-ups (for social bios) | Site Refresh, from $75 |
| `/one-page/` | One scrolling page with pop-ups | Site Refresh, from $75 |
| `/full/` | Five pages matching today's site: RJHS, Meet Janee, Individual Sessions, Events, Testimonials | Site Refresh, from $75 |

## Editing
- Contact details and the session packages live in `tools/site.template.js` (`BIZ`, `PACKAGES`).
- Testimonials live in `tools/testimonials.json`.
- One-pager and full-site pages are generated: edit `tools/build.py`, then run `python3 tools/build.py`. The link page and chooser are hand-written.

## Design
- Warm ivory paper, deep plum ink, her lavender kept as the soft accent, muted gold for Book buttons.
- Cormorant Garamond headlines over DM Sans. Arch-shaped photo frames are the signature shape.
- The full site has its own dark "night sanctuary" theme (`assets/css/full.css`): utility bar, full-bleed photo hero, arch page tiles and photo banners, so it reads clearly different from the light one-pager.

## Client content in use (copied verbatim)
- Home hero quote, Meet Janee story, Individual Sessions welcome and booking information, Our Privacy Promise, all 10 testimonials, address, phone, email, socials, copyright line.
- Credentials line from her Square booking page.
- Photos: the homepage headshot and the Meet Janee photo (EXIF/GPS stripped). Her old banner is kept in `assets/img/original-banner.jpg` for reference only.

## Still to fill in
- Client Login (header, footer, link page) points at her Square site for now. Replaces the GoDaddy account portal, which can't move off GoDaddy. Turn on customer accounts in Square Online, then set `BIZ.login` in `tools/site.template.js` to her exact Square sign-in page.
- Session packages and prices (`PACKAGES`), from her Square booking page. Until then each page shows the booking button.
- Events: the current Events page is empty, so the mockup shows an empty state with the newsletter signup.
- Terms and Conditions links to her current page (its text isn't in the page source).
- Forms show a confirmation only. Hook up Netlify forms when live.
