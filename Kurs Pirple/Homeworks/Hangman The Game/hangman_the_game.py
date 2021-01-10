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

def setActualWord(letterPlaces,letter):
    for place in letterPlaces:
        actualWord[place-1] = letter
    

def drawLettersSpaces(word):
    for letter in word:
        print(letter+" ", end = "")
        
def checkIfWordHaveLetter(word,letterToFind):
    wordLength = len(word)
    letterPlaces = []
    x = 1
    for letter in word:
        if letter == letterToFind:
            letterPlaces.append(x)
        
        placesAmount = len(letterPlaces)
            
        if x == wordLength and placesAmount > 0:
            return letterPlaces
            break
        elif x == wordLength and placesAmount == 0:
            return False
        x += 1
        
englishWords = []

#Import english words
with open("mix_of_english_words.txt","r",encoding='utf-8',) as fileWithWords:
    for word in fileWithWords:
        englishWords.append(word.strip("\n"))
 
#Initial data
randomNumber = randint(0, 61000)
#wordToGuess = englishWords[randomNumber]
wordToGuess = "playstation"
wordLength = len(wordToGuess)

#Lets play :)
while(True):
    hangmanParts = [True,True,True,True,True,True,True,False,False,False,False]
    partNumberToDraw = 7
    actualWord = []
    for letter in wordToGuess:
        actualWord.append("_")
    
    playersNumber = int(input("How many players will play 1 or 2 ?   If you want to exit enter 0. \n"))
    
    if playersNumber == 1:
        while(True):
            print(" \n")
            print("GAME FOR ONE PLAYER")
            
            drawHangman(hangmanParts)
            
            #Checking if player loose
            if hangmanParts[10] == True:
                print(" \n")
                print("YOU LOOSE !!!")
                break
            
            print(" \n")
            print("Word to guess:")
            drawLettersSpaces(actualWord)
            print(" \n")
            
            #Checking if playe won
            if actualWord.count("_") == 0:
                print("YOU WIN !!!")
                break
            
            enteredLetter = input("Enter your letter: ")
            isLetterInWord = checkIfWordHaveLetter(wordToGuess,enteredLetter)
            
            #Check if word contain letter
            if isLetterInWord != False:
                setActualWord(isLetterInWord,enteredLetter)
            else:
                hangmanParts[partNumberToDraw] = True
                partNumberToDraw += 1
        
    elif playersNumber == 2:
        print("Two players.")
    elif playersNumber == 0:
        print(" \n")
        print("Hope see you soon. Good By.")
        break
    else:
        print(" \n")
        print("No, no, no :). Try again !!! \n")
    
    