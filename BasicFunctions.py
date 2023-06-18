import pyttsx3
import speech_recognition as sr
from datetime import datetime


# setting up engine
engine = pyttsx3.init('sapi5')

# set rate
engine.setProperty('rate', 180)

# set volume
engine.setProperty('volume', 1.0)

# set voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# enabling jarvis voice
def Speak(text):
    engine.say(text)
    print(f"JARVIS : {text}")
    engine.runAndWait()


# Speak("")


# enabling jarvis ears
def Listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Thinking...')
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        return ""
    print(f"You : {query}")
    return query


# Listen()


# greeting function
def Greet():
    hour = datetime.now().hour
    if (hour >= 1) and (hour < 12):
        Speak(f"Good Morning Bhavin")
    elif (hour >= 12) and (hour < 16):
        Speak(f"Good afternoon Bhavin")
    elif (hour >= 16) and (hour <= 22):
        Speak(f"Good Evening Bhavin")
    Speak("I am Jarvis. How may I assist you?")


# Greet()


# exit function
def Exit():
    hour = datetime.now().hour
    if 20 <= hour < 6:
        Speak("Good night sir, take care!")
    else:
        Speak('Have a good day sir!')
    exit()


# Exit()
