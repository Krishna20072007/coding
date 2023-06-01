from cryptography.fernet import Fernet
from tkinter import *
import tkinter.messagebox as messagebox

# Generate a key for encryption/decryption
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# Load the encryption key
def load_key():
    try:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
            return key
    except FileNotFoundError:
        messagebox.showerror("Error", "Key file not found!")
        exit()

# Encrypt a password
def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

# Decrypt a password
def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password)
    return decrypted_password.decode()

# Save a password
def save_password():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if website and username and password:
        encrypted_password = encrypt_password(password, key)
        with open("passwords.txt", "a") as password_file:
            password_file.write(f"Website: {website}\nUsername: {username}\nPassword: {encrypted_password.decode()}\n\n")
        messagebox.showinfo("Success", "Password saved successfully!")
        clear_entries()
    else:
        messagebox.showerror("Error", "Please fill in all fields!")

# Retrieve saved passwords
def retrieve_passwords():
    passwords = ""
    with open("passwords.txt", "r") as password_file:
        passwords = password_file.read()
    messagebox.showinfo("Saved Passwords", passwords)

# Clear input fields
def clear_entries():
    website_entry.delete(0, END)
    username_entry.delete(0, END)
    password_entry.delete(0, END)

# Create the GUI
window = Tk()
window.title("Password Manager")

# Generate/load encryption key
generate_key()
key = load_key()

# Website field
website_label = Label(window, text="Website:")
website_label.pack()
website_entry = Entry(window)
website_entry.pack()

# Username field
username_label = Label(window, text="Username:")
username_label.pack()
username_entry = Entry(window)
username_entry.pack()

# Password field
password_label = Label(window, text="Password:")
password_label.pack()
password_entry = Entry(window, show="*")
password_entry.pack()

# Save password button
save_button = Button(window, text="Save Password", command=save_password)
save_button.pack()

# Retrieve passwords button
retrieve_button = Button(window, text="Retrieve Passwords", command=retrieve_passwords)
retrieve_button.pack()

# Clear entries button
clear_button = Button(window, text="Clear Entries", command=clear_entries)
clear_button.pack()

# Run the GUI
window.mainloop()
