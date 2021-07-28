import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import smtplib
import webbrowser
import os
import cv2
from requests import get
import pywhatkit as kit
import sys


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        
        audio = r.listen(source)

    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:{query}\n")

    except Exception as e:
        # print(e)        
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('tanujyaduvanshi1996@gmail.com', 'Y19121996')
    server.sendmail('tanujyaduvanshi1996@gmail.com', to, content)
    server.close()
    

if __name__ == "__main__":
    speak("Hello Trilok")
    wishMe()
    while True:
     query = takeCommand().lower()

     if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        speak(results)

     elif 'open youtube' in query:
        webbrowser.open("youtube.com")

     elif 'open google' in query:
        speak("sir, what should i search on google")
        cm = takeCommand().lower()
        webbrowser.open(f"{cm}")  
  

     elif 'play music' in query:
        music_dir = 'D:\\songs'
        songs = os.listdir(music_dir)
        
        os.startfile(os.path.join(music_dir,songs[0]))

     elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is {strTime}")

     elif 'open code' in query:
        codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codePath)

     elif 'open notepad' in query:
        codePath = "C:\\Windows\\system32\\notepad.exe"
        os.startfile(codePath)

     elif 'open command prompt' in query:
         os.system('start cmd')

     elif 'send message' in query:
        kit.sendwhatmsg("+917015750852", "Hello brother",13,52)

     elif 'play songs on youtube' in query:
        kit.playonyt("see you again")

     elif 'open camera' in query:
        cap = cv2.VideoCapture(0)
        while True:
            ret, img = cap.read()
            cv2.imshow('webcam', img)
            k = cv2.waitKey(50)
            if k==27:
                break
        cap.release()
        cv2.destroyAllWindows()

     elif 'ip address' in query:
        ip = get('https://api.ipify.org').text
        speak(f"your IP address is {ip}")

     elif 'email to tanuj' in query:
      try:
        speak("What should I say?")
        content = takeCommand().lower()
        to = "yaduvanshitrilok@gmail.com"
        sendEmail(to, content)
        speak("Email has been sent!")
      except Exception as e:
        print(e)
        speak("Sorry my friend Trilok. I am not able to send this email")

     elif 'quit' in query:
        speak("Thanks for using me sir, have a good day.")
        sys.exit()

        



