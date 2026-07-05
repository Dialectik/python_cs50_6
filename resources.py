import sys
from pathlib import Path


def resource_path(relative_path):
    """Return an absolute filesystem path to an application resource.

    Args:
        relative_path: Resource path relative to the project or PyInstaller bundle root.

    Returns:
        Absolute filesystem path to the requested resource.
    """
    base_path = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent))
    return str(base_path / relative_path)
