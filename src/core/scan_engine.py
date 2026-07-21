"""
Project : Duplicate File Finder
Project ID : 010

Scan Engine

Revision History
----------------
1.0.0
- Initial implementation.

1.0.1
- Restored stable architecture.
- Removed ScanResult dependency.
"""

from src.core.duplicate_detector import detect_duplicates
from src.core.validation import validate_scan_settings
from src.models.duplicate_group_model import DuplicateGroup
from src.models.scan_settings import ScanSettings
from src.services.file_service import enumerate_files
from src.services.logging_service import get_logger

logger = get_logger()


def scan_folder(
    settings: ScanSettings,
) -> list[DuplicateGroup]:
    """
    Executes the complete duplicate scan workflow.

    Parameters
    ----------
    settings
        User selected scan settings.

    Returns
    -------
    list[DuplicateGroup]
        Duplicate groups found during the scan.
    """

    logger.info("=" * 60)
    logger.info("Starting duplicate scan.")

    validate_scan_settings(settings)

    logger.info("Validation completed.")

    file_records = enumerate_files(settings)

    logger.info(
        "Discovered %d file(s).",
        len(file_records),
    )

    duplicate_groups = detect_duplicates(
        file_records=file_records,
        scan_method=settings.scan_method,
    )

    logger.info(
        "Duplicate groups found: %d",
        len(duplicate_groups),
    )

    logger.info("Duplicate scan completed.")

    return duplicate_groups


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - scan_folder()
#
# Public Signals:
# - None
#
# Dependencies:
# - src.core.validation
# - src.core.duplicate_detector
# - src.models.scan_settings
# - src.models.duplicate_group_model
# - src.services.file_service
# - src.services.logging_service