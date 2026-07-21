"""
Project : Duplicate File Finder
Project ID : 010

Validation
"""

from pathlib import Path

from src.config import SCAN_METHODS
from src.models.scan_settings import ScanSettings


def validate_scan_settings(settings: ScanSettings) -> None:
    """
    Validates all scan settings.
    """

    validate_folder(settings.folder)
    validate_scan_method(settings.scan_method)


def validate_folder(folder: Path) -> None:
    """
    Validates the selected folder.
    """

    if folder is None:
        raise ValueError("Folder cannot be None.")

    if not folder.exists():
        raise FileNotFoundError(
            f"Folder does not exist: {folder}"
        )

    if not folder.is_dir():
        raise NotADirectoryError(
            f"Not a directory: {folder}"
        )


def validate_scan_method(scan_method: str) -> None:
    """
    Validates the selected scan method.
    """

    if scan_method not in SCAN_METHODS:
        raise ValueError(
            f"Unsupported scan method: {scan_method}"
        )


def validate_export_filename(filename: str) -> None:
    """
    Validates the export filename.
    """

    if not filename:
        raise ValueError(
            "Export filename cannot be empty."
        )

    invalid_characters = '<>:"/\\|?*'

    for character in invalid_characters:

        if character in filename:
            raise ValueError(
                f"Invalid character '{character}' found in filename."
            )


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - validate_scan_settings()
# - validate_folder()
# - validate_scan_method()
# - validate_export_filename()
#
# Public Signals:
# - None
#
# Dependencies:
# - pathlib
# - src.config
# - src.models.scan_settings