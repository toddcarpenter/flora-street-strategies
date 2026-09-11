# Accessibility (ADA) & SEO Notes

The redesign has been built with accessibility and SEO fundamentals in mind. This file summarizes what is in place and what should be double-checked before the site goes live.

## Accessibility (ADA / WCAG 2.1 AA considerations)

### In place

- **Semantic HTML:** proper `<header>`, `<nav>`, `<main>`, `<section>`, `<footer>` usage.
- **Language:** `<html lang="en">` on every page.
- **Skip link:** a visually hidden “Skip to content” link appears on focus for keyboard users.
- **Focus management:**
  - `:focus-visible` outline using the terracotta accent color.
  - Mobile menu traps focus while open.
  - Opening the menu moves focus to the first link; closing returns focus to the hamburger button.
  - `Escape` key closes the mobile menu.
- **ARIA:**
  - `aria-label` on hamburger and close buttons.
  - `aria-expanded` toggled by JavaScript.
  - `aria-controls` pointing to the overlay.
  - `aria-current="page"` on the active navigation link.
- **Reduced motion:** `prefers-reduced-motion` media query disables animations and smooth scrolling for users who prefer reduced motion.
- **Form labels:** the contact form uses `<label>` elements visually hidden but available to screen readers, plus `aria-required`.
- **Alt text:** descriptive alt text on the logo, Emily’s headshot, and the emblem (decorative images have `alt=""`).

### Before go-live

- [ ] Run an automated audit with **axe DevTools** or **Lighthouse** and fix any new issues.
- [ ] Test the entire site with only a keyboard (no mouse).
- [ ] Run a screen reader pass (NVDA, JAWS, or VoiceOver) on:
  - [ ] Mobile menu open/close
  - [ ] Contact form submission
  - [ ] Navigation and headings
- [ ] Verify color contrast ratios, especially:
  - [ ] Sage text on warm-beige / cream backgrounds
  - [ ] Terracotta buttons and links
  - [ ] Placeholder text in form fields
- [ ] If the final design changes, re-check focus indicators and heading hierarchy.
- [ ] Confirm the contact form has a real backend or at minimum a working `mailto:` fallback.

## SEO

### In place

- **Unique `<title>`** and **`<meta name="description">`** on every page.
- **Open Graph** tags (`og:title`, `og:description`, `og:type`, `og:url`, `og:image`) and **Twitter Card** meta.
- **Canonical URLs** per page.
- **Favicon** referencing the brand emblem.
- **Theme color** meta for mobile browsers.
- **JSON-LD structured data:**
  - `ProfessionalService` schema on the home page.
  - `WebPage` schema on services, about, and results pages.
  - `ContactPage` schema on the contact page.
- **Clean URLs** and internal linking.
- **Preview blocking:** `robots.txt`, `X-Robots-Tag`, and `<meta robots="noindex">` prevent search engines from indexing the preview.

### Before go-live

- [ ] Remove or update `robots.txt` to allow crawling.
- [ ] Remove `<meta name="robots" content="noindex, nofollow, noarchive">` from all HTML pages.
- [ ] Remove `X-Robots-Tag` from `nginx/default.conf`.
- [ ] Update the placeholder domain in meta/OG/canonical links:
  - Currently `https://florastreetstrategies.com` — replace with the real production domain.
- [ ] Provide an absolute `og:image` URL (currently points to `/images/emily.jpg` under the placeholder domain).
- [ ] Add a `sitemap.xml` and reference it in `robots.txt`.
- [ ] Register the live site with Google Search Console and submit the sitemap.
- [ ] Ensure 301 redirects from `www` or non-www to the canonical version.
- [ ] Add analytics if desired (Plausible, Google Analytics, Fathom, etc.).
