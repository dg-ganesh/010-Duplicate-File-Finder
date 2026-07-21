"""
Project : Duplicate File Finder
Project ID : 010

Event Handlers
"""

from tkinter import messagebox


class EventHandlers:
    """
    Centralizes all UI event bindings.
    """

    def __init__(
        self,
        root,
        menu_bar,
        folder_panel,
        options_panel,
        results_panel,
        progress_panel,
        callbacks,
    ) -> None:

        self.root = root
        self.menu_bar = menu_bar
        self.folder_panel = folder_panel
        self.options_panel = options_panel
        self.results_panel = results_panel
        self.progress_panel = progress_panel
        self.callbacks = callbacks

        self._bind_menu_events()
        self._bind_button_events()
        self._bind_keyboard_events()
        self._bind_treeview_events()

    # ------------------------------------------------------------------
    # Menu Events
    # ------------------------------------------------------------------

    def _bind_menu_events(self) -> None:

        self.menu_bar.set_start_scan_callback(
            self.callbacks.start_scan
        )

        self.menu_bar.set_export_callback(
            self._export_results
        )

        self.menu_bar.set_about_callback(
            self._about
        )

    # ------------------------------------------------------------------
    # Button Events
    # ------------------------------------------------------------------

    def _bind_button_events(self) -> None:

        self.options_panel.set_start_scan_callback(
            self.callbacks.start_scan
        )

    # ------------------------------------------------------------------
    # Keyboard Events
    # ------------------------------------------------------------------

    def _bind_keyboard_events(self) -> None:

        self.root.bind(
            "<F5>",
            lambda event: self.callbacks.start_scan()
        )

        self.root.bind(
            "<Escape>",
            lambda event: self.callbacks.clear_results()
        )

    # ------------------------------------------------------------------
    # TreeView Events
    # ------------------------------------------------------------------

    def _bind_treeview_events(self) -> None:

        self.results_panel.tree.bind(
            "<<TreeviewSelect>>",
            self._on_tree_selection,
        )

    def _on_tree_selection(self, event) -> None:
        """
        Reserved for future use.
        """
        pass

    # ------------------------------------------------------------------
    # Placeholder Actions
    # ------------------------------------------------------------------

    def _export_results(self) -> None:

        messagebox.showinfo(
            "Duplicate File Finder",
            "Export functionality will be available in a future update."
        )

    def _about(self) -> None:

        messagebox.showinfo(
            "About",
            "Duplicate File Finder\n"
            "Version 1.0.0\n\n"
            "Project ID : 010"
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - EventHandlers
#
# Public Signals:
# - F5 -> Start Scan
# - Escape -> Clear Results
# - Scan Menu
# - Start Scan Button
# - About Menu
# - Export Menu
#
# Dependencies:
# - tkinter
# - tkinter.messagebox