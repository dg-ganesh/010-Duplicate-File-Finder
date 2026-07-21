"""
Project : Duplicate File Finder
Project ID : 010

Menu Bar
"""

import tkinter as tk


class MenuBar:
    """
    Creates the application's menu bar.
    """

    def __init__(self, parent) -> None:

        self.parent = parent

        self.menu_bar = tk.Menu(parent)

        self._create_file_menu()
        self._create_scan_menu()
        self._create_help_menu()

        parent.config(menu=self.menu_bar)

    # ------------------------------------------------------------------
    # Menu Creation
    # ------------------------------------------------------------------

    def _create_file_menu(self) -> None:

        self.file_menu = tk.Menu(
            self.menu_bar,
            tearoff=False,
        )

        self.file_menu.add_command(
            label="Export Results",
            command=lambda: None,
        )

        self.file_menu.add_separator()

        self.file_menu.add_command(
            label="Exit",
            command=self.parent.quit,
        )

        self.menu_bar.add_cascade(
            label="File",
            menu=self.file_menu,
        )

    def _create_scan_menu(self) -> None:

        self.scan_menu = tk.Menu(
            self.menu_bar,
            tearoff=False,
        )

        self.scan_menu.add_command(
            label="Start Scan",
            command=lambda: None,
        )

        self.menu_bar.add_cascade(
            label="Scan",
            menu=self.scan_menu,
        )

    def _create_help_menu(self) -> None:

        self.help_menu = tk.Menu(
            self.menu_bar,
            tearoff=False,
        )

        self.help_menu.add_command(
            label="About",
            command=lambda: None,
        )

        self.menu_bar.add_cascade(
            label="Help",
            menu=self.help_menu,
        )

    # ------------------------------------------------------------------
    # Callback Registration
    # ------------------------------------------------------------------

    def set_start_scan_callback(
        self,
        callback,
    ) -> None:
        """
        Registers the Start Scan callback.
        """

        self.scan_menu.entryconfigure(
            "Start Scan",
            command=callback,
        )

    def set_export_callback(
        self,
        callback,
    ) -> None:
        """
        Registers the Export Results callback.
        """

        self.file_menu.entryconfigure(
            "Export Results",
            command=callback,
        )

    def set_about_callback(
        self,
        callback,
    ) -> None:
        """
        Registers the About callback.
        """

        self.help_menu.entryconfigure(
            "About",
            command=callback,
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - MenuBar
#
# Public Methods:
# - set_start_scan_callback()
# - set_export_callback()
# - set_about_callback()
#
# Public Signals:
# - File > Export Results
# - File > Exit
# - Scan > Start Scan
# - Help > About
#
# Dependencies:
# - tkinter