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
        
def checkIfLetterWasEntered(letterToCheck,actualWord):
    for letter in actualWord:
        if letter == letterToCheck:
            return True
            break
    
        
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
        
#Import english words
englishWords = []
with open("mix_of_english_words.txt","r",encoding='utf-8',) as fileWithWords:
    for word in fileWithWords:
        englishWords.append(word.strip("\n"))
 

#Lets play :)
while(True):
    #Initial data
    randomNumber = randint(0, 61000)
    wordToGuess = englishWords[randomNumber]
    wordLength = len(wordToGuess)
    hangmanParts = [True,True,True,True,True,True,True,False,False,False,False]
    partNumberToDraw = 7
    actualWord = []
    for letter in wordToGuess:
        actualWord.append("_")
    player = "Player One"
    
    try:
        playersNumber = int(input("How many players will play 1 or 2 ?   If you want to exit enter 0. \n"))
    except ValueError:
        print(" \n")
        print("Wrong type of data. Please try again.")
        continue
        
    if playersNumber == 1:
        while(True):
            print(" \n")
            print("GAME FOR ONE PLAYER")
            
            drawHangman(hangmanParts)
            
            #Checking if player loose
            if hangmanParts[10] == True:
                print(" \n")
                print("YOU LOOSE !!!")
                print(" \n")
                print("Word to guess was: ", wordToGuess)
                break
            
            print(" \n")
            print("Word to guess:")
            drawLettersSpaces(actualWord)
            print(" \n")
            
            #Checking if player won
            if actualWord.count("_") == 0:
                print("YOU WIN !!!")
                break
            
            enteredLetter = input("Enter your letter: ")
            
            if checkIfLetterWasEntered(enteredLetter,actualWord) == True:
                print(" \n")
                print("This letter was entered before. Try sth else.")
                print(" \n")
                continue
            
            isLetterInWord = checkIfWordHaveLetter(wordToGuess,enteredLetter)
            
            #Check if word contain letter
            if isLetterInWord != False:
                setActualWord(isLetterInWord,enteredLetter)
            else:
                hangmanParts[partNumberToDraw] = True
                partNumberToDraw += 1
                
    # Two players mode   
    elif playersNumber == 2:
        while(True):
            print(" \n")
            print("GAME FOR TWO PLAYERS")
            
            drawHangman(hangmanParts)
            
            #Checking if player loose
            if hangmanParts[10] == True:
                print(" \n")
                print("YOU LOOSE !!!")
                print(" \n")
                print("Word to guess was: ", wordToGuess)
                break
            
            print(" \n")
            print("Word to guess:")
            drawLettersSpaces(actualWord)
            print(" \n")
            
            #Checking if player won
            if actualWord.count("_") == 0:
                print(player,"WON !!!")
                break
            
            print(" \n")
            print(player,"turn.")
            enteredLetter = input("Enter your letter: ")
            
            if checkIfLetterWasEntered(enteredLetter,actualWord) == True:
                print(" \n")
                print("This letter was entered before. Try sth else.")
                print(" \n")
                continue
            
            isLetterInWord = checkIfWordHaveLetter(wordToGuess,enteredLetter)
            
            #Check if word contain letter
            if isLetterInWord != False:
                setActualWord(isLetterInWord,enteredLetter)
            else:
                hangmanParts[partNumberToDraw] = True
                partNumberToDraw += 1
            
                #Change player
                if player == "Player One":
                    player = "Player Two"
                else:
                    player = "Player One"
            
    elif playersNumber == 0:
        print(" \n")
        print("Hope see you soon. Good By.")
        break
    else:
        print(" \n")
        print("No, no, no :). Try again !!! \n")
    
    