import tkinter as tk
from tkinter import messagebox
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Function to encrypt the diary entry
def encrypt_entry(entry_text):
    encrypted_text = cipher_suite.encrypt(entry_text.encode())
    return encrypted_text

# Function to decrypt the diary entry
def decrypt_entry(encrypted_text):
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    return decrypted_text.decode()

# Function to save the diary entry
def save_entry():
    entry_text = text_entry.get("1.0", tk.END).strip()
    if entry_text:
        encrypted_text = encrypt_entry(entry_text)
        with open("diary.txt", "wb") as file:
            file.write(encrypted_text)
        messagebox.showinfo("Success", "Diary entry saved successfully.")
    else:
        messagebox.showwarning("Empty Entry", "Cannot save an empty diary entry.")

# Function to load the diary entry
def load_entry():
    try:
        with open("diary.txt", "rb") as file:
            encrypted_text = file.read()
        decrypted_text = decrypt_entry(encrypted_text)
        text_entry.delete("1.0", tk.END)
        text_entry.insert(tk.END, decrypted_text)
        messagebox.showinfo("Success", "Diary entry loaded successfully.")
    except FileNotFoundError:
        messagebox.showwarning("File Not Found", "No diary entry found.")

# Create the main window
window = tk.Tk()
window.title("Digital Diary")
window.geometry("400x300")

# Create a text entry field
text_entry = tk.Text(window, height=15, width=40)
text_entry.pack(pady=10)

# Create "Save" and "Load" buttons
save_button = tk.Button(window, text="Save", command=save_entry)
save_button.pack(side=tk.LEFT, padx=10)
load_button = tk.Button(window, text="Load", command=load_entry)
load_button.pack(side=tk.LEFT, padx=10)

# Run the main event loop
window.mainloop()
