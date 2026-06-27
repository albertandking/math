"""Build the MkDocs source directory from project content.

:return: Exit code 0 when the site docs are generated successfully.
"""

from __future__ import annotations

from pathlib import Path
import shutil


ROOT: Path = Path(__file__).resolve().parent.parent
SITE_DOCS: Path = ROOT / "site_docs"


def reset_directory(path: Path) -> None:
    """Remove and recreate a directory.

    :param path: Target directory path.
    """
    # Rebuild from scratch so removed files do not linger in the generated docs tree.
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_file(source: Path, target: Path) -> None:
    """Copy a single file while creating parent directories.

    :param source: Source file path.
    :param target: Target file path.
    """
    # Ensure the generated docs tree mirrors the source structure.
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def copy_directory(source: Path, target: Path) -> None:
    """Copy a whole directory into the generated docs tree.

    :param source: Source directory path.
    :param target: Target directory path.
    """
    # Only copy optional folders when they exist in the project root.
    if source.exists():
        shutil.copytree(source, target, dirs_exist_ok=True)


def main() -> int:
    """Generate the MkDocs source tree.

    :return: Process exit code.
    """
    # Start with a clean output directory for MkDocs source files.
    reset_directory(SITE_DOCS)

    # Map the project authoring structure into the docs tree used by MkDocs.
    copy_file(ROOT / "README.md", SITE_DOCS / "index.md")
    copy_directory(ROOT / "chapters", SITE_DOCS / "chapters")
    copy_directory(ROOT / "docs", SITE_DOCS / "docs")
    copy_directory(ROOT / "assets", SITE_DOCS / "assets")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
