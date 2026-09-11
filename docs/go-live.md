# Go-Live Checklist

When Emily approves the redesign and it’s time to launch the new site on her real domain (`florastreetstrategies.com`), run through this list.

## Before launch

- [ ] Replace placeholder content
  - [ ] Swap in Emily’s final brand assets (logo, headshot, colors, fonts)
  - [ ] Replace placeholder testimonials with real client quotes and names
  - [ ] Add real descriptions to the grant list items
  - [ ] Update contact form action/backend (currently uses `mailto:` for the prototype)
- [ ] Final review on desktop and mobile
- [ ] Spell-check all copy

## Accessibility / ADA

- [ ] Run an audit with axe DevTools or Lighthouse
- [ ] Full keyboard-only test
- [ ] Screen reader pass on the mobile menu, form, and headings
- [ ] Verify color contrast ratios
- [ ] See [`docs/accessibility-and-seo.md`](accessibility-and-seo.md) for full details

## Search / SEO

- [ ] Remove `site/robots.txt` or replace it with an allow-all `robots.txt`
- [ ] Remove `<meta name="robots" content="noindex, nofollow, noarchive">` from all HTML pages
- [ ] Remove `X-Robots-Tag` header from `nginx/default.conf`
- [ ] Update placeholder domain in OG / canonical / JSON-LD (`https://florastreetstrategies.com` should become the real production URL)
- [ ] Provide an absolute `og:image` URL
- [ ] Create and submit a sitemap

## Hosting / Domain

- [ ] Decide final hosting (Squarespace, self-hosted, etc.)
- [ ] If self-hosting: move the `site/` files to the production host
- [ ] Point `florastreetstrategies.com` (and `www`) to the production server
- [ ] Set up SSL/HTTPS
- [ ] If using the Cloudflare tunnel: update `cloudflared/config.yml` to use the production domain, or switch to direct DNS

## Analytics / monitoring

- [ ] Add any analytics or tracking Emily wants (Google Analytics, Plausible, etc.)
- [ ] Test contact form submissions
- [ ] Test all internal links

## After launch

- [ ] Verify the site loads over HTTPS
- [ ] Submit the live domain to Google/Bing for indexing
- [ ] Keep a rollback plan (previous Squarespace site or backup)
