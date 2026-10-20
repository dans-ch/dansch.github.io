# Generates the original blog artworks. Pure geometry, no external assets,
# no fonts. Palette follows design-system/variables.css.
import math, pathlib

OUT = pathlib.Path("assets/images/blog")
BG, ACC, ACC2 = "#0b0d11", "#22d3ee", "#67e8f9"
W, H = 1200, 750

def head(title, desc, extra=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
            f'role="img" aria-labelledby="t d" fill="none">'
            f'<title id="t">{title}</title><desc id="d">{desc}</desc>'
            f'<rect width="{W}" height="{H}" fill="{BG}"/>{extra}')

def n(v):  # short numbers
    s = f"{v:.1f}".rstrip("0").rstrip(".")
    return s if s != "-0" else "0"

# ---------------------------------------------------------------- 1. accelerator
p = []
p.append('<g stroke="#ffffff" stroke-opacity=".05" stroke-width="1">'
         + "".join(f'<path d="M110 {y}h980"/>' for y in (170, 300, 450, 580)) + '</g>')
# the spray of cheap options
rays, chosen_y = [], 428
for i in range(17):
    ye = 128 + i * (622 - 128) / 16
    if abs(ye - chosen_y) < 12:
        continue
    c1x, c2x = 400, 610
    rays.append(f'<path d="M148 375C{c1x} 375 {c2x} {n(375+(ye-375)*.72)} 830 {n(ye)}"/>')
p.append(f'<g stroke="{ACC2}" stroke-opacity=".26" stroke-width="1.8" stroke-linecap="round">'
         + "".join(rays) + '</g>')
p.append('<g fill="#ffffff" fill-opacity=".16">'
         + "".join(f'<circle cx="830" cy="{n(128 + i*(622-128)/16)}" r="2.6"/>'
                   for i in range(17) if abs(128 + i*(622-128)/16 - chosen_y) >= 12) + '</g>')
# the gate: where a human decides
p.append('<path d="M830 104v542" stroke="#ffffff" stroke-opacity=".18" stroke-width="1.5" stroke-dasharray="7 9"/>')
p.append(f'<rect x="820" y="{chosen_y-34}" width="20" height="68" rx="10" fill="{BG}" '
         f'stroke="{ACC}" stroke-opacity=".85" stroke-width="2"/>')
# the one option that ships
p.append(f'<path d="M148 375C400 375 610 {n(375+(chosen_y-375)*.72)} 830 {n(chosen_y)}" '
         f'stroke="{ACC}" stroke-width="3" stroke-linecap="round"/>')
p.append(f'<path d="M840 {chosen_y}C930 {chosen_y} 960 375 1046 375" stroke="{ACC}" stroke-width="3" '
         f'stroke-linecap="round"/>')
p.append(f'<circle cx="148" cy="375" r="9" fill="{BG}" stroke="{ACC}" stroke-width="3"/>')
p.append(f'<circle cx="1058" cy="375" r="13" fill="{ACC}"/>'
         f'<circle cx="1058" cy="375" r="26" stroke="{ACC}" stroke-opacity=".3" stroke-width="1.5"/>')
svg1 = head("Many generated options narrowing to one decision",
            "Seventeen thin paths fan out from a single node and stop at a dashed vertical gate; "
            "one path passes through the gate and continues to a solid endpoint.") \
       + "".join(p) + "</svg>"

# ---------------------------------------------------------------- 2. beginner again
p = []
p.append('<g stroke="#ffffff" stroke-opacity=".05" stroke-width="1">'
         + "".join(f'<path d="M110 {y}h980"/>' for y in (200, 330, 460, 590)) + '</g>')
p.append('<path d="M110 660h980" stroke="#ffffff" stroke-opacity=".13" stroke-width="1.5"/>')
# the comfortable plateau, and the flat future it implies
p.append('<path d="M130 520C250 430 330 352 470 330" stroke="#ffffff" stroke-opacity=".34" '
         'stroke-width="2.5" stroke-linecap="round"/>')
p.append('<path d="M470 330C700 316 880 310 1070 306" stroke="#ffffff" stroke-opacity=".16" '
         'stroke-width="2" stroke-dasharray="6 10" stroke-linecap="round"/>')
# the drop, and the steeper climb out of it
p.append(f'<path d="M470 330C560 342 590 470 636 566" stroke="{ACC}" stroke-width="3.4" '
         f'stroke-linecap="round"/>')
p.append(f'<path d="M636 566C700 660 790 452 1070 168" stroke="{ACC}" stroke-width="3.4" '
         f'stroke-linecap="round"/>')
p.append('<path d="M636 588v72" stroke="#ffffff" stroke-opacity=".2" stroke-width="1.5" stroke-dasharray="4 7"/>')
p.append(f'<circle cx="470" cy="330" r="7" fill="#ffffff" fill-opacity=".34"/>')
p.append(f'<circle cx="636" cy="576" r="11" fill="{BG}" stroke="{ACC}" stroke-width="3.4"/>')
p.append(f'<circle cx="1070" cy="168" r="9" fill="{ACC}"/>')
svg2 = head("A competence plateau, a deliberate drop, and a steeper climb",
            "A rising line flattens into a plateau; a dashed line continues that plateau, while a bright "
            "line drops sharply and then climbs past it.") + "".join(p) + "</svg>"

