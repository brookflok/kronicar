"""MkDocs build hooks for the Kroničar wiki."""
import os
import shutil


def on_post_build(config, **kwargs):
    """Copy robots.txt into the built site root.

    The same-dir plugin does not expose root-level static files, so we copy
    robots.txt explicitly to keep the published site out of search engines.
    """
    root = os.path.dirname(config["config_file_path"])
    src = os.path.join(root, "robots.txt")
    if os.path.exists(src):
        shutil.copy(src, os.path.join(config["site_dir"], "robots.txt"))
