# Sharing the Redesign with Emily

## Public preview

The redesign is published as part of the existing toddl.es static site:

```text
https://toddl.es/florastreetstrategies/
```

No separate subdomain, Cloudflare tunnel, or Flora Docker stack is required for public access. The files served publicly are in:

```text
C:\sites\toddl.es\site\florastreetstrategies\
```

## Local previews

Through the toddl.es Docker stack:

```text
http://localhost:8088/florastreetstrategies/
```

Or through the optional standalone Flora stack:

```text
http://localhost:8090/
```

## Mobile and desktop views

1. **Desktop:** open the public or local URL in a normal browser window.
2. **Mobile:** open the same URL on a phone or use Chrome/Edge DevTools device emulation.
3. **Mobile menu:** use the sage hamburger button to open the full-screen navigation.

## Search-engine restriction

The preview remains blocked from indexing:

- The toddl.es root `robots.txt` disallows `/florastreetstrategies/`.
- Every Flora page includes `noindex, nofollow, noarchive` metadata.

See `docs/go-live.md` before moving the design to its final production domain.
