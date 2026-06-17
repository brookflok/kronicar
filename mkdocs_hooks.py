"""MkDocs build hooks for the Kroničar wiki.

Two jobs:
  1. Resolve Obsidian-style [[wikilinks]] and ![[embeds]] against the file tree.
  2. Copy robots.txt into the built site (same-dir hides root static files).

Wikilink resolution slugifies BOTH the link target and every candidate
filename, then matches. That way all three authoring styles resolve to the
same file regardless of how it is named on disk:

    [[Dura]]                        -> Dura.md
    [[central-plateau|Plateau]]     -> Central Plateau.md
    [[boromar-vs-daask|Boromar]]    -> boromar-vs-daask.md

Targets that match no file are left as plain text (the alias, if given) so a
typo never produces a dead link, and the count is logged at the end.
"""
import logging
import os
import posixpath
import re
import shutil

log = logging.getLogger("mkdocs.hooks.kronicar")

# slug -> documentation File ; basename.lower() -> media File
_doc_index = {}
_media_index = {}
_unresolved = []

# ![[image.png]] or ![[image.png|alt]]
_EMBED_RE = re.compile(r"!\[\[\s*([^\]|#]+?)\s*(?:\|\s*([^\]]*?)\s*)?\]\]")
# [[target]] [[target|alias]] [[target#anchor]] [[target#anchor|alias]] [[#anchor]]
_LINK_RE = re.compile(
    r"(?<!!)\[\[\s*([^\]#|]*?)\s*(?:#\s*([^\]|]+?)\s*)?(?:\|\s*([^\]]*?)\s*)?\]\]"
)


def _slug(text):
    text = text.strip().lower()
    text = re.sub(r"[^\w\s-]", "", text)   # drop apostrophes, punctuation
    text = re.sub(r"[\s_]+", "-", text)    # spaces / underscores -> hyphen
    text = re.sub(r"-+", "-", text).strip("-")
    return text


def on_files(files, config, **kwargs):
    _doc_index.clear()
    _media_index.clear()
    del _unresolved[:]
    for f in files:
        if f.is_documentation_page():
            base = os.path.splitext(os.path.basename(f.src_uri))[0]
            slug = _slug(base)
            if slug and slug not in _doc_index:
                _doc_index[slug] = f
        elif f.is_media_file():
            _media_index.setdefault(os.path.basename(f.src_uri).lower(), f)
    return files


def _rel(target_url, page_url):
    rel = posixpath.relpath(target_url.rstrip("/"), page_url.rstrip("/") or ".")
    if target_url.endswith("/") and not rel.endswith("/"):
        rel += "/"
    return rel


def on_page_markdown(markdown, page, config, files, **kwargs):
    page_url = page.file.url

    def repl_embed(m):
        name, alt = m.group(1), m.group(2)
        media = _media_index.get(os.path.basename(name).lower())
        if not media:
            _unresolved.append(name)
            return alt or name
        return "![{}]({})".format(alt or "", _rel(media.url, page_url))

    def repl_link(m):
        target, anchor, alias = m.group(1), m.group(2), m.group(3)
        frag = "#" + _slug(anchor) if anchor else ""

        if not target:  # same-page anchor: [[#Section]]
            return "[{}]({})".format(alias or anchor or "", frag or "#")

        doc = _doc_index.get(_slug(os.path.basename(target)))
        display = alias or target
        if not doc:
            _unresolved.append(target)
            return display
        return "[{}]({}{})".format(display, _rel(doc.url, page_url), frag)

    markdown = _EMBED_RE.sub(repl_embed, markdown)
    markdown = _LINK_RE.sub(repl_link, markdown)
    return markdown


def on_post_build(config, **kwargs):
    if _unresolved:
        uniq = sorted(set(_unresolved))
        log.info(
            "Kroničar: %d wikilink target(s) had no matching file (%d total). "
            "Examples: %s",
            len(uniq), len(_unresolved), ", ".join(uniq[:15]),
        )
    root = os.path.dirname(config["config_file_path"])
    src = os.path.join(root, "robots.txt")
    if os.path.exists(src):
        shutil.copy(src, os.path.join(config["site_dir"], "robots.txt"))
