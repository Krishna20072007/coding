import tkinter as tk
from tkinter import filedialog
from openpyxl import Workbook, load_workbook


def save_formula():
    formula_name = entry_formula_name.get()
    subject = subject_var.get()
    formula = entry_formula.get("1.0", "end-1c")

    try:
        workbook = load_workbook("formulas.xlsx")

        # Check if the sheet for the subject exists, create it if necessary
        if subject not in workbook.sheetnames:
            workbook.create_sheet(subject)

            # Add header row to the new sheet
            new_sheet = workbook[subject]
            new_sheet["A1"] = "Formula Name"
            new_sheet["B1"] = "Formula"

        # Retrieve the sheet for the subject
        sheet = workbook[subject]

        # Check if the header row is present in the sheet
        header_row = next(sheet.iter_rows(min_row=1, max_row=1, values_only=True))
        if header_row != ("Formula Name", "Formula"):
            # If the header row is missing, add it to the sheet
            sheet.insert_rows(1)
            sheet["A1"] = "Formula Name"
            sheet["B1"] = "Formula"

        # Create a new row in the sheet and add the formula details
        sheet.append([formula_name, formula])

        # Save the workbook
        workbook.save("formulas.xlsx")

        clear_fields()
        status_label.config(text="Formula saved successfully.", fg="green")
    except FileNotFoundError:
        status_label.config(text="File not found.", fg="red")


def clear_fields():
    entry_formula_name.delete(0, tk.END)
    entry_formula.delete("1.0", tk.END)


def load_formulas():
    file_path = filedialog.askopenfilename(filetypes=[("Excel Files", "*.xlsx")])
    if file_path:
        try:
            workbook = load_workbook(file_path)

            # Clear the existing formula list
            formula_list.delete(0, tk.END)

            for sheet_name in workbook.sheetnames:
                sheet = workbook[sheet_name]

                # Read the header row
                header_row = next(sheet.iter_rows(min_row=1, max_row=1, values_only=True))
                if header_row == ("Formula Name", "Formula"):
                    # Iterate through the rows and add each formula to the list
                    for row in sheet.iter_rows(min_row=2, values_only=True):
                        formula_name, formula = row
                        formula_list.insert(tk.END, formula_name)

            status_label.config(text="Formulas loaded successfully.", fg="green")
        except FileNotFoundError:
            status_label.config(text="File not found.", fg="red")


def display_formula(event):
    selection = formula_list.curselection()
    if selection:
        index = selection[0]
        formula_name = formula_list.get(index)

        workbook = load_workbook("formulas.xlsx")

        for sheet_name in workbook.sheetnames:
            sheet = workbook[sheet_name]

            # Find the formula row based on the selected formula name
            for row in sheet.iter_rows(min_row=2, values_only=True):
                if row[0] == formula_name:
                    formula = row[1]

                    entry_formula_name.delete(0, tk.END)
                    entry_formula_name.insert(tk.END, formula_name)

                    entry_formula.delete("1.0", tk.END)
                    entry_formula.insert(tk.END, formula)

                    break


# Create the main window
window = tk.Tk()
window.title("Formula Book")

# Create labels
label_formula_name = tk.Label(window, text="Formula Name")
label_formula_name.grid(row=0, column=0, sticky="w")

label_subject = tk.Label(window, text="Subject")
label_subject.grid(row=1, column=0, sticky="w")

label_formula = tk.Label(window, text="Formula")
label_formula.grid(row=2, column=0, sticky="w")

# Create entry fields
entry_formula_name = tk.Entry(window)
entry_formula_name.grid(row=0, column=1, padx=10, pady=5)

# Create a dropdown menu for subject selection
subject_var = tk.StringVar()
subject_dropdown = tk.OptionMenu(window, subject_var, "Maths", "Physics", "Chemistry")
subject_dropdown.grid(row=1, column=1, padx=10, pady=5)

entry_formula = tk.Text(window, height=5, width=40)
entry_formula.grid(row=2, column=1, padx=10, pady=5)

# Create buttons
button_save = tk.Button(window, text="Save Formula", command=save_formula)
button_save.grid(row=3, column=0, padx=10, pady=5, sticky="w")

button_clear = tk.Button(window, text="Clear Fields", command=clear_fields)
button_clear.grid(row=3, column=1, padx=10, pady=5, sticky="w")

button_load = tk.Button(window, text="Load Formulas", command=load_formulas)
button_load.grid(row=3, column=1, padx=10, pady=5, sticky="e")

# Create formula list
formula_list = tk.Listbox(window, width=30)
formula_list.grid(row=0, column=2, rowspan=4, padx=10, pady=5, sticky="nsew")
formula_list.bind("<<ListboxSelect>>", display_formula)

# Create a scrollbar for the formula list
scrollbar = tk.Scrollbar(window, orient=tk.VERTICAL)
scrollbar.grid(row=0, column=3, rowspan=4, sticky="ns")
formula_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=formula_list.yview)

# Create status label
status_label = tk.Label(window, text="", fg="green")
status_label.grid(row=4, column=0, columnspan=3, padx=10, pady=5)

# Create a workbook object
workbook = Workbook()

# Adjust window size to fit content
window.update_idletasks()
window_width = max(window.winfo_width(), 400)
window_height = window.winfo_height()
window.geometry(f"{window_width}x{window_height}")

# Start the GUI event loop
window.mainloop()
