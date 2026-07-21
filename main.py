"""
Project : Duplicate File Finder
Project ID : 010

Application Entry Point

Revision History
----------------
1.0.0
- Initial implementation.

1.0.1
- Restored stable architecture.
- Removed SummaryPanel integration.
"""

import tkinter as tk

from src.config import (
    MIN_WINDOW_HEIGHT,
    MIN_WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_TITLE,
    WINDOW_WIDTH,
)
from src.ui.callbacks import ApplicationCallbacks
from src.ui.event_handlers import EventHandlers
from src.ui.folder_panel import FolderPanel
from src.ui.menu_bar import MenuBar
from src.ui.options_panel import OptionsPanel
from src.ui.progress_panel import ProgressPanel
from src.ui.results_panel import ResultsPanel


def create_application() -> tk.Tk:
    """
    Creates and initializes the application.
    """

    root = tk.Tk()

    root.title(WINDOW_TITLE)

    root.geometry(
        f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
    )

    root.minsize(
        MIN_WINDOW_WIDTH,
        MIN_WINDOW_HEIGHT,
    )

    # ----------------------------------------------------------
    # Window Layout
    # ----------------------------------------------------------

    root.columnconfigure(
        0,
        weight=1,
    )

    root.rowconfigure(
        2,
        weight=1,
    )

    # ----------------------------------------------------------
    # Menu
    # ----------------------------------------------------------

    menu_bar = MenuBar(root)

    # ----------------------------------------------------------
    # Panels
    # ----------------------------------------------------------

    folder_panel = FolderPanel(root)

    options_panel = OptionsPanel(root)

    results_panel = ResultsPanel(root)

    progress_panel = ProgressPanel(root)

    # ----------------------------------------------------------
    # Layout Panels
    # ----------------------------------------------------------

    folder_panel.grid(
        row=0,
        column=0,
        padx=10,
        pady=(10, 5),
        sticky="ew",
    )

    options_panel.grid(
        row=1,
        column=0,
        padx=10,
        pady=5,
        sticky="ew",
    )

    results_panel.grid(
        row=2,
        column=0,
        padx=10,
        pady=5,
        sticky="nsew",
    )

    progress_panel.grid(
        row=3,
        column=0,
        padx=10,
        pady=(5, 10),
        sticky="ew",
    )

    # ----------------------------------------------------------
    # Callbacks
    # ----------------------------------------------------------

    callbacks = ApplicationCallbacks(
        folder_panel=folder_panel,
        options_panel=options_panel,
        results_panel=results_panel,
        progress_panel=progress_panel,
    )

    # ----------------------------------------------------------
    # Event Handlers
    # ----------------------------------------------------------

    EventHandlers(
        root=root,
        menu_bar=menu_bar,
        folder_panel=folder_panel,
        options_panel=options_panel,
        results_panel=results_panel,
        progress_panel=progress_panel,
        callbacks=callbacks,
    )

    return root


def main() -> None:
    """
    Application entry point.
    """

    application = create_application()

    application.mainloop()


if __name__ == "__main__":
    main()


# =============================================================================
# Public Interface
# =============================================================================

# Public Functions:
# - create_application()
# - main()
#
# Public Signals:
# - None
#
# Dependencies:
# - tkinter
# - src.config
# - src.ui.*