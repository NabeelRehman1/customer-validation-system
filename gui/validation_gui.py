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
        self.root.geometry("1100x750")
        self.root.configure(bg="#f4f6f8")

        self.file_path = None
        self.validation_errors = []

        self.build_gui()

    def build_gui(self):

        style = ttk.Style()

        style.theme_use("default")

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        style.configure(
            "Treeview",
            rowheight=25
        )

        title = tk.Label(
            self.root,
            text="Customer Data Validation System",
            font=("Arial", 22, "bold"),
            bg="#f4f6f8",
            fg="#003366"
        )

        title.pack(pady=10)

        self.file_label = tk.Label(
            self.root,
            text="No file selected",
            font=("Arial", 10),
            bg="#f4f6f8"
        )

        self.file_label.pack(pady=5)

        button_frame = tk.Frame(
            self.root,
            bg="#f4f6f8"
        )

        button_frame.pack(pady=5)

        browse_button = tk.Button(
            button_frame,
            text="Browse Dataset",
            width=20,
            bg="#0078D7",
            fg="white",
            command=self.browse_file
        )

        browse_button.grid(row=0, column=0, padx=5)

        run_button = tk.Button(
            button_frame,
            text="Run Validation",
            width=20,
            bg="#28A745",
            fg="white",
            command=self.run_validation
        )

        run_button.grid(row=0, column=1, padx=5)

        export_button = tk.Button(
            button_frame,
            text="Export Report",
            width=20,
            bg="#6C757D",
            fg="white",
            command=self.export_report
        )

        export_button.grid(row=0, column=2, padx=5)

        self.summary_label = tk.Label(
            self.root,
            text="",
            font=("Arial", 12, "bold"),
            fg="red",
            bg="#f4f6f8"
        )

        self.summary_label.pack(pady=10)

        self.test_summary = tk.Label(
            self.root,
            text="",
            font=("Arial", 11, "bold"),
            fg="blue",
            bg="#f4f6f8"
        )

        self.test_summary.pack(pady=5)

        test_frame = tk.LabelFrame(
            self.root,
            text="Validation Test Results",
            font=("Arial", 10, "bold")
        )

        test_frame.pack(fill="x", padx=10, pady=5)

        self.test_tree = ttk.Treeview(
            test_frame,
            columns=("test", "status"),
            show="headings",
            height=8
        )

        self.test_tree.heading(
            "test",
            text="Validation Test"
        )

        self.test_tree.heading(
            "status",
            text="Status"
        )

        self.test_tree.column(
            "test",
            width=350
        )

        self.test_tree.column(
            "status",
            width=120
        )

        self.test_tree.tag_configure(
            "pass",
            background="#d4edda"
        )

        self.test_tree.tag_configure(
            "fail",
            background="#f8d7da"
        )

        self.test_tree.pack(
            fill="x",
            padx=5,
            pady=5
        )

        error_frame = tk.LabelFrame(
            self.root,
            text="Detailed Validation Errors",
            font=("Arial", 10, "bold")
        )

        error_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "row",
            "column",
            "error"
        )

        self.tree = ttk.Treeview(
            error_frame,
            columns=columns,
            show="headings",
            height=18
        )

        self.tree.heading(
            "row",
            text="Row"
        )

        self.tree.heading(
            "column",
            text="Column"
        )

        self.tree.heading(
            "error",
            text="Error"
        )

        self.tree.column(
            "row",
            width=80
        )

        self.tree.column(
            "column",
            width=150
        )

        self.tree.column(
            "error",
            width=650
        )

        self.tree.pack(
            fill="both",
            expand=True,
            padx=5,
            pady=5
        )

    def browse_file(self):

        file_path = filedialog.askopenfilename(
            filetypes=[
                ("Excel Files", "*.xlsx *.xls"),
                ("CSV Files", "*.csv"),
                ("All Files", "*.*")
            ]
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
                "Please select a file."
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

            for item in self.test_tree.get_children():
                self.test_tree.delete(item)

            tests = [
                "Required Column Validation",
                "Missing Value Validation",
                "Email Validation",
                "Phone Validation",
                "Customer ID Validation",
                "Customer Name Validation",
                "Document Type Validation",
                "Duplicate Validation"
            ]

            passed = 0
            failed = 0

            for test in tests:

                keyword = test.split()[0].lower()

                has_error = any(
                    keyword in str(error["column"]).lower()
                    or keyword in str(error["error"]).lower()
                    for error in self.validation_errors
                )

                if has_error:

                    failed += 1

                    self.test_tree.insert(
                        "",
                        "end",
                        values=(test, "FAIL"),
                        tags=("fail",)
                    )

                else:

                    passed += 1

                    self.test_tree.insert(
                        "",
                        "end",
                        values=(test, "PASS"),
                        tags=("pass",)
                    )

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

            self.test_summary.config(
                text=f"Tests Run: {len(tests)} | Passed: {passed} | Failed: {failed}"
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