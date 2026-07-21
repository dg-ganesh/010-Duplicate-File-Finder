"""
Project : Duplicate File Finder
Project ID : 010

File Record Model
"""

from dataclasses import dataclass
from pathlib import Path
from typing import Optional


@dataclass
class FileRecord:
    """
    Represents a single file discovered during a scan.
    """

    path: Path
    name: str
    extension: str
    size: int
    modified_time: float

    content_hash: Optional[str] = None

    duplicate_group_id: Optional[int] = None

    is_duplicate: bool = False


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - FileRecord
#
# Public Signals:
# - None
#
# Dependencies:
# - dataclasses
# - pathlib
# - typing