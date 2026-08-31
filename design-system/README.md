# DanSch Design System

Design tokens for the dans.ch web properties.

## Two systems, on purpose

| File | Used by | Theme |
| --- | --- | --- |
| `variables.css` | Main site — `index.html`, `curriculum.html`, `chave.html`, `greenhop.html`, `thanks.html`, `files/`, `cloud/` | Dark technical (2026) |
| `legacy.css` | Capellaris subsite — `capellaris/assets/style.css` | Light Bootstrap-era (pre-2026) |

`legacy.css` is the previous shared file, frozen. Capellaris still depends on
its base element styles, `.rounded-*` / `.shadow-*` / `.text-white` utilities
and the `pulse` / `glow-pulse` keyframes. **Never import both files into the
same document** — they define conflicting `body` and heading styles.

The numbered documents in this folder (`1-BRAND-FOUNDATION.md` … `7-ICONS-IMAGERY.md`)
describe the legacy system and remain accurate for Capellaris only.

---

## The 2026 dark system

Load the tokens before any other stylesheet:

```html
<link rel="stylesheet" href="design-system/variables.css">
<link rel="stylesheet" href="assets/style.css">
```

### Principles

1. **Hairlines, not glass.** Regions separate with `1px solid var(--line)` and
   whitespace. No stacked translucent panels, no blur except the sticky header.
2. **One accent.** `--accent` (cyan) appears on links, the active section node,
   the walker and small mono labels. Primary buttons are white on black; the
   accent is never the default button colour.
3. **Small radii.** `--r-2` (4px) is the default. Large radii were what made
   the previous design read as playful.
4. **Mono carries metadata.** Eyebrows, section indices, dates, tags and field
   labels are JetBrains Mono, uppercase, `--ls-label`. Prose is Inter.
5. **Motion is a signal, not decoration.** Reveals, the rail progress and the
   walker all respond to scroll position; everything collapses under
   `prefers-reduced-motion`.

### Surfaces

| Token | Value | Use |
| --- | --- | --- |
| `--bg` | `#08090b` | Page ground |
| `--bg-soft` | `#0c0e12` | Inset cells inside a grid |
| `--surface` | `#101318` | Cards, the booking panel |
| `--surface-2` | `#161a21` | Card hover, the walker shell |
| `--line` / `--line-2` / `--line-3` | white @ 8.5% / 15.5% / 26% | Hairlines, borders, markers |

### Text

`--text` `#edeff2` · `--text-2` `#9ba3ae` (body copy, leads) · `--text-3` `#697180`
(mono labels, metadata). Never put `--text-3` on `--surface-2` or lighter.

### Accent

`--accent` `#22d3ee` · `--accent-2` `#67e8f9` (hover) · `--accent-deep` `#0e7490`
(gradient tail) · `--accent-wash` / `--accent-line` for tinted fills and borders.

### Type scale

Every step is fluid — `--fs-display`, `--fs-h1` … `--fs-label`. Do not hard-code
`font-size` in page CSS; pick a step. Families: `--font-sans` (Inter),
`--font-mono` (JetBrains Mono).

### Spacing & layout

4px base: `--s-1` … `--s-32`. `--section-y` is the rhythm between top-level
sections. `--container` 1200px, `--container-narrow` 880px, `--gutter` fluid.

`--rail-w` is the left gutter reserved for the walker; it collapses to `0` below
1181px, where the rail, walker and section nodes are hidden entirely.

### Motion

`--ease` / `--ease-out`, `--t-fast` 140ms, `--t-base` 240ms, `--t-slow` 620ms.
