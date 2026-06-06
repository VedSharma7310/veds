import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
print(voices)

engine.say("Hello Ved")
engine.runAndWait()