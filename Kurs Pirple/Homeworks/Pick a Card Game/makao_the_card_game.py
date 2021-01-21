# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 07:14:34 2021

@author: schomej
"""

#Makau The Card Game

from random import shuffle, randint
import os


rules = "Abc"

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def displayTitleBar():
    # Clears the terminal screen, and displays a title bar.
    clearScreen()
    print("\n")
    print("\t    **********************************************")
    print("\t    ***      Macau - THE BEST CARD GAME        ***")
    print("\t    **********************************************")

def createDeck():
    deck = []
    #suits_name = ['Spades', 'Diamonds', 'Hearts', 'Clubs']
    suitsSymbols = ['♠', '♦', '♥', '♣']
    faceValues = ["A","J","Q","K"]
    for i in range(4):#The are 4 diffrent suits
        for card in range(2,11):#Adding number
            deck.append(str(str(card)+suitsSymbols[i]))
            
        for card in faceValues:
            deck.append(card+suitsSymbols[i])
    shuffle(deck)   
    return deck

class Card:
    def __init__(self,card):
        self.face = card
        self.value = self.checkCardValue(card)
        self.penalty = self.isCardPenalty(card)
        self.isFunctional = self.isCardFunctional(card)
        self.function = self.cardFunction(card)
        

    def checkCardValue(self,card):
        value = 0
        
        if card[0] == "A":
            value = 11
        elif card == "K♥" or card == "K♠":
            value = 5
        elif card == "K♦" or card == "K♣" or card[0] == "Q":
            value = 0
        elif  card[0] == "J":
            value = 1
        else:
            if len(card) == 3:#If it is 10
                card = card.strip("♠♦♥♣")
                print(card)
                value = int(card)
            else:
                if int(card[0]) in range(2,11):
                    value = int(card[0])   
        return value

    def isCardPenalty(self,card):
        isPenalty = False
        penaltyValues =[2,3,5]
        for value in penaltyValues:
            if self.checkCardValue(card) == value:
                isPenalty = True
    
        return isPenalty

    def isCardFunctional(self,card):
        isFunctional = False
        functionCards = ["4","J","Q","A"]
        for sign in functionCards:
            if card[0] == sign:
                isFunctional = True
        return isFunctional

    def cardFunction(self,card):
        function = " "
        if card[0] == "4":
            function = "Wait"
        elif card[0] == "J":
            function = "Value Demand"
        elif card[0] == "Q":
            function = "Any Card"
        elif card[0] == "A":
            function = "Suit Demand"
        return function
    
    def checkIfCardCanGoOnTable(self,cardsOnTable):
        isCardOk = False
        card = self.face
        cardLen = len(card)
        cardOnTop = cardsOnTable[-1].face
        cardOnTopLen = len(cardOnTop)
        
        if self.penalty:
            print("")
        else:
            if card[0] == "Q":#Quin on everything, everything on Quin
                isCardOk = True
            else:
                if cardLen == 2 and cardOnTopLen == 2:
                    if card[0] == cardOnTop[0] or card[1] == cardOnTop[1]:#Check if value or suit are the same
                        isCardOk = True
                elif cardLen == 3 and cardOnTopLen == 3:#10 on table and player also want to put 10 
                   isCardOk = True
                elif  cardLen == 3 and cardOnTopLen == 2:#Some card on table and player want to put 10 card with this same suit
                    if card[2] == cardOnTop[1]:
                        isCardOk = True
                elif cardLen == 2 and cardOnTopLen == 3:#10 on table and player want to put card with this same suit
                    if card[1] == cardOnTop[2]:
                        isCardOk = True
        return isCardOk 

class Player:
    def __init__(self, playerName,deck):
        self.name = playerName
        self.cardsOnHand = self.cardsForPlayer(deck)
         
    def cardsForPlayer(self,deck):
        cards = []
        for i in range(5):
            deckLength = len(deck) - 1
            randomNumber = randint(0,deckLength)
            randomCard = deck[randomNumber]
            CardToGo = Card(randomCard) 
            cards.append(CardToGo)
            deck.pop(randomNumber)
        return cards
    
    def showCards(self):
        for card in self.cardsOnHand:
            print(str(card.face), end=" ")
    


cardDeck = createDeck()
cardsOnTable = []
penaltyCardsOnTable = []
message = " "

print(cardDeck)

#Lets Play :)

#Main loop
while(True):
    
    displayTitleBar()
    
    #Get players names
    playerOneName = str(input("Player1 please enter your name:\nEnter 'x' for exit.\n"))
    if playerOneName == "x":
        break
    
    playerTwoName = str(input("Player2 please enter your name:\nEnter 'x' for exit.\n"))
    if playerTwoName == "x":
        break
    
    #Pick first card on table loop
    FirstCard = ""
    while(True):
        randomNumber = randint(0,len(cardDeck) -1)
        randomCard = cardDeck[randomNumber]
        FirstCard = Card(randomCard)
        if FirstCard.penalty == True or FirstCard.isFunctional == True:
            continue
        else:
            cardsOnTable.append(FirstCard)
            cardDeck.pop(randomNumber)
            break
   
    Player1 = Player(playerOneName,cardDeck)
    Player2 = Player(playerTwoName,cardDeck)
    
    
    actualPlayer = Player1
    #Actual play loop
    while(True):
        displayTitleBar()
        print("\n")
        print(actualPlayer.name , "is your turn.")
        print("Your cards: ")
        actualPlayer.showCards()
        print("\n")
        print("Card on table: " + str(cardsOnTable[-1].face))
        
        if message != " ":
            print("\n")
            print("IMPORTANT !!! - "+message)
            message = " "
        
        try:
            cardToPutNumber = int(input("Chose your card number or take card from the deck by entered '0': "))
        except  ValueError:
            message = "Wrong type of data. Please try again."
            continue
        
        #Check if entered number is not out of the range 
        if cardToPutNumber > len(actualPlayer.cardsOnHand) or cardToPutNumber < 0:
            message = "Card number out of range. Please enter proper number"
            continue
        
        #Player take card from the deck
        if cardToPutNumber == 0:
            randomNumber = randint(0, len(cardDeck)-1)
            randomCard = cardDeck[randomNumber]
            randomCard = Card(randomCard)
            actualPlayer.cardsOnHand.append(randomCard)
            cardDeck.pop(randomNumber)
            if actualPlayer == Player1:
                actualPlayer = Player2
            else:
                actualPlayer = Player1    
        #Card go on table   
        else:
            cardToPut = actualPlayer.cardsOnHand[cardToPutNumber-1]
            
            if  cardToPut.checkIfCardCanGoOnTable(cardsOnTable):
                cardsOnTable.append(cardToPut)
                actualPlayer.cardsOnHand.pop(cardToPutNumber-1)
                
                #Check if player win
                if len(actualPlayer.cardsOnHand) == 0:
                    print("\n")
                    print(actualPlayer.name + " WON THE GAME !!!")
                    break
                #Player changing       
                if actualPlayer == Player1:
                    actualPlayer = Player2
                else:
                    actualPlayer = Player1    
            else:
                message = "You can not put this card !!!"
                continue
                                                              
        
        
        
        
        
        
