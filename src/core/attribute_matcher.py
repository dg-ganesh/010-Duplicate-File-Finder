"""
Project : Duplicate File Finder
Project ID : 010

Attribute Matcher
"""

from collections import defaultdict

from src.models.duplicate_group_model import DuplicateGroup
from src.models.file_record import FileRecord


def find_attribute_duplicates(
    file_records: list[FileRecord],
) -> list[DuplicateGroup]:
    """
    Groups files by their attributes.

    Version 1.0 groups files using file size.
    Only groups containing more than one file
    are returned.
    """

    size_groups: dict[int, list[FileRecord]] = defaultdict(list)

    for file_record in file_records:
        size_groups[file_record.size].append(file_record)

    duplicate_groups: list[DuplicateGroup] = []

    group_id = 1

    for files in size_groups.values():

        if len(files) < 2:
            continue

        duplicate_group = DuplicateGroup(
            group_id=group_id,
            files=files,
        )

        for file in files:
            file.is_duplicate = True
            file.duplicate_group_id = group_id

        duplicate_groups.append(duplicate_group)

        group_id += 1

    return duplicate_groups


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - find_attribute_duplicates()
#
# Public Signals:
# - None
#
# Dependencies:
# - collections
# - src.models.file_record
# - src.models.duplicate_group_model