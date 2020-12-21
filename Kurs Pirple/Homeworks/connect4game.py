# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 08:05:10 2020

@author: schomej
"""

def drawBoard():
    for row in range(6):
        for column in range(12):
            if column %2 != 0:
                if column != 11:
                    print(" |", end="")
                else:
                    print(" |")
        if row < 5:       
            print("--------------")

field = [[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "],[" "," "," "," "," "," "]]

def checkIfWon():
    winner = " "
    #Checking if somebody won in a column
    for column in field:
        for i in range(3):#Only 3 position of 4 element next to each other are avaible in column
            if column[i] == "X" and column[i+1] == "X" and column[i+2] == "X" and column[i+3] == "X":
                winner = "Player 1"
            if column[i] == "O" and column[i+1] == "O" and column[i+2] == "O" and column[i+3] == "O":
                winner = "Player 2"
                
    #Checking if somebody won in a row
    for n in range(6):
        for i in range(4): #Only 4 position of 4 element next to each other are avaible in row
            if field[i][5-n] == "X" and field[i+1][5-n] == "X" and field[i+2][5-n] == "X" and field[i+3][5-n] == "X":
                winner = "Player 1"
            if field[i][5-n] == "O" and field[i+1][5-n] == "O" and field[i+2][5-n] == "O" and field[i+3][5-n] == "O":
                winner = "Player 2"
            
    return winner

#
player = 1
sign = "X"

while (True):
        column = int(input("Player "+str(player)+" in wchich column do you want put "+sign+" sign: \n"))
        column -= 1
        if column > 6:
            print("Column number out of range. It must be in range 1-7.")
            continue
        
        #Checking for first free element in the column and if column is not full
        rowSize = field[column].count(" ")
        if rowSize != 0:
            field[column][rowSize-1] = sign
            if player == 1:
                player = 2
                sign = "O"    
            else:
                if player == 2:
                    player = 1
                    sign = "X"   
        else:
            print("This column is full. Try again")
        print(field)
        
        #Check if somebody won the game
        winner = checkIfWon()
        if winner == "Player 1":
            print(winner,"won the game !!!")
            break
        if winner == "Player 2":
            print(winner,"won the game !!!")
            break

        
drawBoard()


