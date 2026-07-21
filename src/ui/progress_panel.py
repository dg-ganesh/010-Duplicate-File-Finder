"""
Project : Duplicate File Finder
Project ID : 010

Progress Panel
"""

import tkinter as tk
from tkinter import ttk

from src.config import (
    PROGRESS_BAR_MAXIMUM,
    STATUS_READY,
)


class ProgressPanel(ttk.LabelFrame):
    """
    Displays scan progress and application status.
    """

    def __init__(self, parent) -> None:

        super().__init__(parent, text="Progress")

        self.status = tk.StringVar(value=STATUS_READY)
        self.progress = tk.IntVar(value=0)

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self) -> None:

        self.progress_bar = ttk.Progressbar(
            self,
            orient="horizontal",
            mode="determinate",
            maximum=PROGRESS_BAR_MAXIMUM,
            variable=self.progress,
        )

        self.lbl_status = ttk.Label(
            self,
            textvariable=self.status,
            anchor="w",
        )

        self.lbl_percentage = ttk.Label(
            self,
            text="0%",
            width=6,
            anchor="e",
        )

    def _layout_widgets(self) -> None:

        self.columnconfigure(0, weight=1)

        self.progress_bar.grid(
            row=0,
            column=0,
            padx=10,
            pady=(10, 5),
            sticky="ew",
        )

        self.lbl_percentage.grid(
            row=0,
            column=1,
            padx=(0, 10),
            pady=(10, 5),
            sticky="e",
        )

        self.lbl_status.grid(
            row=1,
            column=0,
            columnspan=2,
            padx=10,
            pady=(0, 10),
            sticky="w",
        )

    def reset(self) -> None:
        """
        Resets the progress panel.
        """

        self.set_progress(0)
        self.set_status(STATUS_READY)

    def set_progress(self, value: int) -> None:
        """
        Updates the progress bar.
        """

        value = max(
            0,
            min(PROGRESS_BAR_MAXIMUM, value)
        )

        self.progress.set(value)

        self.lbl_percentage.config(
            text=f"{value}%"
        )

    def set_status(self, message: str) -> None:
        """
        Updates the status message.
        """

        self.status.set(message)

    def complete(
        self,
        message: str,
    ) -> None:
        """
        Marks the current operation as complete.
        """

        self.set_progress(PROGRESS_BAR_MAXIMUM)
        self.set_status(message)


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - ProgressPanel
#
# Public Methods:
# - reset()
# - set_progress()
# - set_status()
# - complete()
#
# Public Signals:
# - None
#
# Dependencies:
# - tkinter
# - tkinter.ttk
# - src.config