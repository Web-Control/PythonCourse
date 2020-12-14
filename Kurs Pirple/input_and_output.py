# -*- coding: utf-8 -*-
"""
Created on Mon Dec 14 07:38:39 2020

@author: schomej
"""
#Introduction

#var = input("Message to the user")

name = input("Please enter yor name: ")
print("Your name is: " + name)

age = int(input("Please enter your age: "))
print("Your age is: " + str(age))

Scores = []

for i in range(5):
    currentScore = float(input("Please enetr the score " + str(i+1) + ": "))
    Scores.append(currentScore)
    print("The score you entered was:",currentScore)
    
    
print(Scores)

#Files

#General form
"""
file = open("Filename","r") #r - read, w - write, a - append
file.close()

"""
vacationSpots = ["London","Paris","New York", "Utah","Iceland"]

vacationFile = open("VacationPlaces", "w")

for spot in vacationSpots:
    vacationFile.write(spot + "\n")

vacationFile.close()

vacationFile = open("VacationPlaces","r")

#theWholeFile = vacationFile.read()
#print(theWholeFile)

firstLine = vacationFile.readline()
print(firstLine)
secondLine = vacationFile.readline()
print(secondLine)

for line in vacationFile:
    print(line, end = "")



vacationFile.close()

finalSpot = "Thailand\n"

vacationFile = open("VacationPlaces", "a")
vacationFile.write(finalSpot)
vacationFile.close()

vacationFile = open("VacationPlaces","r")
for line in vacationFile:
    print(line, end = "")
    
vacationFile.close()

#another way to open file - this way it will close file automaticaly

with open("VacationPlaces","r") as vacationFile:
    for line in vacationFile:
        print(line)
        #hear file will close automaticaly
        
vacationFile.read() #so this will cause error
        

   