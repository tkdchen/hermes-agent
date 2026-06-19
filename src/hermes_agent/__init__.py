from pathlib import Path
from typing import Final


def get_project_root() -> Path:
    """Get the project installation directory.

    From an installation in whatever system-wide or a virtual environment,
    the installation directory is ../../python<version>/site-packages/hermes_agent
    """
    return Path(__file__).parent.resolve()


PROJECT_ROOT: Final = get_project_root()


def get_source_root() -> Path:
    # ../../src/hermes_agent/__init__.py  -> ../../
    return PROJECT_ROOT.parent.parent.parent


SOURCE_ROOT: Final = get_source_root()


def read_source_file(*file_path) -> str:
    # Pin encoding to UTF-8: source files in this repo are UTF-8, but
    # Path.read_text() defaults to the system locale — which is cp1252
    # on most Western Windows installs and crashes as soon as the file
    # contains any non-ASCII byte (e.g. an em-dash in a comment).
    try:
        return Path(PROJECT_ROOT, *file_path).read_text("utf-8")
    except:
        return Path(get_source_root(), *file_path).read_text("utf-8")
