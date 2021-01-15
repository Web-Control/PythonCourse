# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 07:20:46 2021

@author: schomej
"""
from random import shuffle

#Blackjack

def createDeck():
    deck = []
    faceValues = ["A","J","Q","K"]
    for i in range(4):#The are 4 diffrent suits
        for card in range(2,11):#Adding number
            deck.append(str(card))
            
        for card in faceValues:
            deck.append(card)
    shuffle(deck)   
    return deck

cardDeck = createDeck()

print(cardDeck)

class Player:
    def __init__(self,playerHand = [],playerMoney = 100):
        self.hand = playerHand
       
        self.score = self.setScore()
        self.money = playerMoney
        self.bet = 0
        
    def __str__(self):
        currentHand = "On hand: "
        for card in self.hand:
            currentHand += str(card) + " "
         
        finalStatus = currentHand + ",Score: " + str(self.score)
        
        return finalStatus
    
    def setScore(self):
        self.score = 0
        faceCardsDict = {"A":11,"J":10,"Q":10,"K":10,
                         "2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
        aceCounter = 0
        
        for card in self.hand:
            self.score += faceCardsDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score
    
    def hit(self,card):
        self.hand.append(card)
        self.score = self.setScore()
        
    def play(self,newHand):
        self.hand = newHand
        self.score = self.setScore()
    
    def betMoney(self,amount):
        self.money -= amount #MOney 100; bet(20)
        self.bet += amount #MOney 100 -> 80 bet 0->20
        
    def win(self,result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2: #Player have Blackjack
                self.money += 2.5*self.bet
            else:
                self.money += 2*self.bet
            self.bet = 0
        else:
            self.bet = 0
    def draw(self):
        self.money += self.bet
        self.bet = 0
    
    def hasBlackJack(self):
        if self.score == 21 and len(self.hand) == 2:
            return True
        else:
            return False
            
            
###################################################
        
def printHouse(House):
    for card in range(len(House.hand)):
        if card == 0:
            print("X", end = " ")
        elif card == len(House.hand) -1:
            print(House.hand[card])
        else:
            print(House.hand[card], end = " ")
####################################################       
cardDeck = createDeck()
firstHand = [cardDeck.pop(),cardDeck.pop()]
secondHand = [cardDeck.pop(),cardDeck.pop()]

Player1 = Player(firstHand)
House = Player(secondHand)
while(True):
    if len(cardDeck) < 20:
        cardDeck = createDeck()
 
    firstHand = [cardDeck.pop(),cardDeck.pop()]
    secondHand = [cardDeck.pop(),cardDeck.pop()]
    
    Player1.play(firstHand)
    House.play(secondHand)
    
    betAmount = int(input("Please enter your bet: "))
    Player1.betMoney(betAmount)
    print(cardDeck)
    printHouse(House)
    print(Player1)
    
    if Player1.hasBlackJack():
        if House.hasBlackJack():
            Player1.draw()
        else:
            Player1.win(True)
    else:
        while(Player1.score < 21):
            action = input("Do you want another card?(y/n): ")
            if action == "y":
                Player1.hit(cardDeck.pop())
                print(Player1)
                printHouse(House)
            else:
                break
           
        while(House.score < 16):
            print(House)
            House.hit(cardDeck.pop())
        if Player1.score > 21:
            if House.score > 21:
                Player1.draw()
                print("Draw")
            else:
                Player1.win(False)
                print("You Loose")
        elif Player1.score > House.score:
            Player1.win(True)
            print("You win !!!")
        elif Player1.score == House.score:
            Player1.draw()
            print("Draw !!!")
        else:
            if House.score > 21:
                Player1.win(True)
                print("You win !!!")
            else:
                Player1.win(False)
                print("You win !!!")
            
            
    print(Player1.money)            
    print(House)
    
        
            