"""
Project : Duplicate File Finder
Project ID : 010

Duplicate Group Model
"""

from dataclasses import dataclass, field

from src.models.file_record import FileRecord


@dataclass
class DuplicateGroup:
    """
    Represents a single duplicate group.
    """

    group_id: int

    files: list[FileRecord] = field(default_factory=list)

    @property
    def file_count(self) -> int:
        """
        Returns the total number of files in the group.
        """
        return len(self.files)

    @property
    def duplicate_count(self) -> int:
        """
        Returns the number of duplicate files,
        excluding the first (original) file.
        """
        return max(0, len(self.files) - 1)

    @property
    def total_size(self) -> int:
        """
        Returns the combined size of all files
        in this duplicate group.
        """
        return sum(file.size for file in self.files)


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - DuplicateGroup
#
# Public Signals:
# - None
#
# Dependencies:
# - dataclasses
# - src.models.file_record