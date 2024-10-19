import pyttsx3
def ts(text):
    try:
        engine = pyttsx3.init()
        engine.setProperty('rate', 150)
        engine.setProperty('volume', 1)
        engine.say(text)
        engine.runAndWait()
    except:
        pass
