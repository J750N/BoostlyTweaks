"""
Shared helper for resolving bundled resource paths (data files, assets),
correctly handling both:
  - running from source (python app.py)
  - running as a packaged PyInstaller onefile .exe, where everything gets
    extracted to a temporary folder at sys._MEIPASS at runtime

Always build resource paths with this instead of raw __file__-relative
math - __file__ behaves differently for modules loaded from PyInstaller's
bundled archive vs from a real file, and it's easy to get subtly wrong.
"""

import sys
import os

# core/paths.py -> project root is one level up from this file's directory
_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def resource_path(*relative_parts) -> str:
    """Absolute path to a bundled resource, e.g. resource_path("assets", "icon.png")."""
    base_path = getattr(sys, "_MEIPASS", _PROJECT_ROOT)
    return os.path.join(base_path, *relative_parts)
