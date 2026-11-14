/* Goddess of RJHS — shared content and behavior for all three concepts.
   Everything a visitor reads here is copied word for word from goddessofrjhs.com.
   Edit content in this file (BIZ, PACKAGES); testimonials are generated from tools/testimonials.json
   by tools/build.py. */

const BIZ = {
  name: "RJHS Holistic Healing & Wellness",
  owner: "Janee, Goddess Of RJHS",
  phone: "984-268-8660",
  tel: "9842688660",
  email: "goddessofrjhs@rjhsinc.com",
  address: "620 Dr.Calvin Jones Highway Suite 204, Wake Forest, NC 27587",
  booking: "https://goddess-of-rjhs.square.site",
  terms: "https://goddessofrjhs.com/terms-and-conditions",
  socials: [
    { name: "Instagram", url: "https://www.instagram.com/goddess_of_RJHS", icon: "ig" },
    { name: "TikTok", url: "https://www.tiktok.com/@GODDESS_OF_RJHS", icon: "tt" },
    { name: "Facebook", url: "https://www.facebook.com/104971604897944", icon: "fb" },
    { name: "YouTube", url: "https://www.youtube.com/GODDESS_OF_RJHS", icon: "yt" },
    { name: "X", url: "https://www.x.com/goddess_of_rjhs", icon: "x" },
  ],
};

/* Session packages from her Square booking page. Fill these in from the client's list:
   { name: "Reiki Session", price: "$00", duration: "60 min", description: "..." }
   While the list is empty, every page shows the booking button instead of cards. */
const PACKAGES = [];

const TESTIMONIALS = /*TESTIMONIALS*/[];

/* ---------- icons ---------- */
const ICON = {
  ig: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>',
  tt: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M16.6 3c.4 2.2 1.8 3.6 4 3.8v3.1c-1.5.1-2.8-.4-4-1.2v6.2c0 3.5-2.6 6.1-6 6.1a5.9 5.9 0 0 1-6-6c0-3.6 3-6.3 6.7-5.9v3.2c-1.9-.4-3.5.9-3.5 2.7 0 1.6 1.2 2.8 2.8 2.8 1.7 0 2.9-1.2 2.9-3.2V3h3.1z"/></svg>',
  fb: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 21v-7.5h2.6l.4-3h-3V8.6c0-.9.3-1.5 1.5-1.5h1.6V4.4c-.3 0-1.2-.1-2.3-.1-2.3 0-3.9 1.4-3.9 4v2.2H7.8v3h2.6V21h3.1z"/></svg>',
  yt: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2a2.6 2.6 0 0 0-1.8-1.8C18.2 5 12 5 12 5s-6.2 0-7.8.4A2.6 2.6 0 0 0 2.4 7.2C2 8.8 2 12 2 12s0 3.2.4 4.8a2.6 2.6 0 0 0 1.8 1.8C5.8 19 12 19 12 19s6.2 0 7.8-.4a2.6 2.6 0 0 0 1.8-1.8c.4-1.6.4-4.8.4-4.8s0-3.2-.4-4.8zM10 15V9l5.2 3L10 15z"/></svg>',
  x: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.8 3h3.1l-6.8 7.8L22 21h-6.2l-4.9-6.4L5.3 21H2.2l7.3-8.3L2 3h6.4l4.4 5.8L17.8 3zm-1.1 16.2h1.7L7.4 4.7H5.6l11.1 14.5z"/></svg>',
  phone: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1.9.4 1.8.7 2.7a2 2 0 0 1-.5 2.1L8 9.8a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.7.7a2 2 0 0 1 1.7 2z"/></svg>',
  mail: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="4" width="20" height="16" rx="3"/><path d="m22 7-10 6L2 7"/></svg>',
  pin: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M20 10c0 6-8 12-8 12S4 16 4 10a8 8 0 1 1 16 0z"/><circle cx="12" cy="10" r="3"/></svg>',
  cal: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="3"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
  card: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="5" width="20" height="14" rx="3"/><path d="M2 10h20"/></svg>',
  shield: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
  lock: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><rect x="4" y="11" width="16" height="11" rx="3"/><path d="M8 11V7a4 4 0 0 1 8 0v4"/></svg>',
  check: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><path d="m8 12 3 3 5-6"/></svg>',
  arrowL: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M15 18l-6-6 6-6"/></svg>',
  arrowR: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18l6-6-6-6"/></svg>',
  close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M18 6 6 18M6 6l12 12"/></svg>',
  star: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8L12 17.8 5.8 21l1.2-6.8-5-4.9 6.9-1z"/></svg>',
};

