# Flora Street Strategies — Before / After Comparison

## Before: current Squarespace site

The current site is a clean but template-driven Squarespace page with five sections: Home, Services, About, Testimonials, Contact. It uses Emily’s brand colors and logo but has a lot of placeholder content and minimal hierarchy.

### Current site pages

- `site/before/index.html` — Home
- `site/before/services/index.html` — Services
- `site/before/about/index.html` — About
- `site/before/testimonials/index.html` — Testimonials
- `site/before/contact/index.html` — Contact

### Observations

- **Home**: one hero + emblem + CTA. No social proof above the fold.
- **Services**: the intro is repeated but service details are thin.
- **About**: long bio block with no visual breaks.
- **Testimonials**: placeholder quotes; grant list has placeholder descriptions.
- **Contact**: form fields are minimal; layout is very plain.

## After: redesign proposal

The redesign keeps the existing copy and brand assets but restructures the site to be warmer, more personal, and easier to scan. It is inspired by the reference sites Emily shared.

### Design changes

| Element | Before | After |
|---------|--------|-------|
| Hero | Large heading + short paragraph | Heading + subhead + Emily’s photo + two CTAs |
| Services | Reused intro, vague sections | Four clear service cards + engagement models |
| About | One long text block | Two-column layout with headshot + credentials |
| Testimonials | Placeholder quotes | Quote cards + clean grant list |
| Contact | Simple form | Form + contact details with better visual treatment |
| Navigation | Standard links | Sticky header with redesigned labels |
| Typography | Sans-serif only | Serif headings + clean sans-serif body |
| Color use | Mostly beige/white | Warm cream background, terracotta CTAs, sage accents |
| Imagery | Logo + emblem | Emily’s photo featured on Home and About |

### Key principles

1. **Personality first** — Emily’s photo and voice are central, not stock imagery.
2. **Clear services** — each offering has its own card and description.
3. **Proof** — the successful grants list is turned into a prominent stat/result section.
4. **Warm minimalism** — generous whitespace, rounded corners, soft palette.

### Files

- `site/after/index.html` — Home
- `site/after/services/index.html` — Services
- `site/after/about/index.html` — About
- `site/after/testimonials/index.html` — Results
- `site/after/contact/index.html` — Contact
- `site/after/css/style.css` — redesign styles

## Next steps

1. Review both versions at `http://localhost:8088`.
2. Collect final brand assets from Emily (higher-resolution headshot, final logo, any brand guidelines).
3. Replace placeholder testimonials with real client quotes and names.
4. Write short descriptions for each grant/award.
5. Decide on a contact form backend (Formspree, Netlify Forms, Squarespace form, etc.).
6. Port the redesign into a real Figma file (or build directly into the final production site).
