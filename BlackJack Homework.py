import random
import os

playingcards = None

suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']

def issueCards():
    cardsdict = dict()
    for suit in suits:
        for i in range(1, 14):
            cardsdict[suit+str(i)] = [int(i), suit]
    return cardsdict

playerhand = []
dealerhand = []

def resetHands():
    global playerhand
    global dealerhand
    playerhand = []
    dealerhand = []

def dealHand(hand): #list
    suitchoice = random.choice([randomcard for randomcard in playingcards.keys()])
    hand.append(playingcards[suitchoice])
    del playingcards[suitchoice]

def displayHand(hand, indication):
    counter = 0
    if indication == "show":
        for i in hand:
            print(i)
    elif indication == "hide":
        for i in hand:
            if counter == 1:
                print("Hidden")
            else:
                print(i)
                counter += 1

def handsandOptions():
    print("Player's Hand:")
    displayHand(playerhand, "show")
    print(" ")
    print("Dealer's Hand:")
    displayHand(dealerhand, "hide")
    print(" ")

def handsandOptions2():
    print("Player's Hand:")
    displayHand(playerhand, "show")
    print(" ")
    print("Dealer's Hand:")
    displayHand(dealerhand, "show")
    print(" ")

def collectData():
    playersum = 0
    dealersum = 0
    for i in playerhand:
        playersum += i[0]
    for i in dealerhand:
        dealersum += i[0]
    return playersum, dealersum
        
def playerFunction():
    os.system('cls')
    print("Player's Turn" + '\n')
    handsandOptions()
    print("1. Hit")
    print("2. Stand")
    print("Enter below")
    choice = int(input())
    if choice == 1:
        dealHand(playerhand)
        os.system('cls')
        print("Player's Turn" + '\n')
        handsandOptions()
        print("Player has decided to hit!")
        continuing3 = input("Press Enter to continue.")
        return None, None
    elif choice == 2:
        print("Player has decided to stand!")
        continuing3 = input("Press Enter to continue.")
        return "stand", "Player"

def dealerMoves(hand):
    os.system('cls')
    print("Dealer's Turn" + '\n')
    handsandOptions()
    print("The Dealer is viewing their hand......")
    continuing2 = input("Press Enter to Continue")
    handsum = 0 #handsome lol
    for i in hand:
        handsum += i[0]
        if handsum < 24:
            dealHand(dealerhand)
            os.system('cls')
            print("Dealer's Turn" + '\n')
            handsandOptions()
            print("The Dealer has decided to Hit!")
            continuing2 = input("Press Enter to Continue")
            return None, None
        elif handsum > 24:
            print("The Dealer has decided Stand!")
            continuing2 = input("Press Enter to Continue")
            return 'stand', 'Dealer'
        
def bustCatch(person, sum):
    print(f"The {person}'s hand has Bust.")
    print(f"{person}'s hand equals to {sum}.")
    print(f"The {person} loses.")

def playAgain():
    global OnOffGame
    global method
    global playingcards
    global turn
    choice = input("Play again? (Y)es or (N)o) Enter the letter of either choice: ")
    choice = choice.lower()
    if choice == "n":
        OnOffGame = False
    elif choice == 'y':
        method = 'deal'
        playingcards = {}
        turn = 'player'
        resetHands()
        
stand = None
standplayer = None

OnOffGame = True
method = 'deal'
turn = 'player'
while OnOffGame:
    #player
    if turn == 'player':
        os.system('cls')
        if method == 'deal':
            playingcards = issueCards()
            dealHand(playerhand)
            dealHand(dealerhand)
            dealHand(playerhand)
            dealHand(dealerhand)
            method = 'play'
        stand, standplayer = playerFunction()
        turn = 'dealer'
    elif turn == 'dealer':
        stand, standplayer = dealerMoves(dealerhand)
        turn = 'player'

    playersum, dealersum = collectData()

    #bust
    if playersum > 30:
        bustCatch("Player", playersum)
        playAgain()
    elif dealersum > 30:
        bustCatch("Dealer", dealersum)
        playAgain()

    #stand
    if stand and standplayer:
        os.system('cls')
        handsandOptions2()
        print('\n')
        print(f"User Score: {playersum}")
        print(f"Dealer Score: {dealersum}")
        if playersum > dealersum:
            print('User has won!')
        else:
            print('Dealer has won!')
        playAgain()

# CODE THAT DID NOT MAKE THE FINAL CUT:

       
#OnOffGame = False
        
# class BlackJack:
#     def __init__(self):
#         playerhand = []
#         dealerhand = []
#     def playerHandDeal(self):
#         suitchoice = random.choice([randomcard for randomcard in playingcards.keys()])
#         if playingcards[suitchoice] not in self.dealerhand and playingcards[suitchoice] not in self.playerhand:
#             self.playerhand.append(playingcards[suitchoice])

#     def dealerHandDeal(self):
#         suitchoice = random.choice([randomcard for randomcard in playingcards.keys()])
#         if playingcards[suitchoice] not in self.dealerhand and playingcards[suitchoice] not in self.playerhand:
#             self.dealerhand.append(playingcards[suitchoice])

#     def getSums(self):
#         playersum = 0
#         dealersum = 0
#         for i in self.playerhand:
#             playersum += i[0]
#         for v in self.dealerhand:
#             dealersum += v[0]
#         return [playersum, dealersum]
    
#     def gameStand(self):
#         results = self.getSums()
#         print(f'Your score is {results[0]}')
#         print(f"The Dealer's score is {results[1]}")
#         if results[0] > results[1]:
#             print("You've won the game!")
#         elif results[1] > results[0]:
#             print("The Dealer has won the game.")
#         else:
#             print("This was a draw!")

#     def dealermove(self):
#         dealersum = 0
#         for v in self.dealerhand:
#             dealersum += v[0]
#         if dealersum <= 24:
#             os.system('cls')
#             print("The Dealer has decided to take a hit!")
#             suitchoice = random.choice([randomcard for randomcard in playingcards.keys()])
#             if playingcards[suitchoice] not in self.dealerhand and playingcards[suitchoice] not in self.playerhand:
#                 self.dealerhand.append(playingcards[suitchoice])
#         elif dealersum > 24:
#             print("The Dealer has decided to stand!")
#             self.gameStand()
        