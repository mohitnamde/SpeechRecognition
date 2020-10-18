import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        print("speak_now...")
        audio = r.listen(source)
        print("Done: voice detected.")

    try:
        print("Recognizing: Converting your voice into text.")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: , {query}\n")

    except Exception as e:
        speak("Say that again please...")
        print(e)
        return "None"
    return query


if __name__ == "__main__":
    speak("Vision is here.")
    while True:
        query = takeCommand().lower()