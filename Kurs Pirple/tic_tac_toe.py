# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 08:36:09 2020

@author: schomej
"""
# / /   0
#-----  1
# / /   2 
#-----  3
# / /   4
#01234



def drawField(field):
    for row in range(5):
        if row %2 == 0:
            practicalRow = int(row/2) #0,1,2
            for column in range(5):
                if column %2 == 0:#0,2,4
                    practicalColumn = int(column/2) #0,1,2
                    if column !=4:
                        print(field[practicalColumn][practicalRow],end="")
                    else:
                        print(field[practicalColumn][practicalRow])
                else:
                     print("|", end = "")    
        else:
            print("-----")

player = 1
currentField = [[" "," "," "],[" "," "," "],[" "," "," "]]
drawField(currentField)
while(True):
    print("Players turn: ", player)
    moveRow = int(input("Please enter the row number:\n"))
    moveColumn = int(input("Please enetr the column number:\n"))
    if player == 1:
        #make move for player one
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "X"
            player = 2
    else:
        #make move for player 2
        if currentField[moveColumn][moveRow] == " ":
            currentField[moveColumn][moveRow] = "O"
            player = 1
    drawField(currentField)

drawField(currentField)