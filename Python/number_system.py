import tkinter as tk

def convert():
    number = entry_number.get()
    base = int(combo_base.get())

    try:
        decimal = int(number, base)
        entry_decimal.delete(0, tk.END)
        entry_decimal.insert(tk.END, str(decimal))
    except ValueError:
        entry_decimal.delete(0, tk.END)
        entry_decimal.insert(tk.END, "Invalid number")

root = tk.Tk()
root.title("Number System Converter")

label_number = tk.Label(root, text="Number:")
label_number.grid(row=0, column=0, padx=5, pady=5)

entry_number = tk.Entry(root)
entry_number.grid(row=0, column=1, padx=5, pady=5)

label_base = tk.Label(root, text="Base:")
label_base.grid(row=1, column=0, padx=5, pady=5)

combo_base = tk.Spinbox(root, values=["2", "8", "10", "16"])
combo_base.grid(row=1, column=1, padx=5, pady=5)

button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

label_decimal = tk.Label(root, text="Decimal:")
label_decimal.grid(row=3, column=0, padx=5, pady=5)

entry_decimal = tk.Entry(root)
entry_decimal.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()
