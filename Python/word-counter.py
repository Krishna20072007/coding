import tkinter as tk

def count_words():
    text = input_text.get("1.0", "end-1c")
    word_count = len(text.split())
    char_count = len(text.replace(" ", "").replace("\n", ""))
    output_label.config(text="Word count: " + str(word_count) + "\nCharacter count: " + str(char_count))

# Create the main window
window = tk.Tk()
window.title("Word and Character Counter")

# Create the input text area
input_text = tk.Text(window, height=10, width=30)
input_text.pack()

# Create the "Count Words" button
count_button = tk.Button(window, text="Count Words", command=count_words)
count_button.pack()

# Create the output label
output_label = tk.Label(window, text="Word count: 0\nCharacter count: 0")
output_label.pack()

# Start the main loop
window.mainloop()
