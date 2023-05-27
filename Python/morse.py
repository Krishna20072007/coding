import tkinter as tk

# Morse code dictionary
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
    '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
    ' ': '/'
}

# Reverse the Morse code dictionary
reverse_morse_code = {v: k for k, v in morse_code.items()}


def translate_to_morse(text):
    morse = []
    for char in text:
        if char.upper() in morse_code:
            morse.append(morse_code[char.upper()])
    return ' '.join(morse)


def translate_to_text(morse):
    text = []
    morse_words = morse.split('/')
    for word in morse_words:
        for code in word.split(' '):
            if code in reverse_morse_code:
                text.append(reverse_morse_code[code])
    return ''.join(text)


def translate_text():
    input_text = text_entry.get('1.0', 'end-1c')
    morse = translate_to_morse(input_text)
    morse_entry.delete('1.0', tk.END)
    morse_entry.insert('1.0', morse)


def translate_morse():
    input_morse = morse_entry.get('1.0', 'end-1c')
    text = translate_to_text(input_morse)
    text_entry.delete('1.0', tk.END)
    text_entry.insert('1.0', text)


# Create the GUI
window = tk.Tk()
window.title('Morse Code Translator')
window.resizable(False, False)

# Text entry for input
text_entry = tk.Text(window, height=5, width=30)
text_entry.pack()

# Button to translate text to Morse code
to_morse_button = tk.Button(window, text='Translate to Morse', command=translate_text)
to_morse_button.pack()

# Display area for Morse code
morse_entry = tk.Text(window, height=5, width=30)
morse_entry.pack()

# Button to translate Morse code to text
to_text_button = tk.Button(window, text='Translate to Text', command=translate_morse)
to_text_button.pack()

window.mainloop()
