# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 08:05:10 2020

@author: schomej
"""
"""
import sys
from termcolor import colored, cprint

text = colored('Hello, World!', 'red', attrs=['reverse', 'blink'])
print(text)
"""
#I don't know why but above import doesn't work for me :(
# ModuleNotFoundError: No module named 'termcolor'

def drawBoard(field):
    for row in range(6):
        for column in range(14):
            if column %2 != 0:
                if column != 13:
                    print(" |", end="")
                else:
                    print(" ")
            else:
                practicalColumn = int(column/2)
                if column != 14:
                    print(field[practicalColumn][row], end="")
                else:
                    print(field[practicalColumn][row])         
        if row < 5:       
            print("--------------------")

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
    for n in range(6):#n is a row
        for i in range(4): #Only 4 position of 4 element next to each other are avaible in row
            if field[i][5-n] == "X" and field[i+1][5-n] == "X" and field[i+2][5-n] == "X" and field[i+3][5-n] == "X":
                winner = "Player 1"
            if field[i][5-n] == "O" and field[i+1][5-n] == "O" and field[i+2][5-n] == "O" and field[i+3][5-n] == "O":
                winner = "Player 2"
                
    #Checking if somebody won in diagonal lines
    #First: diagonal lines from left-bottom corner
    for n in range(3):#We check 3 row from corner
        for i in range(4):#Here we change column
            if field[i][5-n] == "X" and field[i+1][4-n] == "X" and field[i+2][3-n] == "X" and field[i+3][2-n] == "X":
                winner = "Player 1"
            if field[i][5-n] == "O" and field[i+1][4-n] == "O" and field[i+2][3-n] == "O" and field[i+3][2-n] == "O":
                winner = "Player 2"
    #Second: diagonal lines from right-bottom corner
    for n in range(3):#We check 3 row from corner
        for i in range(4):#Here we change column
            if field[6-i][5-n] == "X" and field[5-i][4-n] == "X" and field[4-i][3-n] == "X" and field[3-i][2-n] == "X":
                winner = "Player 1"
            if field[6-i][5-n] == "O" and field[5-i][4-n] == "O" and field[4-i][3-n] == "O" and field[3-i][2-n] == "O":
                winner = "Player 2"
    #Third: diagonal lines from left-top corner
    for n in range(3):#We check 3 row from corner
        for i in range(4):#Here we change column
            if field[i][n] == "X" and field[i+1][n+1] == "X" and field[i+2][n+2] == "X" and field[i+3][n+3] == "X":
                winner = "Player 1"
            if field[i][n] == "O" and field[i+1][n+1] == "O" and field[i+2][n+2] == "O" and field[i+3][n+3] == "O":
                winner = "Player 2"
    #Fourth: diagonal lines from right-top corner
    for n in range(3):#We check 3 row from corner
        for i in range(4):#Here we change column
            if field[6-i][n] == "X" and field[5-i][n+1] == "X" and field[4-i][n+2] == "X" and field[3-i][n+3] == "X":
                winner = "Player 1"
            if field[6-i][n] == "O" and field[5-i][n+1] == "O" and field[4-i][n+2] == "O" and field[3-i][n+3] == "O":
                winner = "Player 2"
    #Check if is a draw
    fullColumn = 0
    for column in field:
        rowSize = column.count(" ") 
        if rowSize == 0:
            fullColumn += 1 
    if fullColumn == 7:
        winner = "Draw"
    return winner

#Initial variables
player = 1
sign = "X"

while (True):
        print("    ")#Space
        column = int(input("Player "+str(player)+" in wchich column from 1 to 7 do you want put "+sign+" sign: \n"))
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
            print("    ")#Space
            print("This column is full. Try again")
            
        print("    ")#Space
        drawBoard(field)
        
        #Check if somebody won the game
        winner = checkIfWon()
        if winner == "Player 1":
            print("    ")#Space
            print(winner,"won the game !!!")
            break
        if winner == "Player 2":
            print("    ")#Space
            print(winner,"won the game !!!")
            break
        if winner == "Draw":
            print("    ")#Space
            print("Draw !!!. Lets try again")
            break
        
        



