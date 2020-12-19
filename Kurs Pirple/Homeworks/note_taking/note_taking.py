# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 08:29:10 2020

@author: schomej
"""
import os
import os.path
from os import path

def readFile(fileToRead):
    for line in fileToRead:
        print(line)
    

while(True):
    fileName = input("Please enter file name: \n")
    fileName = fileName +".txt"
    isFileThere = path.isfile(fileName)

    if isFileThere == False:
        textToWrite = str(input("Please enter text to write to the file: \n")) + "\n"
        notesFile = open(fileName,"w")
        notesFile.write(textToWrite)
        notesFile.close()
        break
    if isFileThere == True:
        action = str(input("What next:\n r - read file \n d - delete file \n a - append to file \n c - change single line \n x - exit \n"))
        if action == "x":
            break
        else:
            notesFile = open(fileName,"r+")
            if action == "r":
                readFile(notesFile)
            if action == "a":
                text = str(input("Enter the text which will be added to the file: \n")) + "\n"
                notesFile.write(text)
                readFile(notesFile)
            if action == "c":
                lineNumber = int(input("Which line number do you want to change: "))
                lineNumber -= 1
                newText = str(input("Now enter the new text: ")) + "\n"
                
                fileContentByLines = notesFile.readlines()
                contentLineNumbers = len(fileContentByLines)
                
                while (True):
                    if lineNumber <= contentLineNumbers:
                        fileContentByLines[lineNumber] = newText
                        break
                    else:
                        lineNumber = int(input("Your number line is out of range, enter new number: "))
                        lineNumber -= 1
        
                notesFile.truncate(0)
                
                for line in fileContentByLines:
                    notesFile.write(line)
                    
                readFile(notesFile)
                
            if action == "d":
                os.remove(fileName)
             
            notesFile.close()