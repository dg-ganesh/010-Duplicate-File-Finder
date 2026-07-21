"""
Project : Duplicate File Finder
Project ID : 010

Content Matcher
"""

from collections import defaultdict

from src.models.duplicate_group_model import DuplicateGroup
from src.models.file_record import FileRecord
from src.services.hash_service import update_file_hash


def find_content_duplicates(
    file_records: list[FileRecord],
) -> list[DuplicateGroup]:
    """
    Finds duplicate files by comparing
    SHA-256 hashes.

    Files are first grouped by file size.
    Only files sharing the same size are hashed.
    """

    size_groups: dict[int, list[FileRecord]] = defaultdict(list)

    for file_record in file_records:
        size_groups[file_record.size].append(file_record)

    duplicate_groups: list[DuplicateGroup] = []

    group_id = 1

    for size_group in size_groups.values():

        if len(size_group) < 2:
            continue

        hash_groups: dict[str, list[FileRecord]] = defaultdict(list)

        for file_record in size_group:

            if file_record.content_hash is None:
                update_file_hash(file_record)

            hash_groups[file_record.content_hash].append(file_record)

        for hash_group in hash_groups.values():

            if len(hash_group) < 2:
                continue

            duplicate_group = DuplicateGroup(
                group_id=group_id,
                files=hash_group,
            )

            for file_record in hash_group:
                file_record.is_duplicate = True
                file_record.duplicate_group_id = group_id

            duplicate_groups.append(duplicate_group)

            group_id += 1

    return duplicate_groups


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - find_content_duplicates()
#
# Public Signals:
# - None
#
# Dependencies:
# - collections
# - src.models.file_record
# - src.models.duplicate_group_model
# - src.services.hash_service