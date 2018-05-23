import pyttsx3
import random

voicel = []
engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
   voicel.append(voice.id)

vid = random.choice(voicel)
engine.setProperty('voice', vid)
engine.say('Welcome to the Cedar House tuckshop, how may we help you.')
engine.runAndWait()
