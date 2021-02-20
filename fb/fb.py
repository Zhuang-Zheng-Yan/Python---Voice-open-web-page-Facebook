import speech_recognition as sr
import webbrowser

r =sr.Recognizer()
with sr.Microphone() as source:
    while True:
        audio = r.listen(source)
        print("You said "+r.recognize_google(audio))
        if r.recognize_google(audio)=="Facebook":
            webbrowser.open('https://www.facebook.com')
            break