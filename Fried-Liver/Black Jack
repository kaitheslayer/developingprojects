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
  print ("  _________   _________ ")
  print (" |    " + card1s + "    | |    " + card2s + "    | ")
  print (" |         | |         |")
  print (" |    " + card1 + "    | |    " + card2 + "    |")
  print (" |         | |         |")
  print (" |    " + card1s + "    | |    " + card2s + "    | ")
  print ("  ---------   --------- \n")
  return
  
  

print ("\033[1;30;41m ______ _       ___  _____  _   __    ___  ___  _____  _   __")
print ("\033[1;30;41m | ___ \ |     / _ \/  __ \| | / /   |_  |/ _ \/  __ \| | / /")
print ("\033[1;30;41m | |_/ / |    / /_\ \ /  \/| |/ /      | / /_\ \ /  \/| |/ / ")
print ("\033[1;30;41m | ___ \ |    |  _  | |    |    \      | |  _  | |    |    \ ")
print ("\033[1;30;41m | |_/ / |____| | | | \__/\| |\  \ /\__/ / | | | \__/\| |\  \ ")
print ("\033[1;30;41m \____/\_____/\_| |_/\____/\_| \_/ \____/\_| |_/\____/\_| \_/")



print ("\033[1;30;45m  _________                                       __________      ")
print ("\033[1;30;45m |    ♠    |____                                 |    ♠     |____ ")
print ("\033[1;30;45m |         |♠  /                                 |          |♠  / ")
print ("\033[1;30;45m |    J    |  /                                  |    J     |  /  ")
print ("\033[1;30;45m |         | /                                   |          | /   ")
print ("\033[1;30;45m |    ♠    |/                                    |    ♠     |/    ")
print ("\033[1;30;45m  ---------                                       ----------      \n")



actg = input ("\033[1;30;42m Press any key to play:")

printer (['Loading...', ''])

plname = input("What's your name:")
printer (["Welcome " + plname + " Do you know how to play blackjack / 21? "])
yn = input("Y/N:").lower()

if yn == ("n"):
    printer (["Here are the rules:", "", "I am the Dealer and you are a player, your goal is to beat my hand without going over 21"])



elif yn == ("y"):
    printer (["\033[1;30;42m Dealer ", "\033[1;30;42m  Shuffling cards... ", "\033[1;30;42m  Your cards are " ])
    randomcard ()
    imgcard(card1=rcard1, card2=rcard2, card1s=rcard1s, card2s=rcard2s)
   
