import speech_recognition as sr

# Create a recognizer instance
r = sr.Recognizer()

# Capture audio input
print("Speak something...")

with sr.Microphone() as source:
    audio = r.listen(source)

# Perform speech recognition
try:
    text = r.recognize_google(audio)
    print("You said: " + text)
except sr.UnknownValueError:
    print("Sorry, I couldn't understand audio.")
except sr.RequestError:
    print("Sorry, speech recognition service is unavailable.")
