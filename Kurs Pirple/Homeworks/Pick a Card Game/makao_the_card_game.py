# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 07:14:34 2021

@author: schomej
"""

#Makau The Card Game

from random import shuffle, randint

rules = "Abc"

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

def checkCardValue(card):
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

def checkIfCardCanGoOnTable(card,cardsOnTable):
    
    isCardOk = False
    
    cardLen = len(card)
    cardOnTop = cardsOnTable[-1]
    cardOnTopLen = len(cardOnTop)
    
    if cardLen == 2 and cardOnTopLen == 2:
        if card[0] == cardOnTop[0] or card[1] == cardOnTop[1]:#Check if value or suit are the same
            isCardOk = True
    elif cardLen == 3 and cardOnTopLen == 3:#10 on table and player also want to put 10 
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
            cardNumber = randint(0,deckLength)
            cards.append(deck[cardNumber])
            deck.pop(cardNumber)
        return cards



cardDeck = createDeck()
cardsOnTable = []
message = " "

print(cardDeck)

while(True):
    
    #Get players names
    playerOneName = str(input("Player1 please enter your name: "))
    playerTwoName = str(input("Player2 please enter your name: "))
  
    Player1 = Player(playerOneName,cardDeck)
    Player2 = Player(playerTwoName,cardDeck)
    
    #First card on table
    firstCard = randint(0,len(cardDeck) -1)
    cardsOnTable.append(cardDeck[firstCard])
    cardDeck.pop(firstCard)
    
    actualPlayer = Player1.name
    
    while(True):
         
        print(actualPlayer, "is your turn.")
        print("Your cards: " + str(Player1.cardsOnHand))
        
        print("\n")
        print("Card on table: " + str(cardsOnTable[-1]))
        
        if message != " ":
            print(message)
            message = " "
        
        
        cardToPutNumber = int(input("Chose your card number: "))
        
        cardToPut = Player1.cardsOnHand[cardToPutNumber-1]
        
        isCardOk = checkIfCardCanGoOnTable(cardToPut,cardsOnTable)
        
        if isCardOk:
            cardsOnTable.append(cardToPut)
            Player1.cardsOnHand.pop(cardToPutNumber-1)
            
        else:
            message = "You can not put this card !!!"
            continue
            
        
        
        
        
        
        
        
