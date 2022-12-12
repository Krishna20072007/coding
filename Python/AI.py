import subprocess
import wolframalpha
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import feedparser
import smtplib
import ctypes
import time
import requests
import shutil
from clint.textui import progress
from bs4 import BeautifulSoup
from urllib.request import urlopen

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")

    else:
        speak("Good Evening Sir!")

    name = ("AI")
    speak("I am AI Sir")


def takeCommand():

    r = sr.Recognizer()

    with sr.Microphone() as source:

        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-us')
        print(f"You said: {query}\n")

    except Exception as e:
        print(e)
        print("Please try again")
        return "None"

    return query


if __name__ == '__main__':
    def clear(): return os.system('cls')

    wishMe()

    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("Opening Youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Search on Google\n")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")

        elif 'how are you' in query:
            speak("I am fine Sir")
            speak("How are you")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif 'exit' in query:
            exit()

        elif 'who made you' in query or 'who created you' in query:
            speak("I have been created by Krishna.")

        elif 'joke' in query:
            speak(pyjokes.get_joke())

        elif 'calculate" i'in  query:
            app_id = "Wolframalpha api id"
            client = wolframalpha.Client(app_id)
            indx = query.lower().split().index('calculate')
            query = query.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)

        elif 'search' in query or 'play' in query:
            query = query.replace("search", "")
            webbrowser.open(query)

        elif 'AI" in query':
            wishMe()
            speak("At your service Sir!")

        elif 'wikipedia" i' in query:
            webbrowser.open("wikipedia.com")

        elif 'Good Morning' or "Good Afternoon" or "Good Evening" in query:
            speak(query)
            speak("Sir")

        elif 'how are you"'in query:
            speak("I'm fine Sir, how about you?")

        elif 'i love you" ' in query:
            speak("I Love you too Sir")

        elif 'how are you"'in query:
            speak("I am good Sir ! How are you")

        elif 'all good' in query:
            speak('great to hear that')

        elif 'i dont understand' in query:
            speak('Ok')