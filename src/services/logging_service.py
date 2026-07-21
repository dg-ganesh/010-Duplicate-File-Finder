"""
Project : Duplicate File Finder
Project ID : 010

Logging Service
"""

import logging
from pathlib import Path

from src.config import (
    LOG_FILE_NAME,
    LOG_FORMAT,
    LOG_LEVEL,
)

# Module-level logger instance
_logger = None


def get_logger() -> logging.Logger:
    """
    Returns the application's configured logger.

    The logger is initialized only once and reused
    throughout the application.
    """
    global _logger

    if _logger is not None:
        return _logger

    log_file = Path(LOG_FILE_NAME)

    logger = logging.getLogger("DuplicateFileFinder")

    if logger.handlers:
        _logger = logger
        return logger

    logger.setLevel(getattr(logging, LOG_LEVEL.upper(), logging.INFO))

    formatter = logging.Formatter(LOG_FORMAT)

    file_handler = logging.FileHandler(
        log_file,
        encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.propagate = False

    logger.info("=" * 60)
    logger.info("Application Started")

    _logger = logger

    return logger


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - get_logger()
#
# Public Signals:
# - None
#
# Dependencies:
# - logging
# - pathlib
# - src.config