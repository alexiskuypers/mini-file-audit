from pathlib import Path
import logging


logger = logging.getLogger(__name__)


def is_hidden_path(path: Path, root: Path) -> bool:
    relative_path = path.relative_to(root)

    return any(
        part.startswith(".")
        for part in relative_path.parts
    )


def scan_folder(
    folder: Path,
    recursive: bool = False,
    extensions: list[str] | None = None,
    include_hidden: bool = False,
    max_size: int | None = None
) -> list[Path] :
    files = []
    logger.info("scan start for folder: %s", folder)

    if recursive:
        items = folder.rglob("*")
    else:
        items = folder.iterdir()
    for path in items:
        if not path.is_file():
            continue
        if not include_hidden and is_hidden_path(path, folder):
            continue
        if extensions is not None and path.suffix not in extensions:
            continue
        try:
            if max_size is not None and path.stat().st_size > max_size:
                continue
        except OSError:
            logger.warning("file can't be inspected, skip: %s", path)
            continue
        files.append(path)
    selected_files = sorted(files)

    if not selected_files:
        logger.warning("No files selected from folder: %s", folder)

    logger.info("scanner folder: %s, validates, files selected: %s",
                folder,
                len(files)
            )
    return selected_files
