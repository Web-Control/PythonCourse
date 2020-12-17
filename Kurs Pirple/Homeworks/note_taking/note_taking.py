# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 08:29:10 2020

@author: schomej
"""
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
        textToWrite = str(input("Please enter text to write to the file: \n"))
        notesFile = open(fileName,"w")
        notesFile.write(textToWrite)
        notesFile.close()
        break
    if isFileThere == True:
        action = str(input("What next:\n r - read file \n d - delete file \n a - append to file \n x - exit \n"))
        if action == "x":
            break
        else:
            if action == "r":
                notesFile = open(fileName,"r")
                readFile(notesFile)
                notesFile.close()
            if action == "a":
                notesFile = open(fileName,"r+")
                text = str(input("Enter the text which will be added to the file: \n")) + "\n"
                notesFile.write(text)
                readFile(notesFile)
                notesFile.close()
            