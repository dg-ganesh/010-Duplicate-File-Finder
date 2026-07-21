"""
Project : Duplicate File Finder
Project ID : 010

File Service
"""

from pathlib import Path

from src.models.file_record import FileRecord
from src.models.scan_settings import ScanSettings
from src.services.logging_service import get_logger

logger = get_logger()


def enumerate_files(settings: ScanSettings) -> list[FileRecord]:
    """
    Scans the selected folder and returns a list
    of FileRecord objects.
    """

    folder = settings.folder

    if not folder.exists():
        raise FileNotFoundError(f"Folder does not exist: {folder}")

    if not folder.is_dir():
        raise NotADirectoryError(f"Not a directory: {folder}")

    logger.info("Scanning folder: %s", folder)

    file_records: list[FileRecord] = []

    if settings.recursive:
        iterator = folder.rglob("*")
    else:
        iterator = folder.glob("*")

    for item in iterator:

        if not item.is_file():
            continue

        if item.is_symlink() and not settings.follow_symbolic_links:
            continue

        try:

            stats = item.stat()

            file_record = FileRecord(
                path=item,
                name=item.name,
                extension=item.suffix.lower(),
                size=stats.st_size,
                modified_time=stats.st_mtime,
            )

            file_records.append(file_record)

        except (PermissionError, OSError) as ex:

            logger.warning(
                "Unable to access file: %s (%s)",
                item,
                ex,
            )

    logger.info(
        "Files discovered: %d",
        len(file_records),
    )

    return file_records


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - enumerate_files()
#
# Public Signals:
# - None
#
# Dependencies:
# - pathlib
# - src.models.file_record
# - src.models.scan_settings
# - src.services.logging_service