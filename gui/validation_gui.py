import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

import pandas as pd

from facade.validation_facade import ValidationFacade
from reports.report_generator import ReportGenerator


class ValidationGUI:

    def __init__(self, root):

        self.root = root
        self.root.title("Customer Data Validation System")
        self.root.geometry("900x600")

        self.file_path = None
        self.validation_errors = []

        self.build_gui()

    def build_gui(self):

        title = tk.Label(
            self.root,
            text="Customer Data Validation System",
            font=("Arial", 18, "bold")
        )

        title.pack(pady=10)

        self.file_label = tk.Label(
            self.root,
            text="No file selected",
            font=("Arial", 10)
        )

        self.file_label.pack(pady=5)

        browse_button = tk.Button(
            self.root,
            text="Browse CSV File",
            width=20,
            command=self.browse_file
        )

        browse_button.pack(pady=5)

        run_button = tk.Button(
            self.root,
            text="Run Validation",
            width=20,
            command=self.run_validation
        )

        run_button.pack(pady=5)

        export_button = tk.Button(
            self.root,
            text="Export Report",
            width=20,
            command=self.export_report
        )

        export_button.pack(pady=5)

        self.summary_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 10, "bold")
        )

        self.summary_label.pack(pady=10)

        columns = ("row", "column", "error")

        self.tree = ttk.Treeview(
            self.root,
            columns=columns,
            show="headings",
            height=18
        )

        self.tree.heading("row", text="Row")
        self.tree.heading("column", text="Column")
        self.tree.heading("error", text="Error")

        self.tree.column("row", width=80)
        self.tree.column("column", width=150)
        self.tree.column("error", width=500)

        self.tree.pack(fill="both", expand=True, padx=10, pady=10)

    def browse_file(self):

        file_path = filedialog.askopenfilename(
            filetypes=[
            ("Excel Files", "*.xlsx *.xls"),
            ("CSV Files", "*.csv"),
            ("All Files", "*.*")]
        )

        if file_path:

            self.file_path = file_path

            self.file_label.config(
                text=file_path
            )

    def run_validation(self):

        if not self.file_path:

            messagebox.showerror(
                "Error",
                "Please select a CSV file."
            )

            return

        try:

            if self.file_path.endswith(".csv"):
                df = pd.read_csv(self.file_path)
            else:
                df = pd.read_excel(self.file_path)

            facade = ValidationFacade()

            self.validation_errors = facade.validate(df)

            for item in self.tree.get_children():
                self.tree.delete(item)

            for error in self.validation_errors:

                self.tree.insert(
                    "",
                    "end",
                    values=(
                        error["row"],
                        error["column"],
                        error["error"]
                    )
                )

            self.summary_label.config(
                text=f"Total Errors Found: {len(self.validation_errors)}"
            )

            messagebox.showinfo(
                "Success",
                "Validation completed."
            )

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    def export_report(self):

        if len(self.validation_errors) == 0:

            messagebox.showwarning(
                "Warning",
                "No validation results to export."
            )

            return

        output_path = filedialog.asksaveasfilename(
            defaultextension=".xlsx",
            filetypes=[("Excel File", "*.xlsx")]
        )

        if output_path:

            ReportGenerator.generate(
                self.validation_errors,
                output_path
            )

            messagebox.showinfo(
                "Success",
                "Report exported successfully."
            )