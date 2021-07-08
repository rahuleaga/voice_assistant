import pyttsx3
import datetime

engine = pyttsx3.init()

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id) #changing index changes voices but ony 0 and 1 are working here

newVoiceRate = 200;
engine.setProperty('rate',newVoiceRate)

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
    speak('Welcome back sir')
    date()
    time()
    speak('Friday at your service')

wishme()