# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 20:52:14 2021

@author: psnma
"""

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
    
    print(topBar)
    print(topPost)
    print(pieceOfPost + head)
    print(pieceOfPost + shoulders)
    print(pieceOfPost + torso)
    print(pieceOfPost + legs)
    print(bottomBar)

hangmanParts = []
drawHangman(hangmanParts)
    