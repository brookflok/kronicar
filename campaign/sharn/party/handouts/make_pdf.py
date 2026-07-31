#!/usr/bin/env python3
"""Generiše player handout PDF iz kragz_handout.md (PyMuPDF Story API).
Pokretanje: _tools/.venv/bin/python campaign/sharn/party/handouts/make_pdf.py
"""
import os
import re
import html
import fitz  # PyMuPDF

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "kragz_handout.md")
OUT = os.path.join(HERE, "kragz.pdf")

FONTS = {
    "g-reg.ttf": "/System/Library/Fonts/Supplemental/Georgia.ttf",
    "g-bold.ttf": "/System/Library/Fonts/Supplemental/Georgia Bold.ttf",
    "g-italic.ttf": "/System/Library/Fonts/Supplemental/Georgia Italic.ttf",
    "g-bolditalic.ttf": "/System/Library/Fonts/Supplemental/Georgia Bold Italic.ttf",
}


def inline(text):
    text = html.escape(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"\*(.+?)\*", r"<i>\1</i>", text)
    return text


def md_to_html(md):
    out = []
    in_list = False
    for raw in md.splitlines():
        line = raw.rstrip()
        if not line.strip():
            if in_list:
                out.append("</ul>")
                in_list = False
            continue
        if line.startswith("- "):
            if not in_list:
                out.append("<ul>")
                in_list = True
            out.append("<li>%s</li>" % inline(line[2:]))
            continue
        if in_list:
            out.append("</ul>")
            in_list = False
        if line.startswith("## "):
            out.append("<h2>%s</h2>" % inline(line[3:]))
        elif line.startswith("# "):
            out.append("<h1>%s</h1>" % inline(line[2:]))
        else:
            out.append("<p>%s</p>" % inline(line))
    if in_list:
        out.append("</ul>")
    return "\n".join(out)


CSS = """
@font-face { font-family: body; src: url(g-reg.ttf); }
@font-face { font-family: body; src: url(g-bold.ttf); font-weight: bold; }
@font-face { font-family: body; src: url(g-italic.ttf); font-style: italic; }
@font-face { font-family: body; src: url(g-bolditalic.ttf); font-weight: bold; font-style: italic; }
* { font-family: body; }
body { font-size: 10px; line-height: 1.4; color: #1c1a17; }
h1 { font-size: 27px; color: #5a2d0c; margin: 0 0 2px 0; }
h2 { font-size: 13.5px; color: #7a3b12; margin: 11px 0 3px 0; }
p { margin: 0 0 6px 0; text-align: left; }
ul { margin: 2px 0 6px 0; }
li { margin: 0 0 3px 0; }
"""


def main():
    with open(SRC, encoding="utf-8") as f:
        md = f.read()
    body = md_to_html(md)
    full = "<html><body>%s</body></html>" % body

    arch = fitz.Archive()
    for name, path in FONTS.items():
        with open(path, "rb") as ff:
            arch.add(ff.read(), name)

    story = fitz.Story(html=full, user_css=CSS, archive=arch)
    writer = fitz.DocumentWriter(OUT)
    mediabox = fitz.paper_rect("a4")
    where = mediabox + (60, 55, -60, -55)
    more = 1
    pages = 0
    while more:
        dev = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
        pages += 1
    writer.close()
    print("OK ->", OUT, "| stranica:", pages)


if __name__ == "__main__":
    main()