# ---------------------------------------------------------------- 3. rollout
p = []
share = [1, 3, 8, 20, 45, 72, 92, 100]
x0, bw, gap, top, bot = 132, 96, 24, 190, 566
p.append(f'<g stroke="#ffffff" stroke-opacity=".05" stroke-width="1">'
         f'<path d="M110 {top}h980"/><path d="M110 {(top+bot)//2}h980"/></g>')
old, new, caps = [], [], []
for i, s in enumerate(share):
    x = x0 + i * (bw + gap)
    split = bot - (bot - top) * s / 100
    if s < 100:
        old.append(f'<rect x="{x}" y="{n(top)}" width="{bw}" height="{n(split-top)}" rx="4"/>')
    if s > 0:
        new.append(f'<rect x="{x}" y="{n(split)}" width="{bw}" height="{n(bot-split)}" rx="4"/>')
    caps.append(f'<path d="M{x} {n(split)}h{bw}"/>')
p.append(f'<g fill="#ffffff" fill-opacity=".07">' + "".join(old) + '</g>')
p.append(f'<g fill="{ACC}" fill-opacity=".85">' + "".join(new) + '</g>')
p.append(f'<g stroke="{ACC2}" stroke-opacity=".55" stroke-width="2" stroke-linecap="round">'
         + "".join(caps) + '</g>')
p.append(f'<path d="M110 {bot}h980" stroke="#ffffff" stroke-opacity=".16" stroke-width="1.5"/>')
p.append(f'<g stroke="#ffffff" stroke-opacity=".2" stroke-width="1.5">'
         + "".join(f'<path d="M{x0 + i*(bw+gap) + bw/2:.0f} {bot+8}v14"/>' for i in range(8)) + '</g>')
# the rollback path nobody plans for
p.append(f'<path d="M732 168C700 126 620 126 588 166" stroke="{ACC2}" stroke-opacity=".5" '
         f'stroke-width="2.2" stroke-dasharray="7 8" stroke-linecap="round"/>')
p.append(f'<path d="M588 168l1-21 19 9z" fill="{ACC2}" fill-opacity=".5"/>')
svg3 = head("Traffic moving from an old system to a new one in stages",
            "Eight columns across the frame; in each, the bright lower share of traffic on the new system "
            "grows from a sliver to the whole column, with a dashed rollback arrow above.") \
       + "".join(p) + "</svg>"

# ---------------------------------------------------------------- 4. end to end
p = []
xs = [180, 390, 600, 810, 1020]
ya, yb = 250, 520
p.append('<g stroke="#ffffff" stroke-opacity=".05" stroke-width="1">'
         + "".join(f'<path d="M110 {y}h980"/>' for y in (ya, yb)) + '</g>')
# the relay: five owners, a gap at every handoff
p.append('<g stroke="#ffffff" stroke-opacity=".2" stroke-width="2" stroke-linecap="round">'
         + "".join(f'<path d="M{a+26} {ya}H{b-70}"/>' for a, b in zip(xs, xs[1:])) + '</g>')
p.append('<g fill="#ffffff" fill-opacity=".14">'
         + "".join(f'<circle cx="{x}" cy="{ya}" r="10"/>' for x in xs) + '</g>')
# one owner: a single continuous line, and the return path from operation back to the need
p.append(f'<path d="M{xs[0]} {yb}H{xs[-1]}" stroke="{ACC}" stroke-width="3.2" stroke-linecap="round"/>')
p.append(f'<path d="M{xs[-1]} {yb+28}C{xs[-1]} 668 {xs[0]} 668 {xs[0]} {yb+14}" stroke="{ACC2}" '
         f'stroke-opacity=".55" stroke-width="2.2" stroke-dasharray="7 8" stroke-linecap="round"/>')
p.append(f'<path d="M{xs[0]} {yb+16}l-10 19h20z" fill="{ACC2}" fill-opacity=".55"/>')
p.append('<g>' + "".join(f'<circle cx="{x}" cy="{yb}" r="11" fill="{BG}" stroke="{ACC}" stroke-width="3"/>'
                          for x in xs[:-1]) + '</g>')
p.append(f'<circle cx="{xs[-1]}" cy="{yb}" r="13" fill="{ACC}"/>'
         f'<circle cx="{xs[-1]}" cy="{yb}" r="26" stroke="{ACC}" stroke-opacity=".3" stroke-width="1.5"/>')
svg4 = head("Five stages handed off between owners, versus one owner carrying them all",
            "Above, five faint nodes joined by short lines that stop before each next node; below, the same "
            "five nodes on one continuous bright line, with a dashed arc returning from the last node to the first.") \
       + "".join(p) + "</svg>"

for name, svg in (("ai-accelerator.svg", svg1),
                  ("beginner-again.svg", svg2),
                  ("legacy-rollout.svg", svg3),
                  ("end-to-end.svg", svg4)):
    (OUT / name).write_text(svg)
    print(name, len(svg), "bytes")
