"""
Project : Duplicate File Finder
Project ID : 010

Duplicate Detector
"""

from src.config import (
    SCAN_METHOD_ATTRIBUTE,
    SCAN_METHOD_CONTENT,
)
from src.core.attribute_matcher import find_attribute_duplicates
from src.core.content_matcher import find_content_duplicates
from src.models.duplicate_group_model import DuplicateGroup
from src.models.file_record import FileRecord


def detect_duplicates(
    file_records: list[FileRecord],
    scan_method: str,
) -> list[DuplicateGroup]:
    """
    Detects duplicate files using the selected
    scan method.

    Parameters
    ----------
    file_records
        List of discovered files.

    scan_method
        Selected duplicate detection method.

    Returns
    -------
    list[DuplicateGroup]
        Duplicate groups identified by the
        selected scan method.
    """

    if scan_method == SCAN_METHOD_ATTRIBUTE:
        return find_attribute_duplicates(file_records)

    if scan_method == SCAN_METHOD_CONTENT:
        return find_content_duplicates(file_records)

    raise ValueError(
        f"Unsupported scan method: {scan_method}"
    )


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - detect_duplicates()
#
# Public Signals:
# - None
#
# Dependencies:
# - src.config
# - src.core.attribute_matcher
# - src.core.content_matcher
# - src.models.duplicate_group_model
# - src.models.file_record