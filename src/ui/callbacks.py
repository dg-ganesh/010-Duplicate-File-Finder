"""
Project : Duplicate File Finder
Project ID : 010

Application Callbacks

Revision History
----------------
1.0.0
- Initial implementation.

1.0.1
- Restored stable architecture.
- Removed ScanResult dependency.

1.1.0
- Integrated Duplicate Analysis panel.
- Dynamic scan title.
- Improved scan completion messages.
"""

from pathlib import Path
from tkinter import messagebox

from src.core.scan_engine import scan_folder
from src.models.scan_settings import ScanSettings
from src.services.logging_service import get_logger

logger = get_logger()


class ApplicationCallbacks:
    """
    Handles communication between the
    user interface and the application backend.
    """

    def __init__(
        self,
        folder_panel,
        options_panel,
        results_panel,
        progress_panel,
    ) -> None:

        self.folder_panel = folder_panel
        self.options_panel = options_panel
        self.results_panel = results_panel
        self.progress_panel = progress_panel

    # ------------------------------------------------------------------
    # Private Methods
    # ------------------------------------------------------------------

    def _build_scan_settings(self) -> ScanSettings:
        """
        Creates a ScanSettings object using
        the current UI selections.
        """

        return ScanSettings(
            folder=Path(
                self.folder_panel.get_folder()
            ),
            scan_method=self.options_panel.get_scan_method(),
            recursive=self.folder_panel.is_recursive(),
        )

    # ------------------------------------------------------------------
    # Public Methods
    # ------------------------------------------------------------------

    def start_scan(self) -> None:
        """
        Executes a duplicate file scan.
        """

        try:

            logger.info(
                "Starting duplicate scan."
            )

            self.results_panel.clear()

            self.progress_panel.reset()

            self.progress_panel.set_status(
                "Preparing scan..."
            )

            settings = self._build_scan_settings()

            self.progress_panel.set_progress(20)

            self.progress_panel.set_status(
                "Scanning files..."
            )

            duplicate_groups = scan_folder(
                settings
            )

            self.progress_panel.set_progress(80)

            self.progress_panel.set_status(
                "Loading results..."
            )

            # ------------------------------------------
            # Update Results Panel
            # ------------------------------------------

            self.results_panel.set_scan_title(
                settings.scan_method
            )

            self.results_panel.load_results(
                duplicate_groups
            )

            # ------------------------------------------
            # Final Status
            # ------------------------------------------

            if duplicate_groups:

                total_groups = len(
                    duplicate_groups
                )

                total_duplicates = sum(
                    group.duplicate_count
                    for group in duplicate_groups
                )

                self.progress_panel.complete(
                    f"Scan completed. "
                    f"{total_groups} group(s), "
                    f"{total_duplicates} duplicate file(s) found."
                )

            else:

                self.progress_panel.complete(
                    "Scan completed. No duplicate files found."
                )

            logger.info(
                "Duplicate scan completed."
            )

        except Exception as ex:

            logger.exception(
                "Duplicate scan failed."
            )

            self.results_panel.clear()

            self.progress_panel.reset()

            messagebox.showerror(
                "Duplicate File Finder",
                str(ex),
            )

    def clear_results(self) -> None:
        """
        Clears all displayed scan results.
        """

        self.results_panel.clear()

        self.progress_panel.reset()

        logger.info(
            "Results cleared."
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - ApplicationCallbacks
#
# Public Methods:
# - start_scan()
# - clear_results()
#
# Public Signals:
# - None
#
# Dependencies:
# - pathlib
# - tkinter.messagebox
# - src.core.scan_engine
# - src.models.scan_settings
# - src.services.logging_service