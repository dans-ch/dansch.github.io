import pathlib, html
posts = [
    ("ai-accelerator", "Engineering", "AI is an accelerator,<br>not a decision-maker", 58),
    ("beginner-again", "Career", "You have to be bad<br>at something again", 58),
    ("legacy-rollout", "Architecture", "Planning a legacy migration:<br>the rollout is the hard part", 49),
    ("end-to-end", "Architecture", "End to end:<br>why small companies<br>can’t afford handoffs", 54),
]
TPL = """<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500&display=swap');
*{{margin:0;box-sizing:border-box}}
body{{width:1200px;height:630px;background:#08090b;font-family:Inter,sans-serif;
 display:grid;grid-template-columns:1fr 1fr;overflow:hidden;position:relative}}
.art{{position:absolute;right:-40px;top:50%;transform:translateY(-50%);width:760px}}
.art img{{width:100%;display:block;opacity:.9}}
.art::after{{content:'';position:absolute;inset:0;
 background:linear-gradient(90deg,#08090b 6%,rgba(8,9,11,.86) 34%,rgba(8,9,11,0) 78%)}}
.pad{{position:relative;z-index:2;padding:74px 0 66px 78px;display:flex;flex-direction:column;
 justify-content:space-between;grid-column:1/3;width:760px}}
.label{{font-family:'JetBrains Mono',monospace;font-size:15px;letter-spacing:.16em;
 text-transform:uppercase;color:#22d3ee}}
.rule{{width:56px;height:2px;background:#22d3ee;margin:0 0 26px}}
h1{{font-size:{size}px;line-height:1.1;letter-spacing:-.022em;font-weight:600;color:#edeff2}}
.foot{{display:flex;gap:14px;align-items:center;font-size:19px;color:#697180}}
.foot b{{color:#9ba3ae;font-weight:500}}
</style>
<div class="art"><img src="{slug}.svg"></div>
<div class="pad">
  <div><div class="rule"></div><div class="label">{label}</div></div>
  <h1>{title}</h1>
  <div class="foot"><b>Daniel Scheidemantel Camargo</b><span>dans.ch/blog</span></div>
</div>"""
out = pathlib.Path("assets/images/blog")
for slug, label, title, size in posts:
    (out / f"_og-{slug}.html").write_text(TPL.format(slug=slug, label=label, title=title, size=size))
    print(slug)
