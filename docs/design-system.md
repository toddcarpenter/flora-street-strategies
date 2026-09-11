# Flora Street Strategies — Design System

## Direction

A modern, warm, and professional redesign that keeps Emily’s personality at the center. The site should feel approachable and boutique — like a trusted strategist for small businesses — not a faceless agency. No stock photography; use Emily’s real headshot, the Flora Street logo, and the emblem.

### Inspiration summary

- **Mural City Cellars**: warm, personal, neighborhood-first tone.
- **Williams Grant Writing**: clear service breakdown and confident proof.
- **Great Hands Hospitality**: clean balance of biography + services.

## Color palette

| Token | Hex | HSL | Usage |
|-------|-----|-----|-------|
| `--color-cream` | `#fbf9f7` | `30, 24%, 97%` | Page backgrounds |
| `--color-surface` | `#ffffff` | | Cards, nav bar |
| `--color-warm-beige` | `#e8e2db` | `30, 24%, 90%` | Section accents, borders |
| `--color-terracotta` | `#b06943` | `14, 62%, 43%` | Primary CTAs, links, accents |
| `--color-terracotta-dark` | `#8f4f2f` | | Hover states |
| `--color-sage` | `#60695f` | `124, 8%, 40%` | Secondary buttons, headings |
| `--color-warm-brown` | `#a87c5d` | `23, 35%, 51%` | Muted headings, footer |
| `--color-text` | `#2c2a28` | | Body text |
| `--color-muted` | `#6b6560` | | Captions, secondary text |

## Typography

| Element | Font | Weight | Size | Line-height |
|---------|------|--------|------|-------------|
| H1 (hero) | Georgia, "Times New Roman", serif | 400 | `clamp(2.6rem, 6vw, 4.5rem)` | 1.05 |
| H2 | Georgia, "Times New Roman", serif | 400 | `clamp(1.8rem, 4vw, 2.8rem)` | 1.15 |
| H3 | system-ui, sans-serif | 600 | `1.25rem` | 1.3 |
| Body | system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif | 400 | `1.05rem` | 1.65 |
| Small / label | system-ui, sans-serif | 500 | `0.85rem` | 1.4 |

## Spacing

- Page max width: `1200px`
- Section padding: `5rem 1rem` (desktop), `3.5rem 1rem` (mobile)
- Grid gap: `2rem`
- Card padding: `2rem`
- Container side padding: `1.5rem`

## Components

### Mobile navigation

- **Trigger:** Sage-green rounded square button, 44×44px, with white hamburger icon (`☰`). Hidden on desktop; shown below 700px.
- **Overlay:** Full-screen fixed panel (`position: fixed; inset: 0; min-height: 100vh`) with sage background, centered stacked links in large cream serif type, close button (sage `×` on cream circle) top-right.
- **Behavior:** Click hamburger to open, click close or any link to close. Body scroll locked while open.

### Primary button

- Background: `--color-terracotta`
- Text: white
- Padding: `0.9rem 2rem`
- Border-radius: `999px`
- Hover: `--color-terracotta-dark`

### Secondary button

- Background: transparent
- Border: `2px solid --color-sage`
- Text: `--color-sage`
- Border-radius: `999px`

### Service card

- Background: `--color-surface`
- Border: `1px solid --color-warm-beige`
- Border-radius: `16px`
- Padding: `2rem`
- Subtle shadow: `0 6px 24px rgba(44,42,40,.05)`

### Quote card

- Background: `--color-warm-beige`
- Border-radius: `16px`
- Left border accent: `4px solid --color-terracotta`

## Responsive breakpoints

- Mobile: < 640px
- Tablet: 640px – 1024px
- Desktop: > 1024px

## Principles

1. **Personality first** — Emily’s photo and voice front and center.
2. **Clarity over cleverness** — services and proof are easy to scan.
3. **Warm minimalism** — lots of whitespace, rounded corners, soft palette.
4. **No stock images** — only real brand assets.
