# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:52:14 2021

@author: psnma
"""
from random import randint

#HANGMAN THE GAME

# =============================================================================
# print("__________")
# print("  |     |  ")
# print("  |" + "     O")
# print("  |" + "   --|--")
# print("  |" + "     |")
# print("  |" + "    //")
# print("__|__")
# =============================================================================

def drawHangman(parts):
    #parts
    topBar = "__________"
    topPost = "  |     |  "
    pieceOfPost = "  |"
    bottomBar = "__|__"
    head = "     O"
    shoulders = "   --|--"
    torso = "     |"
    legs = "    //"
    
    if parts[0] == True:
        print(topBar)
        
    if parts[1] == True:    
        print(topPost)
        
    if parts[2] == True and parts[7] == True:
        print(pieceOfPost + head)
    elif parts[2] == True:
        print(pieceOfPost)
        
    if parts[3] == True and parts[8] == True:
        print(pieceOfPost + shoulders)
    elif parts[3] == True:
        print(pieceOfPost)
    
    if parts[4] == True and parts[9] == True:
        print(pieceOfPost + torso)
    elif parts[4] == True:
        print(pieceOfPost)
    
    if parts[5] == True and parts[10]:
        print(pieceOfPost + legs)
    elif parts[5] == True:
        print(pieceOfPost)
    
    if parts[6] == True:
        print(bottomBar)


englishWords = []

#Import english words
with open("mix_of_english_words.txt","r",encoding='utf-8',) as fileWithWords:
    for word in fileWithWords:
        englishWords.append(word.strip("\n"))
        

randomNumber = randint(0, 61000)

hangmanParts = [True,True,True,True,True,True,True,False,False,False,False]
#drawHangman(hangmanParts)


    