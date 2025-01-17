import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import spotify
import webbrowser
import os
from datetime import date

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Boss!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Boss!")

    else:
        speak("Good Evening Boss!")

    speak("I am Friday. Please tell me how may i help you")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1

        audio = r.listen(source)

    try:
        print("Recogninzing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: , {query}\n")

    except BaseException as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:

        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia... ,,sir')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak('opening youtube,, Sir')

        elif 'open google' in query:
            webbrowser.open("google.com")
            speak('opening google,,Master')

        elif 'open song' in query:
            webbrowser.open("spotify.com")
            speak('opening spotify Sir')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is{strTime}")

        elif 'open vs code' in query:
            codePath = "C:\\Users\\Lenovo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak('opening virtual studio code Master')

        elif 'open code 2' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm 2024.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)
            speak('opening pycharm boss')

        elif 'the date' in query:
            today = date.today()
            print(today)
            speak(today)

        elif 'open code 3' in query:
            codePath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2024.1.1\\bin\\pycharm64.exe"
            os.startfile(codePath)
            speak('opening pycharm community boss')

