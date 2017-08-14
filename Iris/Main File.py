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
        'divide': 'divide(ine)',
        'power': 'po(ine)',
        'minus': 'minus(ine)',
        'weather': 'weather(ine)'
    }[x]


def speak(x):
    wincl.Dispatch("SAPI.SpVoice").Speak(x)

def output (group, mode, x):
    # Group 1 = Mathematical Answer, Group 2 = String Ouput
    if mode == 0:
        if group == 1:
            answer(x)
            speak ("The answer is " + str(x))
        if group == 2:
            speak (x)


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
    output(1, 0, a)

def e(x):
    exec(x)


def add(x):
    t = 0
    c = re.findall(r'\b\d+\b', x)
    for _ in c:
        t = float(_) + t
    print (t)
    output(1, 0, t)


def multiply(x):
    t = 1
    c = re.findall(r'\b\d+\b', x)
    for _ in c:
        t = float(_) * t
    print (t)
    output(1, 0, t)


def divide(x):
    c = re.findall(r'\b\d+\b', x)
    p = c[0]
    del(c[0])
    for _ in c:
        p = float(p) / float(_)
    output(1, 0, p)


def po(x):
    t = 1
    c = re.findall(r'\b\d+\b', x)
    t = float(c[0]) ** float(c[1])
    output(1, 0, t)


def weather(lc):
    b = re.findall(r'(?<!\.\s)\b[A-Z][a-z]*\b', lc)
    owm = pyowm.OWM('ae0bcff60dfaaa49d582c81a517da9c0')
    location = ' '.join(b)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    b = "It is currently %s  With a temperature of %s °C \n a max of %s °C  and a min of %s °C " % ( w.get_status(), w.get_temperature(unit='celsius')['temp'], w.get_temperature(unit='celsius')['temp_max'],
    w.get_temperature(unit='celsius')['temp_min'])
    output(2, 0, b)








ine = "what is the weather in London"
words = ['add', 'subtract', 'divide', 'minus', 'multiply', 'weather', 'how are you', 'weather', 'power', 'answer to universe']
word_exp = '|'.join(words)
inputi = re.findall(word_exp, ine, re.M)




output = e(tr(inputi[0]))




