import os
import tkinter as tk
from tkinter import filedialog


def list_files():
    files = os.listdir('.')
    file_list.delete(0, tk.END)  # Clear the listbox
    for file in files:
        file_list.insert(tk.END, file)


def create_file():
    filename = file_entry.get()
    try:
        with open(filename, 'w') as file:
            file.write('')
        status_label.config(text="File created successfully!", fg="green")
    except IOError:
        status_label.config(text="Error creating the file.", fg="red")


def delete_file():
    filename = file_entry.get()
    try:
        os.remove(filename)
        status_label.config(text="File deleted successfully!", fg="green")
    except FileNotFoundError:
        status_label.config(text="File not found.", fg="red")
    except PermissionError:
        status_label.config(text="Permission denied.", fg="red")

    # Refresh the file list
    list_files()


def browse_file():
    filename = filedialog.askopenfilename()
    file_entry.delete(0, tk.END)
    file_entry.insert(tk.END, filename)


root = tk.Tk()
root.title("File Manager")
root.

# Create file listbox
file_list = tk.Listbox(root, width=50)
file_list.pack(pady=10)

# Create file entry
file_entry = tk.Entry(root, width=40)
file_entry.pack(pady=5)

# Create buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

list_button = tk.Button(button_frame, text="List Files", command=list_files)
list_button.grid(row=0, column=0, padx=5)

create_button = tk.Button(button_frame, text="Create File", command=create_file)
create_button.grid(row=0, column=1, padx=5)

delete_button = tk.Button(button_frame, text="Delete File", command=delete_file)
delete_button.grid(row=0, column=2, padx=5)

browse_button = tk.Button(button_frame, text="Browse", command=browse_file)
browse_button.grid(row=0, column=3, padx=5)

# Create status label
status_label = tk.Label(root, text="", fg="green")
status_label.pack(pady=5)

root.mainloop()
