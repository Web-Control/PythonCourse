# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 07:14:34 2021

@author: schomej
"""

#Some card game

rules = "Abc"

while(True):
    #Player 1 name
    player1 = str(input("Player1 please enter your name: "))
    print("Welcome",player1 + "!!!")
    player2 = str(input("Player2 please enter your name: "))
    print("Welcome",player2 + "!!!")
    print(" \n")
    
    whoseTurn = player1
    
    
    print(whoseTurn, "is your turn.")