const esc = (s) => String(s).replace(/[&<>"]/g, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const stars = () => '<div class="stars" aria-hidden="true">' + ICON.star.repeat(5) + "</div>";

/* ---------- renderers (fill any element with a data-render attribute) ---------- */
const RENDER = {
  socials: () => BIZ.socials.map((s) => `<a href="${s.url}" target="_blank" rel="noopener" aria-label="${s.name}">${ICON[s.icon]}</a>`).join(""),

  "testimonial-cards": (el) => {
    const n = el.dataset.limit ? +el.dataset.limit : TESTIMONIALS.length;
    return TESTIMONIALS.slice(0, n).map((t, i) => `
      <article class="card quote">
        ${stars()}
        <h3>${esc(t.title)}</h3>
        <p class="clamp">${esc(t.body.join(" "))}</p>
        <button class="more" type="button" data-quote="${i}">Read the full story</button>
      </article>`).join("");
  },

  "testimonial-full": () => TESTIMONIALS.map((t) => `
      <article class="card quote">
        ${stars()}
        <h3>${esc(t.title)}</h3>
        ${t.body.map((p) => `<p>${esc(p)}</p>`).join("")}
      </article>`).join(""),

  packages: () => {
    if (!PACKAGES.length) {
      return `<div class="card pkg-slot">
          ${ICON.cal.replace("<svg", '<svg class="spark" style="width:30px;height:30px;color:var(--violet)"')}
          <h3 style="font-size:28px">Session menu</h3>
          <p>Janee's sessions, prices and times are pulled straight from her booking calendar.</p>
          <a class="btn btn-gold" href="${BIZ.booking}" target="_blank" rel="noopener">Book Your Individual Session Today!</a>
        </div>`;
    }
    return PACKAGES.map((p) => `
      <article class="card pkg">
        ${p.duration ? `<span class="dur">${esc(p.duration)}</span>` : ""}
        <h3 style="font-size:28px">${esc(p.name)}</h3>
        ${p.price ? `<span class="price">${esc(p.price)}</span>` : ""}
        ${p.description ? `<p class="muted">${esc(p.description)}</p>` : ""}
        <a class="btn btn-plum" href="${BIZ.booking}" target="_blank" rel="noopener">Book</a>
      </article>`).join("");
  },

  "booking-info": () => `
    <li>${ICON.card}<span>Full payment is required at the time of booking.</span></li>
    <li>${ICON.shield}<span>Please note that once a session is booked, refunds are not available.</span></li>
    <li>${ICON.mail}<span>If you do not receive a confirmation email within 24 hours of your booking, kindly contact me to verify that your information was received correctly.</span></li>`,

  "connect-form": () => `
    <form class="form" data-form="connect">
      <div class="field"><label for="cf-name">Name*</label><input id="cf-name" name="name" autocomplete="name" required></div>
      <div class="field"><label for="cf-phone">Phone*</label><input id="cf-phone" name="phone" type="tel" autocomplete="tel" required></div>
      <div class="field"><label for="cf-email">Email*</label><input id="cf-email" name="email" type="email" autocomplete="email" required></div>
      <button class="btn btn-plum" type="submit">Send</button>
      <p class="fine">This site is protected by reCAPTCHA and the Google <a href="https://policies.google.com/privacy" target="_blank" rel="noopener">Privacy Policy</a> and <a href="https://policies.google.com/terms" target="_blank" rel="noopener">Terms of Service</a> apply.</p>
    </form>
    <div class="form-done" hidden><h3 style="font-size:28px">Thank you.</h3><p class="muted">Janee will be in touch soon.</p></div>`,

  "subscribe-form": () => `
    <form class="subscribe" data-form="subscribe">
      <label class="sr" for="sub-email" style="position:absolute;left:-9999px">Your Email Address</label>
      <input id="sub-email" type="email" placeholder="Your Email Address" autocomplete="email" required>
      <button class="btn btn-gold" type="submit">Join Now</button>
    </form>
    <p class="form-done" hidden style="margin-top:12px">You're on the list.</p>`,
};

/* ---------- behavior ---------- */
function openDialog(id) {
  const d = document.getElementById(id);
  if (!d) return;
  d.showModal();
  document.body.classList.add("modal-open");
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-render]").forEach((el) => {
    const fn = RENDER[el.dataset.render];
    if (fn) el.innerHTML = fn(el);
  });
  document.querySelectorAll("[data-icon]").forEach((el) => { el.innerHTML = ICON[el.dataset.icon] || ""; });
  document.querySelectorAll("[data-biz]").forEach((el) => {
    const k = el.dataset.biz;
    if (k === "phone") { el.href = "tel:" + BIZ.tel; if (!el.textContent.trim()) el.textContent = BIZ.phone; }
    else if (k === "email") { el.href = "mailto:" + BIZ.email; if (!el.textContent.trim()) el.textContent = BIZ.email; }
    else if (k === "booking") el.href = BIZ.booking;
    else if (k === "terms") el.href = BIZ.terms;
    else if (k === "address") el.textContent = BIZ.address;
    else if (k === "map") el.href = "https://maps.google.com/?q=" + encodeURIComponent(BIZ.address);
  });
  document.querySelectorAll("[data-year]").forEach((el) => (el.textContent = "2022"));

  // Dialog open/close
  document.addEventListener("click", (e) => {
    const opener = e.target.closest("[data-open]");
    if (opener) { e.preventDefault(); openDialog(opener.dataset.open); return; }
    const q = e.target.closest("[data-quote]");
    if (q) {
      const t = TESTIMONIALS[+q.dataset.quote];
      const d = document.getElementById("quote-pop");
      if (d && t) {
        d.querySelector("h2").textContent = t.title;
        d.querySelector(".pop-body").innerHTML = stars() + t.body.map((p) => `<p>${esc(p)}</p>`).join("");
        openDialog("quote-pop");
      }
      return;
    }
    if (e.target.closest(".pop-close")) e.target.closest("dialog").close();
  });
  document.querySelectorAll("dialog.pop").forEach((d) => {
    d.addEventListener("close", () => document.body.classList.remove("modal-open"));
    d.addEventListener("click", (e) => { if (e.target === d) d.close(); });
    const close = d.querySelector(".pop-close");
    if (close) close.innerHTML = ICON.close;
  });

  // Forms (mockup: show confirmation only)
  document.addEventListener("submit", (e) => {
    const f = e.target.closest("[data-form]");
    if (!f) return;
    e.preventDefault();
    f.hidden = true;
    const done = f.parentElement.querySelector(".form-done");
    if (done) done.hidden = false;
  });

  // Carousels
  document.querySelectorAll(".carousel").forEach((c) => {
    const track = c.querySelector(".track");
    (c.closest("section") || c).querySelectorAll("[data-dir]").forEach((b) => {
      b.innerHTML = b.dataset.dir === "-1" ? ICON.arrowL : ICON.arrowR;
      b.addEventListener("click", () => {
        const step = track.firstElementChild ? track.firstElementChild.getBoundingClientRect().width + 18 : 300;
        track.scrollBy({ left: step * +b.dataset.dir, behavior: "smooth" });
      });
    });
  });

  // Mobile nav
  const toggle = document.querySelector(".nav-toggle");
  if (toggle) toggle.addEventListener("click", () => {
    const open = document.body.classList.toggle("nav-open");
    toggle.setAttribute("aria-expanded", open);
  });
});
