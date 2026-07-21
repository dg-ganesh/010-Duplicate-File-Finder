"""
Project : Duplicate File Finder
Project ID : 010

Folder Selection Panel
"""

import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class FolderPanel(ttk.LabelFrame):
    """
    Folder selection panel.
    """

    def __init__(self, parent) -> None:
        super().__init__(parent, text="Folder Selection")

        self.folder_path = tk.StringVar()
        self.recursive = tk.BooleanVar(value=True)

        self._create_widgets()
        self._layout_widgets()

    def _create_widgets(self) -> None:

        self.lbl_folder = ttk.Label(
            self,
            text="Folder"
        )

        self.txt_folder = ttk.Entry(
            self,
            textvariable=self.folder_path,
            width=70
        )

        self.btn_browse = ttk.Button(
            self,
            text="Browse...",
            command=self.browse_folder
        )

        self.chk_recursive = ttk.Checkbutton(
            self,
            text="Include Subfolders",
            variable=self.recursive
        )

    def _layout_widgets(self) -> None:

        self.columnconfigure(1, weight=1)

        self.lbl_folder.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            sticky="w"
        )

        self.txt_folder.grid(
            row=0,
            column=1,
            padx=10,
            pady=10,
            sticky="ew"
        )

        self.btn_browse.grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        self.chk_recursive.grid(
            row=1,
            column=1,
            padx=10,
            pady=(0, 10),
            sticky="w"
        )

    def browse_folder(self) -> None:
        """
        Opens the folder selection dialog.
        """

        folder = filedialog.askdirectory()

        if folder:
            self.folder_path.set(folder)

    def get_folder(self) -> str:
        """
        Returns the selected folder.
        """

        return self.folder_path.get()

    def is_recursive(self) -> bool:
        """
        Returns True if recursive scanning
        is enabled.
        """

        return self.recursive.get()


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - FolderPanel
#
# Public Methods:
# - browse_folder()
# - get_folder()
# - is_recursive()
#
# Public Signals:
# - Browse button click
# - Recursive checkbox state
#
# Dependencies:
# - tkinter
# - tkinter.ttk