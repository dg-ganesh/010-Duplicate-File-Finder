"""
Project : Duplicate File Finder
Project ID : 010

Scan Settings Model
"""

from dataclasses import dataclass
from pathlib import Path

from src.config import (
    DEFAULT_SCAN_METHOD,
    FOLLOW_SYMBOLIC_LINKS,
    RECURSIVE_SCAN_DEFAULT,
)


@dataclass
class ScanSettings:
    """
    Stores all user-selected scan settings.
    """

    folder: Path

    scan_method: str = DEFAULT_SCAN_METHOD

    recursive: bool = RECURSIVE_SCAN_DEFAULT

    follow_symbolic_links: bool = FOLLOW_SYMBOLIC_LINKS


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - ScanSettings
#
# Public Signals:
# - None
#
# Dependencies:
# - dataclasses
# - pathlib
# - src.config