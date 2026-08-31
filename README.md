# dans.ch

Personal site of Daniel Scheidemantel Camargo — <https://www.dans.ch>

Static HTML, CSS and vanilla JavaScript. No build step, no `node_modules`,
no package manager. Deployed straight from this repository to GitHub Pages.

## Stack

| Concern | Choice |
| --- | --- |
| Markup | Hand-written HTML5, one file per page |
| Styles | `design-system/variables.css` (tokens) + `assets/style.css` |
| Behaviour | `assets/app.js` — ~300 lines, no framework |
| Icons | `assets/icons.svg` sprite, inlined into every page |
| Type | Inter + JetBrains Mono (Google Fonts) |
| Brand | `assets/images/dsc_mark.svg` (cyan) — Capellaris keeps the blue `dsc_white.svg` |
| Background | three.js + Vanta NET, lazy-loaded after first paint |
| Offline | `sw.js` — network-first for documents, cache-first for assets |
| Forms | Formspree |
| Booking | TidyCal |

Nothing else is loaded. There is no jQuery, Bootstrap, Font Awesome, Swiper,
particles.js or GSAP — all removed in the 2026 rebuild.

## Pages

| Path | Contents |
| --- | --- |
| `index.html` | Hero, featured project, selected work, publications, booking CTA, contact |
| `curriculum.html` | Full CV — experience, skills, languages, education, teaching, publications |
| `chave.html`, `greenhop.html` | Research project write-ups |
| `files/` | Complete publication and course-material archive |
| `cloud/` | OpenStack course handouts |
| `blog/` | Writing — index, RSS feed, and `_template.html` (noindex) |
| `thanks.html` | Post-submission confirmation |
| `capellaris/` | Separate subsite with its own stylesheet and theme |

## Local development

```sh
make serve          # http://localhost:8080
make serve PORT=3000
make dev            # serve and open a browser
make stop
```

Any static server works; `make serve` is just `python3 -m http.server`.

## Notes

- The scroll walker, the rail and the section nodes only render at ≥1181px.
- `prefers-reduced-motion` disables the animated background, the walker
  animation and every reveal transition.
- Capellaris keeps the previous light theme and imports
  `design-system/legacy.css`. See `design-system/README.md` before touching
  either token file.
## Publishing a post

There is no build step, so a post is a file:

1. `cp blog/_template.html blog/<slug>.html`
2. Replace the title, `<meta name="description">`, canonical URL, date and body.
   Delete the `<meta name="robots">` line and the draft banner.
3. Add a `<li class="post-item">` to `blog/index.html` (the commented block there
   shows the shape) and remove the empty state once the first post is live.
4. Add an `<item>` to `blog/feed.xml` — `pubDate` must be RFC-822, which
   `date -R` prints.
5. Add a `<url>` to `sitemap.xml`.

`_template.html` carries `robots: noindex, nofollow` and is disallowed in
`robots.txt`, so it can live in the repo without being indexed.

The 2010–2013 Blogger archive stays at `blog.dscamargo.com.br`. It is a
different registrable domain from `dans.ch`, so it never passed authority here;
it is linked once from the blog index as an archive and nowhere else.

- Bump `CACHE` in `sw.js` whenever the asset set changes.
- Favicons live in `assets/ico/` and are all derived from the brand path in
  `assets/images/dsc_white.svg`. `favicon.svg` is the rounded tab tile;
  `apple-touch-icon.png` and the `android-chrome-*` PNGs bleed to the edge
  because the OS masks them. A copy of `favicon.ico` sits at the repo root
  because bots probe `/favicon.ico` regardless of the `<link>` tags.
- `assets/icons.svg` is the canonical icon source, but each page embeds its
  own copy of the `<symbol>` block (`<svg class="sprite">`, right after the GTM
  noscript). It is embedded rather than fetched so icons survive `file://`
  and a JS-less load. Edit `assets/icons.svg` first, then copy the block into
  every page.
