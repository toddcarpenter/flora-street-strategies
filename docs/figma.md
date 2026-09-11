# Flora Street Strategies — Figma File Spec

This document describes the frames, components, and tokens needed for a Figma version of the redesign. If you share a Figma account/token, I can create/update the file directly; otherwise this spec can be used to build it manually.

## File structure

```
Flora Street Strategies — Redesign
├── 00 Cover
├── 01 Design Tokens
│   ├── Colors
│   ├── Typography
│   └── Spacing + Shadows
├── 02 Components
│   ├── Button / Primary
│   ├── Button / Secondary
│   ├── Service Card
│   ├── Quote Card
│   ├── Grant List Item
│   ├── Section Heading
│   └── Navigation Bar
└── 03 Pages
    ├── Home
    ├── Services
    ├── About
    ├── Testimonials & Results
    └── Contact
```

## Page frames (desktop 1440×auto, mobile 375×auto)

### Home

1. **Nav bar** — logo left, links right, transparent background over hero.
2. **Hero section** — full-width warm beige/cream background. H1 + subhead + primary CTA. Emily photo on right or below on mobile.
3. **Services preview** — 4 service cards in a row. “Grant Strategy”, “HR & Admin Infrastructure”, “Recruitment & Hiring”, “Project Management”.
4. **About snippet** — headshot + short bio excerpt + link to About.
5. **Proof banner** — large number/stat (e.g., “11+ successful grants”) + CTA to Testimonials.
6. **Footer** — contact info, minimal links.

### Services

1. **Hero** — “Services that help your business flourish.”
2. **Service grid** — four detailed cards with descriptions.
3. **How it works** — 3-step process: Discover, Build, Apply/Operate.
4. **CTA section** — “Ready to grow?” + contact button.

### About

1. **Hero** — “Hi, I’m Emily.”
2. **Two-column layout** — headshot left, long-form bio right.
3. **Credentials** — wine certs, MS Hospitality, Philadelphia universities.
4. **CTA** — “Let’s talk about your business.”

### Testimonials & Results

1. **Hero** — “Client Reviews & Successful Grants.”
2. **Quote grid** — three quote cards.
3. **Grant logos / list** — 11 grant programs listed.
4. **CTA** — contact.

### Contact

1. **Hero** — “Let’s Talk.”
2. **Form** — Name, Email, Message.
3. **Contact details** — email + phone.

## Component specs

### Mobile Menu / Hamburger

- **Hamburger trigger** — 44×44px sage square, 10px radius, white `☰` icon, fixed top-right on mobile.
- **Overlay** — full-screen sage panel (`position: fixed; inset: 0; min-height: 100vh`), vertically centered cream links.
- **Close button** — 44×44px cream circle, sage `×`, top-right 1.25rem.
- **Link style** — Georgia serif, `clamp(1.8rem, 8vw, 3rem)`, cream, hover terracotta.

### Button / Primary

- Text: “Get In Touch”, weight 600, white
- Background: `#b06943`
- Padding: 16px 32px
- Corner radius: 999
- Shadow: none

### Button / Secondary

- Text: “Learn More”, weight 600, `#60695f`
- Border: 2px `#60695f`
- Padding: 14px 30px
- Corner radius: 999

### Service Card

- Size: min 280 × auto
- Background: `#ffffff`
- Border: 1px `#e8e2db`
- Corner radius: 16
- Padding: 32
- Icon: 48×48 circle with sage fill, white icon

### Quote Card

- Background: `#e8e2db`
- Left accent: 4px `#b06943`
- Padding: 32
- Corner radius: 16

## Tokens

See `design-system.md` for the full color, type, and spacing values to add to Figma Variables.
