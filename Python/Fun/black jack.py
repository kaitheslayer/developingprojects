import random
import os 
import datetime


# Functions to utilise

def randomcard ():
  "Generate a random card"
  ctouse = random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
  stouse = random.choice(['♥', '♠', '♣', '♦'])
  global rcard1 
  global rcard2 
  global rcard1t 
  global rcard2t 
  global rcard1s
  global rcard2s
  
  rcard1 = ctouse
  rcard1s = stouse
  
  ctouse = random.choice(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'])
  stouse = random.choice(['♥', '♠', '♣', '♦'])
  rcard2 = ctouse
  rcard2s = stouse
  
  return 
  

def printer (tprint):
  print(*tprint, sep='\n')
  return

def imgcard (card1, card2, card1s, card2s):
  print (" .---------. .---------.")
  print (" |    " + card1s + "    | |    " + card2s + "    | ")
  print (" |         | |         |")
  print (" |    " + card1 + "    | |    " + card2 + "    |")
  print (" |         | |         |")
  print (" |    " + card1s + "    | |    " + card2s + "    | ")
  print (" `---------' `---------' \n")
  return
  
  

print ("\033[1;37;40m .-------. ______ _       ___  _____  _   __    ___  ___  _____  _   __ .-------.")
print ("\033[1;37;40m | J --. | | ___ \ |     / _ \/  __ \| | / /   |_  |/ _ \/  __ \| | / / | J --. |")
print ("\033[1;37;40m |   ♠   | | |_/ / |    / /_\ \ /  \/| |/ /      | / /_\ \ /  \/| |/ /  |   ♠   |")
print ("\033[1;37;40m |   ♠   | | ___ \ |    |  _  | |    |    \      | |  _  | |    |    \  |   ♠   |")
print ("\033[1;37;40m | '-- J | | |_/ / |____| | | | \__/\| |\  \ /\__/ / | | | \__/\| |\  \ | '-- J |")
print ("\033[1;37;40m `-------' \____/\_____/\_| |_/\____/\_| \_/ \____/\_| |_/\____/\_| \_/ `-------'\n")



print ("         .---------.                                     .---------.     ")
print ("         |    ♠    |____                                 |    ♠    |____ ")
print ("         |         |♠  /           CREATED BY:           |         |♠  / ")
print ("         |    J    |  /                                  |    J    |  /  ")
print ("         |         | /            kaitheslayer           |         | /   ")
print ("         |    ♠    |/              Fried-Liver           |    ♠    |/    ")
print ("         `---------'                                     `---------'      \n")



actg = input ("                            Press 'Enter' key to play:")

printer ([''])
printer (['Loading...', ''])
printer (['...................................................................................................'])
plname = input("\033[1;37;40m What's your name:")
printer (["Welcome " + plname + " Do you know how to play blackjack / 21? "])
yn = input("\033[1;37;40m Y/N:").lower()

if yn == ("n"):
  printer (["Here are the rules:", "http://www.bicyclecards.com/how-to-play/blackjack/"])


elif yn == ("y"):
    printer (["Dealer ", "Shuffling cards... ", "Your cards are " ])
    randomcard ()
    imgcard(card1=rcard1, card2=rcard2, card1s=rcard1s, card2s=rcard2s)
