"""
Project : Duplicate File Finder
Project ID : 010

Results Panel

Revision History
----------------
1.1.0
- Redesigned duplicate analysis view.
- Human readable file sizes.
- Original / Duplicate status.
- Folder column replaces full path.
"""

from tkinter import ttk

from src.models.duplicate_group_model import DuplicateGroup


class ResultsPanel(ttk.LabelFrame):
    """
    Displays duplicate analysis results.
    """

    def __init__(self, parent) -> None:

        super().__init__(
            parent,
            text="Duplicate Analysis",
        )

        self._create_widgets()
        self._layout_widgets()

    # ---------------------------------------------------------
    # Widget Creation
    # ---------------------------------------------------------

    def _create_widgets(self) -> None:

        columns = (
            "Group",
            "Status",
            "File Name",
            "Size",
            "Folder",
        )

        self.tree = ttk.Treeview(
            self,
            columns=columns,
            show="headings",
            selectmode="browse",
        )

        self.tree.heading(
            "Group",
            text="Group",
        )

        self.tree.heading(
            "Status",
            text="Status",
        )

        self.tree.heading(
            "File Name",
            text="File Name",
        )

        self.tree.heading(
            "Size",
            text="Size",
        )

        self.tree.heading(
            "Folder",
            text="Folder",
        )

        self.tree.column(
            "Group",
            width=70,
            anchor="center",
            stretch=False,
        )

        self.tree.column(
            "Status",
            width=100,
            anchor="center",
            stretch=False,
        )

        self.tree.column(
            "File Name",
            width=260,
            anchor="w",
        )

        self.tree.column(
            "Size",
            width=110,
            anchor="e",
            stretch=False,
        )

        self.tree.column(
            "Folder",
            width=520,
            anchor="w",
        )

        self.scrollbar = ttk.Scrollbar(
            self,
            orient="vertical",
            command=self.tree.yview,
        )

        self.tree.configure(
            yscrollcommand=self.scrollbar.set,
        )

        self.tree.tag_configure(
            "original",
            background="#EAF7EA",
        )

        self.tree.tag_configure(
            "duplicate",
            background="white",
        )

    # ---------------------------------------------------------
    # Layout
    # ---------------------------------------------------------

    def _layout_widgets(self) -> None:

        self.columnconfigure(
            0,
            weight=1,
        )

        self.rowconfigure(
            0,
            weight=1,
        )

        self.tree.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=(10, 0),
            pady=10,
        )

        self.scrollbar.grid(
            row=0,
            column=1,
            sticky="ns",
            padx=(0, 10),
            pady=10,
        )

    # ---------------------------------------------------------
    # Public Helpers
    # ---------------------------------------------------------

    def set_scan_title(
        self,
        scan_method: str,
    ) -> None:
        """
        Updates the panel title to indicate
        the scan method used.
        """

        self.configure(
            text=f"Duplicate Analysis - {scan_method}"
        )

    # ---------------------------------------------------------
    # Private Helpers
    # ---------------------------------------------------------

    @staticmethod
    def _format_size(
        size: int,
    ) -> str:
        """
        Converts bytes into a human-readable string.
        """

        value = float(size)

        units = (
            "B",
            "KB",
            "MB",
            "GB",
            "TB",
        )

        for unit in units:

            if value < 1024 or unit == units[-1]:

                if unit == "B":
                    return f"{int(value)} B"

                return f"{value:.1f} {unit}"

            value /= 1024

    @staticmethod
    def _get_status(
        is_original: bool,
    ) -> tuple[str, str]:
        """
        Returns the row status and tag.
        """

        if is_original:
            return (
                "Original",
                "original",
            )

        return (
            "Duplicate",
            "duplicate",
        )

    @staticmethod
    def _get_folder(
        file_record,
    ) -> str:
        """
        Returns only the parent folder.
        """

        return str(
            file_record.path.parent
        )

    # ---------------------------------------------------------
    # Public Methods
    # ---------------------------------------------------------

    def clear(self) -> None:
        """
        Clears all displayed results.
        """

        self.tree.delete(
            *self.tree.get_children()
        )


    # ---------------------------------------------------------
    # Results
    # ---------------------------------------------------------

    def load_results(
        self,
        duplicate_groups: list[DuplicateGroup],
    ) -> None:
        """
        Displays duplicate groups in the results table.
        """

        self.clear()

        for group in duplicate_groups:

            is_original = True

            for file in group.files:

                status, tag = self._get_status(
                    is_original
                )

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        group.group_id,
                        status,
                        file.name,
                        self._format_size(
                            file.size
                        ),
                        self._get_folder(
                            file
                        ),
                    ),
                    tags=(tag,),
                )

                is_original = False

    # ---------------------------------------------------------
    # Selection
    # ---------------------------------------------------------

    def get_selected_item(self):
        """
        Returns the selected TreeView item.

        Returns
        -------
        dict | None
            Selected TreeView item or None if nothing
            is selected.
        """

        selection = self.tree.selection()

        if not selection:
            return None

        return self.tree.item(
            selection[0]
        )


# =============================================================================
# Public Interface
# =============================================================================

# Public Classes:
# - ResultsPanel
#
# Public Methods:
# - set_scan_title()
# - clear()
# - load_results()
# - get_selected_item()
#
# Public Signals:
# - TreeView selection
#
# Dependencies:
# - tkinter
# - tkinter.ttk
# - src.models.duplicate_group_model