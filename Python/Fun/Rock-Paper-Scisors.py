
# game counter
utotal = 0
ctotal = 0

# beginning of loop
restart=1

while restart!="x":

    import random

# 1 in 24 chance (4,17%)of computer choosing 'gun' and instant gameover
    hsign = ['rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'rock', 'paper', 'scissors', 'gun']
    coh = random.choice(hsign)

    plh = input("ROCK, PAPER, SCISSORS(r, p, s)")

    # Variations of Game, if coh == ("rock")
    if coh == ("rock"):
        if plh == ("s"):
            print ("Computer chose rock")
            print ("Computer Wins!")
            ctotal = ctotal +1
            print ()

    if coh == ("rock"):
            if plh == ("p"):
                print ("Computer chose rock")
                print ("YOU WIN!")
                utotal = utotal + 1
                print ()

    if coh == ("rock"):
            if plh == ("r"):
                print ("Computer chose rock")
                print ("It's a Draw.")
                print ()



    # Variations of Game, if coh == ("paper")
    if coh == ("paper"):
            if plh == ("p"):
                print ("Computer chose paper")
                print ("It's a Draw.")
                print ()

    if coh == ("paper"):
            if plh == ("r"):
                print ("Computer chose paper")
                print ("Computer Wins!")
                ctotal = ctotal +1
                print ()

    if coh == ("paper"):
            if plh == ("s"):
                print ("Computer chose paper")
                print ("YOU WIN!")
                utotal = utotal + 1
                print ()



    # Variations of Game, if coh == ("scissors")
    if coh == ("scissors"):
            if plh == ("s"):
                print ("Computer chose scissors")
                print ("It's a Draw.")
                print ()

    if coh == ("scissors"):
            if plh == ("r"):
                print ("Computer chose scissors")
                print ("YOU WIN!")
                utotal = utotal + 1
                print ()

    if coh == ("scissors"):
            if plh == ("p"):
                print ("Computer chose scissors")
                print ("Computer Wins!")
                ctotal = ctotal +1
                print ()

    if coh == ("gun"):
                print ("COMPUTER CHOSE GUN")
                print ("COMPUTER DOMINATES!")
                print ("YOU LOSE")
                print ("GAME OVER")
                ctotal = ctotal +1
                print ()

# if you start beating the computer by 5 points, the next round you play, computer WILL win and give itself +5 points
    if ctotal == utotal - 5:
        print ("NOW I WILL END YOU!")
        plh = input("ROCK, PAPER, SCISSORS(r, p, s)")
        if plh == ("r"):
            print ("COMPUTER WINS!")
            print ("COMPUTER WINS!")
            print ("COMPUTER WINS!")
            ctotal = ctotal + 5

    if ctotal == utotal - 5:
        print ("NOW I WILL END YOU!")
        plh = input("ROCK, PAPER, SCISSORS(r, p, s)")
        if plh == ("p"):
            print ("COMPUTER WINS!")
            print ("COMPUTER WINS!")
            print ("COMPUTER WINS!")
            ctotal = ctotal + 5

    if ctotal == utotal - 5:
        print ("NOW I WILL END YOU!")
        plh = input("ROCK, PAPER, SCISSORS(r, p, s)")
        if plh == ("s"):
            print ("COMPUTER WINS!")
            print ("COMPUTER WINS!")
            print ("COMPUTER WINS!")
            ctotal = ctotal + 5


# when the computer is ahead by 2 points, it will start to taunt
    if ctotal == utotal + 2:
        import random
        taunt = ['DESTROYED', 'GIVE UP NOW, PETTY HUMAN', 'OH WHATS THAT, I WON AGAIN', 'UNSTOPPABLE', 'MY CODE IS OMNIPOTENT']
        cht = random.choice(taunt)
        print ("%s" %cht)

# when you are ahead by 3 points, computer will print ("NOT BAD, HUMAN, NOT BAD AT ALL")
    if ctotal == utotal - 3:
        print ("NOT BAD, HUMAN, NOT BAD AT ALL")

# display of score counter
    print ("YOU:" + str(utotal) + " vs COMPUTER:" + str(ctotal))


# End of loop
input("press any key to start again, or x to exit.")
