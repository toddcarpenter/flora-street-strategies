# Flora Street Strategies — Website Redesign

Static redesign for Flora Street Strategies, published as a directory within the existing `toddl.es` site.

## Project structure

| Path | Contents |
|------|----------|
| `site/` | Complete redesign website and publishable source |
| `site/css/` | Shared styles |
| `site/js/` | Mobile navigation behavior |
| `site/images/` | Flora Street Strategies brand assets |
| `docs/` | Design, accessibility, SEO, content, and launch notes |
| `docs/archive/` | Archived source material from the original Squarespace site |
| `scripts/` | Local development helpers |
| `docker-compose.yml` | Optional standalone local preview |

## Local standalone preview

```powershell
powershell -ExecutionPolicy Bypass -File C:\sites\flora-street-strategies\scripts\start-static-only.ps1
```

Open `http://localhost:8090/`.

## toddl.es preview

The published copy lives at:

```text
C:\sites\toddl.es\site\florastreetstrategies\
```

It is served by the existing toddl.es stack at:

```text
https://toddl.es/florastreetstrategies/
```

For local testing through that stack, open `http://localhost:8088/florastreetstrategies/`.

All homepage links intentionally point to `/florastreetstrategies/` so the site works from the toddl.es subdirectory.

## Publishing updates

Deploy the contents of `site/` to the local `toddl.es` project with:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\deploy.ps1
```

The script copies the site to `C:\sites\toddl.es\site\florastreetstrategies\` and adds a timestamp cache version to local CSS, JavaScript, image, icon, and font references in the deployed HTML. Source files are not modified.

Use a custom destination or cache version when needed:

```powershell
.\scripts\deploy.ps1 -Destination "C:\path\to\site" -Version "preview-2"
```

## Project documentation

- [`docs/design-system.md`](docs/design-system.md) — redesign design system
- [`docs/figma.md`](docs/figma.md) — Figma-ready specification
- [`docs/audit.md`](docs/audit.md) — original-site audit
- [`docs/share.md`](docs/share.md) — preview and sharing instructions
- [`docs/go-live.md`](docs/go-live.md) — production launch checklist
- [`docs/accessibility-and-seo.md`](docs/accessibility-and-seo.md) — ADA and SEO notes
