import pyttsx3
import pywin32_system32
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui

engine = pyttsx3.init()

def speak(audio) -> None:
    engine.say(audio)
    engine.runAndWait()
    
def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("current time is",Time)
    
def data() -> None:
    day: int = datetime.datetime.now().day
    month: int = datetime.datetime.now().month
    year: int = datetime.datetime.now().year
    speak("current date is")
    speak(day)
    speak(month)
    speak(year)
    print(f"current date is{day}/{month}/{year}")
    
def wishme() -> None:
    print("welcome back sir")
    speak("welcome back sir")
    
    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir")
        print("Good Morning Sir")
    elif 12 <= hour < 17:
        speak("Good Afternoon Sir")
        print("Good Afternoon Sir")
    elif 17 <= hour < 00:
        speak("Good Evening Sir")
        print("Good Evening Sir")
    else:
        speak("Good Night Sir , See you later")
        
    speak ("Friday is here sir , tell me how may i help you")
    print ("Friday is here sir , tell me how may i help you")
    
def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser("~\\Pictures\\ss.png")
    img.save(img_path)
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,languagae = "en-in")
        print(query)
        
    except Exception as e:
        print(e)
        speak("please say that again")
        return "Try Again"
    
    return query

if __name__ == "__main__":
    wishme()
    while True:
        query = takecommand().lower()
        if "time" in query:
            time()
        elif "who are you " in query:
            speak("I'm Friday sir by created by Ashwin and I'm super AI")
            print("I'm Friday sir by created by Ashwin and I'm super AI")
        elif "how are you " in query:
            speak("I'm fine sir , What about you?")
            print("I'm fine sir , What about you?")
        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")
            
        elif "open youtube " in query: ## open for youtube ##
            wb.open("youtube.com")
            
        elif "open google" in query: ## open for google ##
            wb.open("google.com")
            
        elif "open instagram" in query: ## open for instagram ##
            wb.open("instagram.com")
            
        elif "open amity" in query: ## open for amity ##
            wb.open("amizone.net")
            
        elif "open github" in query: ## open for github ## 
            wb.open("github.com")
            
        elif "open linkedin" in query: ## open for linkedin ##
            wb.open("linkedin.com")
            
        elif "open flipkart" in query: ## open for flipkart ##
            wb.open("flipkart.com")
        
        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(chromePath)

        elif "search on chrome" in query: ## serach for chrome command ##
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        elif "remember that" in query:
            speak("What should I remember")
            data = takecommand()
            speak("You said me to remember that" + data)
            print("You said me to remember that " + str(data))
            remember = open("data.txt", "w")
            remember.write(data)
            remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that" + remember.read())
            print("You told me to remember that " + str(remember))
        
        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
            
        elif "offline " in query:
            quit()