import pyttsx3
import speech_recognition as sr

r = sr.Recognizer()
def speak (text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def listen():
    num_tries= 3
    while num_tries:
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)

        try:
            response=  r.recognize_google(audio)
            print('done and sent!')
            return response
        except Exception:
            speak(' i did not get that')
            num_tries -=1
            return listen()


