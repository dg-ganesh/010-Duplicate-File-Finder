"""
Project : Duplicate File Finder
Project ID : 010

Options Panel
"""

import tkinter as tk
from tkinter import ttk

from src.config import (
    DEFAULT_SCAN_METHOD,
    SCAN_METHODS,
)


class OptionsPanel(ttk.LabelFrame):
    """
    Scan options panel.
    """

    def __init__(self, parent) -> None:

        super().__init__(parent, text="Scan Options")

        self.scan_method = tk.StringVar(
            value=DEFAULT_SCAN_METHOD
        )

        self._create_widgets()
        self._layout_widgets()

    # ------------------------------------------------------------------
    # Widget Creation
    # ------------------------------------------------------------------

    def _create_widgets(self) -> None:

        self.lbl_scan_method = ttk.Label(
            self,
            text="Scan Method"
        )

        self.cbo_scan_method = ttk.Combobox(
            self,
            textvariable=self.scan_method,
            values=SCAN_METHODS,
            state="readonly",
            width=30,
        )

        self.btn_start_scan = ttk.Button(
            self,
            text="Start Scan",
        )

    # ------------------------------------------------------------------
    # Layout
    # ------------------------------------------------------------------

    def _layout_widgets(self) -> None:

        self.columnconfigure(1, weight=1)

        self.lbl_scan_method.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w",
        )

        self.cbo_scan_method.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="w",
        )

        self.btn_start_scan.grid(
            row=0,
            column=2,
            padx=(20, 10),
            pady=10,
            sticky="e",
        )

    # ------------------------------------------------------------------
    # Public Methods
    # ------------------------------------------------------------------

    def get_scan_method(self) -> str:
        """
        Returns the selected scan method.
        """

        return self.scan_method.get()

    def set_scan_method(
        self,
        scan_method: str,
    ) -> None:
        """
        Updates the selected scan method.
        """

        self.scan_method.set(scan_method)

    def set_start_scan_callback(
        self,
        callback,
    ) -> None:
        """
        Registers the Start Scan button callback.
        """

        self.btn_start_scan.configure(
            command=callback
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - OptionsPanel
#
# Public Methods:
# - get_scan_method()
# - set_scan_method()
# - set_start_scan_callback()
#
# Public Signals:
# - Start Scan button
#
# Dependencies:
# - tkinter
# - tkinter.ttk
# - src.config