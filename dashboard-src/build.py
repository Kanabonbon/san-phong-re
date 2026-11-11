"""Build the bilingual dashboard (VI + EN) from the two single-language sources.

    python3 dashboard-src/build.py

Edit vi.html and en.html (same structure, different text), then run this script.
It writes plugins/san-phong-re/skills/mo-dashboard/dashboard/index.html: one page
with a VI | EN switch in the header. Only one language is mounted at a time; the
form and the last results carry over when the user switches.
"""
import pathlib
import re
import sys

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "plugins/san-phong-re/skills/mo-dashboard/dashboard/index.html"
LANGS = ["vi", "en"]
STORE = "san-phong-re:v1"

SWITCH = ('<div class="lang" role="group" aria-label="Ngôn ngữ / Language">'
          '<button type="button" data-lang="vi" title="Tiếng Việt">VI</button>'
          '<button type="button" data-lang="en" title="English">EN</button></div>')

EXTRA_CSS = """
/* language switch */
.tools{display:flex;flex-wrap:wrap;align-items:center;gap:10px}
.lang{display:inline-flex;padding:3px;border-radius:999px;background:rgba(255,255,255,.08);border:1px solid rgba(255,255,255,.16)}
.lang button{border:0;background:none;color:var(--on-hero-muted);font:inherit;font-size:.74rem;font-weight:800;letter-spacing:.06em;padding:5px 11px;border-radius:999px;cursor:pointer}
.lang button:hover{color:var(--on-hero)}
.lang button[aria-pressed="true"]{background:var(--gold);color:#2b1c00}
.lang button:focus-visible{outline:2px solid var(--gold);outline-offset:2px}
html[lang="en"] details.filters>summary::after{content:"Collapse ▴"}
html[lang="en"] details.filters:not([open])>summary::after{content:"Show filters ▾"}
"""

BOOT = """
(() => {
  const KEY = "san-phong-re:lang", TITLES = { vi: "Săn Phòng Rẻ", en: "Stay Hunter" };
  const root = document.getElementById("spr-root");
  let cur = null, owned = [];
  // document-level listeners of the mounted language, removed on switch
  window.__sprListen = (t, type, fn, opt) => { owned.push([t, type, fn, opt]); t.addEventListener(type, fn, opt); };
  function mount(lang, state) {
    owned.forEach(([t, type, fn, opt]) => t.removeEventListener(type, fn, opt)); owned = [];
    root.replaceChildren(document.getElementById("spr-" + lang).content.cloneNode(true));
    document.documentElement.lang = lang; document.title = TITLES[lang];
    window.__sprState = state || null; window.__spr = null;
    window.__SPR_APPS[lang]();
    cur = lang;
    root.querySelectorAll(".lang [data-lang]").forEach(b => b.setAttribute("aria-pressed", String(b.dataset.lang === lang)));
  }
  document.addEventListener("click", ev => {
    const b = ev.target.closest(".lang [data-lang]");
    if (!b || b.dataset.lang === cur) return;
    if (window.__spr?.busy?.()) {
      const t = document.getElementById("envText");
      if (t) t.textContent = cur === "vi" ? "Đang tìm — đổi ngôn ngữ sau khi tìm xong" : "Search running — switch language when it finishes";
      return;
    }
    const state = window.__spr?.snapshot?.();
    try { localStorage.setItem(KEY, b.dataset.lang); } catch {}
    mount(b.dataset.lang, state);
    root.querySelector('.lang [data-lang="' + cur + '"]')?.focus();
  });
  let lang = null;
  try { lang = localStorage.getItem(KEY); } catch {}
  mount(window.__SPR_APPS[lang] ? lang : "vi");
})();
"""


def one(text, count, old, new, label):
    n = text.count(old)
    if n != count:
        sys.exit(f"{label}: expected {count} match(es), found {n}: {old[:70]!r}")
    return text.replace(old, new)


def split(lang):
    src = (HERE / f"{lang}.html").read_text(encoding="utf-8")
    m = re.match(r"\s*<title>.*?</title>(.*?)<style>(.*?)</style>(.*?)<script>(.*)</script>\s*$", src, re.S)
    if not m:
        sys.exit(f"{lang}.html: expected <title>, <style>, markup, <script>")
    head, css, markup, code = m.groups()

    env = re.search(r'<span class="env" id="env">.*?</span></span>', markup)
    if not env:
        sys.exit(f"{lang}.html: env badge not found")
    markup = markup.replace(env.group(0), f'<div class="tools">{env.group(0)}{SWITCH}</div>')

    code = code.strip()
    if not (code.startswith("(() => {") and code.endswith("})();")):
        sys.exit(f"{lang}.html: script must be one (() => {{ ... }})(); block")
    code = code[len("(() => {"):-len("})();")]
    code = re.sub(r'const STORE = "[^"]+";', f'const STORE = "{STORE}";', code)
    code = one(code, 1, 'document.addEventListener("keydown", ', '__sprListen(document, "keydown", ', lang)
    code = one(code, 1, "  const saved = store.get();",
               "  const saved = window.__sprState || store.get(); window.__sprState = null;\n"
               "  window.__spr = { busy: () => running, snapshot: () => ({ draft: readForm().q, last: current && !current.example ? current : null }) };",
               lang)
    if "window.addEventListener" in code or "document.addEventListener" in code:
        sys.exit(f"{lang}.html: route new global listeners through __sprListen")
    return head.strip(), css, markup, code


def main():
    parts = {l: split(l) for l in LANGS}
    head, css = parts["vi"][0], parts["vi"][1]
    out = ["<title>Săn Phòng Rẻ</title>", head, "<style>" + css + EXTRA_CSS + "</style>", "", '<div id="spr-root"></div>']
    for l in LANGS:
        out.append(f'<template id="spr-{l}">{parts[l][2]}</template>')
    out.append("<script>\nwindow.__SPR_APPS = window.__SPR_APPS || {};")
    for l in LANGS:
        out.append(f"window.__SPR_APPS.{l} = () => {{{parts[l][3]}}};")
    out.append(BOOT + "</script>\n")
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {OUT.relative_to(HERE.parent)} ({OUT.stat().st_size:,} bytes)")


main()
