#!/usr/bin/env python3
"""Pomocna skripta za izvlacenje teksta iz PDF-a (PyMuPDF).

Koristi venv u istom folderu:
  _tools/.venv/bin/python _tools/extract.py --toc  "put/do/knjige.pdf"
  _tools/.venv/bin/python _tools/extract.py --range 10-35 \
      --title "Chapter 1: A Visitor's Guide" \
      --out  "method/01_batches/batch_01.md" \
      "put/do/knjige.pdf"

--toc      ispise broj strana i embedded sadrzaj (za odredjivanje opsega po poglavlju)
--range    book pages (1-indeksirano, inkluzivno), npr. 10-35 ili samo 12
--title    naslov koji ide u batch zaglavlje
--out      izlazni .md fajl (ako se izostavi, ispisuje na stdout)

Svaki batch dobija source tag u prvom redu, isto kao kod Sharn obrade.
"""
import argparse
import sys

try:
    import fitz  # PyMuPDF
except ImportError:
    sys.exit("PyMuPDF nije instaliran. Pokreni: _tools/.venv/bin/pip install pymupdf")


def cmd_toc(doc):
    print(f"pages: {doc.page_count}")
    toc = doc.get_toc()
    print(f"toc entries: {len(toc)}")
    for lvl, title, page in toc:
        print(f"{'  ' * (lvl - 1)}{page:>4}  {title}")


def cmd_range(doc, rng, title, out):
    if "-" in rng:
        a, b = rng.split("-", 1)
        p0, p1 = int(a), int(b)
    else:
        p0 = p1 = int(rng)
    parts = [f"<!-- SOURCE: {title} | book pages {p0}-{p1} -->",
             f"# {title}\n"]
    for bp in range(p0, p1 + 1):
        parts.append(f"\n\n===== [book page {bp}] =====\n")
        parts.append(doc[bp - 1].get_text())
    text = "".join(parts)
    if out:
        with open(out, "w") as f:
            f.write(text)
        print(f"napisano: {out} ({len(text)} znakova, strane {p0}-{p1})")
    else:
        sys.stdout.write(text)


def main():
    ap = argparse.ArgumentParser(description="Izvlacenje teksta iz PDF-a u .md batch")
    ap.add_argument("pdf", help="putanja do PDF knjige")
    ap.add_argument("--toc", action="store_true", help="ispisi sadrzaj i broj strana")
    ap.add_argument("--range", dest="rng", help="opseg book pages, npr. 10-35")
    ap.add_argument("--title", default="Untitled", help="naslov za batch zaglavlje")
    ap.add_argument("--out", help="izlazni .md fajl")
    args = ap.parse_args()

    doc = fitz.open(args.pdf)
    if args.toc:
        cmd_toc(doc)
    elif args.rng:
        cmd_range(doc, args.rng, args.title, args.out)
    else:
        ap.error("zadaj --toc ili --range")


if __name__ == "__main__":
    main()
