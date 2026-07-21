"""
Project : Duplicate File Finder
Project ID : 010

Hash Service
"""

import hashlib

from src.config import HASH_ALGORITHM, HASH_BLOCK_SIZE
from src.models.file_record import FileRecord
from src.services.logging_service import get_logger

logger = get_logger()


def calculate_file_hash(file_record: FileRecord) -> str:
    """
    Calculates and returns the hash value
    for the specified file.
    """

    hash_object = hashlib.new(HASH_ALGORITHM)

    try:

        with file_record.path.open("rb") as file:

            while True:

                data = file.read(HASH_BLOCK_SIZE)

                if not data:
                    break

                hash_object.update(data)

    except (PermissionError, OSError) as ex:

        logger.error(
            "Failed to hash file: %s (%s)",
            file_record.path,
            ex,
        )

        raise

    return hash_object.hexdigest()


def update_file_hash(file_record: FileRecord) -> None:
    """
    Calculates the file hash and updates
    the FileRecord instance.
    """

    file_record.content_hash = calculate_file_hash(file_record)


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - calculate_file_hash()
# - update_file_hash()
#
# Public Signals:
# - None
#
# Dependencies:
# - hashlib
# - src.config
# - src.models.file_record
# - src.services.logging_service