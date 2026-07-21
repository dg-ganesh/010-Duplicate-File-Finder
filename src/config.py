"""
Project : Duplicate File Finder
Project ID : 010

Application Configuration

Revision History
----------------
1.0.0
- Initial implementation.

1.0.1
- Renamed scan methods for improved usability.
- Added user-friendly scan names while maintaining
  backward compatibility.
"""

# =============================================================================
# Project Information
# =============================================================================

PROJECT_NAME = "Duplicate File Finder"
PROJECT_ID = "010"
APPLICATION_VERSION = "1.0.0"

# =============================================================================
# Window Configuration
# =============================================================================

WINDOW_TITLE = f"{PROJECT_NAME} v{APPLICATION_VERSION}"

WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 700

MIN_WINDOW_WIDTH = 900
MIN_WINDOW_HEIGHT = 600

# =============================================================================
# Scan Methods
# =============================================================================

# User-facing scan names
SCAN_METHOD_QUICK = "Quick Scan (File Size)"
SCAN_METHOD_VERIFIED = "Verified Scan (SHA-256)"

# Backward-compatible aliases
SCAN_METHOD_ATTRIBUTE = SCAN_METHOD_QUICK
SCAN_METHOD_CONTENT = SCAN_METHOD_VERIFIED

SCAN_METHODS = [
    SCAN_METHOD_QUICK,
    SCAN_METHOD_VERIFIED,
]

DEFAULT_SCAN_METHOD = SCAN_METHOD_VERIFIED

# =============================================================================
# Hash Configuration
# =============================================================================

HASH_ALGORITHM = "sha256"

# Number of bytes read per iteration while hashing files.
HASH_BLOCK_SIZE = 65536  # 64 KB

# =============================================================================
# File Enumeration
# =============================================================================

RECURSIVE_SCAN_DEFAULT = True

FOLLOW_SYMBOLIC_LINKS = False

# =============================================================================
# Export Configuration
# =============================================================================

EXPORT_FORMAT_CSV = "CSV"

SUPPORTED_EXPORT_FORMATS = [
    EXPORT_FORMAT_CSV,
]

DEFAULT_EXPORT_FILENAME = "duplicate_files_report.csv"

DEFAULT_TEXT_ENCODING = "utf-8"

# =============================================================================
# Logging Configuration
# =============================================================================

LOG_FILE_NAME = "duplicate_file_finder.log"

LOG_LEVEL = "INFO"

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(module)s | %(message)s"
)

# =============================================================================
# User Interface Constants
# =============================================================================

DEFAULT_PADDING = 10

SECTION_SPACING = 8

BUTTON_WIDTH = 15

STATUS_REFRESH_INTERVAL_MS = 250

PROGRESS_BAR_MAXIMUM = 100

# =============================================================================
# Results Table Defaults
# =============================================================================

COLUMN_WIDTH_FILE_NAME = 280

COLUMN_WIDTH_FILE_SIZE = 110

COLUMN_WIDTH_FILE_PATH = 520

COLUMN_WIDTH_DUPLICATE_GROUP = 110

# =============================================================================
# Application Messages
# =============================================================================

STATUS_READY = "Ready"

STATUS_SCANNING = "Scanning..."

STATUS_SCAN_COMPLETE = "Scan complete."

STATUS_NO_DUPLICATES = "No duplicate files found."

STATUS_DUPLICATES_FOUND = "Duplicate files found."

STATUS_EXPORT_COMPLETE = "Export completed successfully."

STATUS_DELETE_COMPLETE = "Selected files deleted successfully."

STATUS_SCAN_CANCELLED = "Scan cancelled."

# =============================================================================
# Dialog Messages
# =============================================================================

CONFIRM_DELETE_TITLE = "Delete Files"

CONFIRM_DELETE_MESSAGE = (
    "Are you sure you want to permanently delete the selected file(s)?"
)

ERROR_INVALID_FOLDER = "Please select a valid folder."

ERROR_NO_RESULTS = "There are no results to export."

# =============================================================================
# File Dialog Filters
# =============================================================================

CSV_FILE_FILTER = (
    ("CSV Files", "*.csv"),
    ("All Files", "*.*"),
)

# =============================================================================
# Reserved for Future Versions
# =============================================================================

# Future scan modes
# Future export formats
# Theme settings
# User preferences
# Localization
# Performance tuning
# Cache configuration

# =============================================================================
# Public Constants
# =============================================================================

# Public Interface:
# - All module constants
#
# Public Signals:
# - None
#
# Dependencies:
# - None