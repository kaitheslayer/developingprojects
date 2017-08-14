import re
import win32com.client as wincl
import pyowm
import math

ans = ''
preans = ''

def tr(x):
    return {
        'how are you': 'speak("I do not feel emotions.")',
        'add': 'add(ine)',
        'multiply': 'multiply(ine)',
        'divide': 'division(ine)',
        'power': 'po(ine)',
        'minus': 'minus(ine)'
    }[x]


def speak(x):
    wincl.Dispatch("SAPI.SpVoice").Speak(x)


def answer(x):
    global ans
    global preans
    preans = ans
    ans = x

def minus(v):
    v = re.findall(r'\b\d+\b', v)
    t = 0
    c = []
    for _ in v:
        c.append(float(_))
    y = len(c)
    a = c[0] - sum(c[1:y])
    answer(a)
    speak("The answer is " + str(a))



def e(x):
    exec(x)

def add(x):
    t = 0
    c = re.findall(r'\b\d+\b', x)
    for _ in c:
        t = float(_) + t
    print (t)
    answer (t)
    speak ("The answer is " + str(t))



def multiply(x):
    t = 1
    c = re.findall(r'\b\d+\b', x)
    for _ in c:
        t = float(_) * t
    print (t)
    answer (t)
    speak("The answer is " + str(t))


def division(x):
    t = 1
    c = re.findall(r'\b\d+\b', x)
    t = float(c[0]) / float(c[1])
    print (t)
    answer (t)
    speak("The answer is " + str(t))


def po(x):
    t = 1
    c = re.findall(r'\b\d+\b', x)
    t = float(c[0]) ** float(c[1])
    print (t)
    answer (t)
    speak("The answer is " + str(t))

def weather (lc):
    owm = pyowm.OWM('ae0bcff60dfaaa49d582c81a517da9c0')
    location = ' '.join(lc)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    b = "Weather details: \n Status: %s \n Current Temp: %s °C \n Max Temp: %s °C \n Min Temp: %s °C " % ( w.get_status(), w.get_temperature(unit='celsius')['temp'], w.get_temperature(unit='celsius')['temp_max'],
    w.get_temperature(unit='celsius')['temp_min'])
    answer(b)
    speak(b)








ine = "hey machine 32 minus 21 minus"
words = ['add', 'subtract', 'divide', 'minus', 'multiply', 'weather', 'how are you', 'weather', 'power', 'answer to universe']
word_exp = '|'.join(words)
inputi = re.findall(word_exp, ine, re.M)




output = e(tr(inputi[0]))




