import pyttsx3

def say(s):
    engine.say(s)
    engine.runAndWait()

def stop():
    engine.stop()

    
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
