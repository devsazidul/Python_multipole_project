# pip install pyttsx3
# pip install SpeechRecognition
# pip install pyjokes
# pip install datetime
# brew install portaudio
# pip install pyaudio


import pyttsx3 #Text-to-speech (TTS) — অর্থাৎ অ্যাসিস্ট্যান্ট কথা বলবে
import speech_recognition as sr # Microphone থেকে কণ্ঠ শুনে text-এ রূপান্তর করবে
import webbrowser # ওয়েবসাইট খুলতে ব্যবহৃত হয় (Google, YouTube ইত্যাদি)
import datetime # সময় ও তারিখ জানার জন্য
import pyjokes # মজার জোকস শোনাতে
import os # Operationg system এর কাজের জন্য
import time

def sptext():
    recognizer =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("Recognizing...")
            data = recognizer.recognize_google(audio)
            print(data)
            return data
        except sr.UnknownValueError:
            print("Sorry, I did not understand that.")

def speechtx(x):
    engine = pyttsx3.init()
    voices= engine.getProperty('voices')
    engine.setProperty('voice',voices[9].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    engine.runAndWait()
# 9
# only speechtx funtion used korle niche while loop ta run korta hobe. noito off thakbe. -------------
# while True:
#     text =input("Hello, Sir, How can I help you?")

#     if text.lower() =="exit()":
#         speechtx("Goodbye, Sir")
#         break

    #speechtx(text)

if __name__ == "__main__":

    # if sptext().lower() == "hay Sazidul":
    while True:
        data1=sptext().lower()
        if "tell me your name" in data1:
             name = "My name is Sazidul islam"
             speechtx(name)
        elif "tell me your age" in data1:
             age = "I am 22 years old"
             speechtx(age)
        elif "who are you" in data1:
            person="I am your personal assistant, Sazidul islam"
            speechtx(person)
        elif "now time" in data1:
            time =datetime.datetime.now().strftime("%H:%M:%S")
            speechtx(f"Current time is {time}")
            print(time)
        elif "open youtube" in data1:
            youtube = "https://www.youtube.com/"
            webbrowser.open(youtube)
        elif "joke" in data1:
            joke_1=pyjokes.get_joke(language='en', category='neutral')
            speechtx(joke_1)
            print(joke_1)
        elif "play music" in data1:
            add ="D:\gaurav\music"
            listsongs= os.listdir(add)
            print(listsongs)
            os.startfile(os.path.join(add,listsongs[0]))
        elif "exit" in data1:
            speechtx("Goodbye, Sir")
            break
            time.sleep(5)
    else:
        print("Thank you")
    # else: 
    #     print("Thank")