import json
import os, sys
import random

def load_words():
    try:
        filename = os.path.dirname(sys.argv[0])+"/"+"words/words.json"

        print (filename)

        with open(filename,"r") as english_dictionary:
            valid_words = json.load(english_dictionary)
            return valid_words
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    ew = load_words()
    # demo print



passw = []
wordlen = 0

while wordlen < 4:
    passw.append(random.choice(ew.keys()))
    wordlen+= 1


print (passw[0] + " " + passw[1] + " " + passw[2] + " " + passw[3])
