from platform import uname
import subprocess
from wikipedia.wikipedia import search
import wolframalpha
import pyttsx3
import tkinter
import json, requests
import winshell
import shutil
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyautogui
import psutil
import pyjokes
import os.path



engine = pyttsx3.init('sapi5')

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak('this is friday')


def time():
    Time = datetime.datetime.now().strftime("%H:%M:%S")
    speak(Time)


def date():
    tday = datetime.datetime.today().strftime("%B %d, %Y")
    speak(tday)


def wishme():
    speak('Welcome back sir, ')

    hour = datetime.datetime.now().hour

    if hour >= 6 and hour <= 12:
        speak('Good Morning')
    elif hour >= 12 and hour <= 18:
        speak('Good Afternoon')
    elif hour >= 18 and hour <= 24:
        speak('Good Evening')
    else:
        speak('Good Night')

    speak('Friday at your service! How can I help you')


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en=in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Sorry i didn't catch that...")
        speak('Say that again please')
        print("Error : " + str(e))
        return input("Can't get it . Type here:\n")
    
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('rahul1316154@gmail.com', 'iloveyouvedanti')
    server.sendmail('rahul1316154@gmail.com', to, content)
    server.close()

def cpu():
    usage = str(psutil.cpu_percent())
    speak("the CPU is at" + usage)

    battery = psutil.sensors_battery()
    speak("battery is at ")

    speak(battery.percent)

def username():
    speak("What should i call you sir")
    uname = takeCommand()
    speak("hello mister" + uname)
    columns = shutil.get_terminal_size().columns
     
    print("#####################".center(columns))
    print("Welcome Mr.", uname.center(columns))
    print("#####################".center(columns))
     
    speak("How can i Help you, Sir")


if __name__ == "__main__":
    clear = lambda: os.system('cls')
     
    clear()
    
    while True:
        query = takeCommand().lower()
        print(query)


        ## opening some apps and also in browser
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            


        elif 'open youtube' in query:
            print("working")
            speak("Here you go to Youtube\n")
            webbrowser.open('http://www.youtube.com')
            quit() 

        elif 'send a mail' in query or 'send email' in query:
            try: 
                speak("What should I say")
                content = takeCommand()
                speak("whom I should send the mail")
                to = input()
                sendEmail(to,content)
                speak("the mail has sent successfully")
            except Exception as e:
                print(e)
                speak("I am unable to send the mail")

        elif 'search in web' in query or 'searching web' in query:
            speak('What should I search')
            path = "C:\Program Files\Mozilla Firefox\firefox.exe %s"
            search = takeCommand().lower()
            webbrowser.get('C:\Program Files\Mozilla Firefox\firefox.exe').open(search + ".com")
        
        
        elif 'open google' in query:
            speak("Here you go to Google\n")
            webbrowser.open("https://www.google.com/")
            quit() 

        elif 'open stackoverflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("https://stackoverflow.com/") 
            quit() 

        elif 'play songs' in query or 'open spotify' in query:
            speak("opening spotifi")
            os.startfile("spotify")
            quit()

        elif ' open powerpoint presentation' in query or 'open powerpoint' in query:
            speak("opening Power Point presentation")
            power = r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.exe"
            os.startfile(power)
            quit()

        elif 'open lightroom' in query:
            speak("opening adobe lightroom")
            lr = r"D:\Adobe\Software\Adobe Lightroom Classic CC\Lightroom.exe"
            os.startfile(lr)
            quit()

        elif 'open photoshop' in query:
            speak("opening adobe photoshop")
            ps = r"D:\Adobe\Software\Adobe Photoshop 2020\photoshop.exe"
            os.startfile(ps)
            quit()

        elif 'open premiere pro' in query:
            speak("opening adobe premiere pro")
            pp = r"D:\Adobe\Software\Adobe Premiere Pro 2020\Adobe Premiere Pro.exe"
            os.startfile(pp)
            quit()

        elif 'open notepad' in query:
            speak("opemimg notepad")
            np = r"C:\WINDOWS\system32\notepad.exe"
            os.startfile(np)
            quit()

        elif 'wifi speed' in query or  'wi-fi speed' in query:
            speak("testing")
            webbrowser.open("https://fast.com/") 
            quit()

        elif 'open whatsapp' in query:
            speak("due to some security reasons I am unable to open whatsapp")
            

        ## remainder function
        
        elif "write a note" in query:
            speak("What should i write sir")
            note = takeCommand()
            speak("shall i make a new file or do it in the default file")
            option = takeCommand()

            if 'new' in option:
                inputFileName = input("Enter name of input file: ") 
                inputFile = open(inputFileName, "w")
            else:
                file = open('defualt_notepad.txt', 'w')

            
            speak("Sir, Should i include date and time")
            snfm = takeCommand()

            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.today().strftime("%m/%d/%Y, %H:%M:%S")
                inputFile.write(strTime)
                inputFile.write(" :- \n")
                inputFile.write(note)

            elif None in snfm or 'no' in snfm:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes/n")
            speak("what note should I open")
            opty = input("Enter name of input file: ") 
            if os.path.isdir(opty):
                file = open(opty, "r")
                print(file.read())
                speak(file.read(6))
            else:
                speak("opening default note")
                filepo = open("default_notepad.txt", "r")
                print(filepo.read())
                speak(filepo.read(6))
            
        
        
        elif 'remember me' in query or 'remember that' in query or 'remainder' in query or 'remind me' in query:
            speak("what should I remggember?")
            data = takeCommand()
            speak("you sid to remember " + data)
            remember = open("remembertxt.txt", "a")
            
            if remember != None:
                remember.write("\n")
            remember.write(data)
            remember.close()

        elif 'any reminders' in query:
            remember = open("remembertxt.txt", "r")
            kp = remember.read()
            print(kp)
            speak("you said to remember that " + kp)

        
        ##some system functions
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')

        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])

        elif "logout" in query:
            speak("Make sure all the application are closed before sign-out")
            subprocess.call(["shutdown", "/l"])
        
        elif 'take a screenshot' in query:
            img = pyautogui.screenshot()
            now = datetime.datetime.now()
            name = now.strftime("%Y_%m_%d_%H_%M_%S")

            img.save(r'C:\Users\rahul\Pictures\ss_by_assistant\name_{}.png'.format(name))
            speak("done")

            os.startfile(r'C:\Users\rahul\Pictures\ss_by_assistant')  

        elif 'cpu' in query:
            cpu()
            
        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        ## some cool conversations
        elif 'joke' in query:
            speak(pyjokes.get_jokes())
        
        elif "hi there" in query:
            wishme()


        ## naming conversation
        elif 'start naming'in query:
            username()
            
        elif 'change my name' in query:
            speak("Got it! What should I call you ")
            new_name = takeCommand()
            uname = new_name
            print(uname)
            speak("your name is " + uname)

        elif "who made you" in query or "who created you" in query:
            speak("I have been created by Rahul.")

        elif 'what is your name' in query:
            speak("my names's personal assistant. I wish that everybody had a cool nickname as mine")


        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query :
            speak("It's good to know that your fine")
        
        elif "i love you" in query:
            speak("Aww thank you but It's hard to understand")
        
        elif "will you be my gf" in query or "will you be my bf" in query:  
            speak("I'm not sure about, may be you should give me some time")
        

        ##date and time including quitting functionss
        elif 'time' in query:
            time()

        elif 'date' in query:
            date()

        elif 'offline'  in query or 'sign out' in query or 'quit' in query or 'gofland' in query:
            quit()
        
        else:
            quit()
