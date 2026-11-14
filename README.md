# Goddess of RJHS: website refresh concepts

Refresh mockups by Distorted Web for **RJHS Holistic Healing & Wellness** (Janee, Goddess Of RJHS), Wake Forest, NC.
Current site: https://goddessofrjhs.com/ (GoDaddy Website Builder). Brief: a completely new modern look, keeping every word, image and testimonial the same.

Plain HTML and CSS, no build needed to view. Deploy the repo root as-is (Netlify, GitHub Pages, etc).

| Path | Concept | Package |
| --- | --- | --- |
| `/` | Chooser page linking all three | n/a |
| `/link/` | Link page with pop-ups (for social bios) | Link Page, from $100 |
| `/one-page/` | One scrolling page with pop-ups | One-Pager, from $200 |
| `/full/` | Five pages matching today's site: RJHS, Meet Janee, Individual Sessions, Events, Testimonials | Full Website, from $300 |

## Editing
- Contact details and the session packages live in `tools/site.template.js` (`BIZ`, `PACKAGES`).
- Testimonials live in `tools/testimonials.json`.
- One-pager and full-site pages are generated: edit `tools/build.py`, then run `python3 tools/build.py`. The link page and chooser are hand-written.

## Design
- Warm ivory paper, deep plum ink, her lavender kept as the soft accent, muted gold for Book buttons.
- Cormorant Garamond headlines over DM Sans. Arch-shaped photo frames are the signature shape.

## Client content in use (copied verbatim)
- Home hero quote, Meet Janee story, Individual Sessions welcome and booking information, Our Privacy Promise, all 10 testimonials, address, phone, email, socials, copyright line.
- Credentials line from her Square booking page.
- Photos: the homepage headshot and the Meet Janee photo (EXIF/GPS stripped). Her old banner is kept in `assets/img/original-banner.jpg` for reference only.

## Still to fill in
- Session packages and prices (`PACKAGES`), from her Square booking page. Until then each page shows the booking button.
- Events: the current Events page is empty, so the mockup shows an empty state with the newsletter signup.
- Terms and Conditions links to her current page (its text isn't in the page source).
- Forms show a confirmation only. Hook up Netlify forms when live.
