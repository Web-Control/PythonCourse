# -*- coding: utf-8 -*-
"""
Created on Wed Dec 16 07:08:48 2020

@author: schomej
"""

participantNumber = 5
participantData = []

registeredParticipants = 0
outputFile = open("ParticipantData.txt","w")

while(registeredParticipants < participantNumber):
    tempPartData = [] #name,country of origin, age
    
    name = input("Please enter your name: ")
    tempPartData.append(name)
    
    country = input("Please enter your country of origin: ")
    tempPartData.append(country)
    
    age = int(input("Please enter your age: "))
    tempPartData.append(age)
    
    participantData.append(tempPartData)
    print(participantData)
    registeredParticipants += 1
    

for participant in participantData:
    for data in participant:
        outputFile.write(str(data))
        outputFile.write(" ")#Max U.S 21
        
    outputFile.write("\n")
  
outputFile.close()

#reading data from file
inputFile = open("ParticipantData.txt","r")
inputList = []

for line in inputFile:
    tempParticipantData = line.strip("\n").split()
    #"Max U.S 21 /n" strip(/n) -> Max U.S 21
    #"Max U.S 21 " split() -> ["Max","U.S","21"]
    
    inputList.append(tempParticipantData)
    print(inputList)

#Make dictionary
age = {}

for part in inputList:
    tempAge = int(part[-1])
    if tempAge in age:
        age[tempAge] += 1
    else:
        age[tempAge] = 1
print(age)

#Finding max age and max counter for age
oldest = 0
youngest = 1000
mostOccuringAge = 0
counter = 0

for tempAge in age:
    if tempAge > oldest:
        oldest = tempAge
    if tempAge < youngest:
        youngest = tempAge
    if age[tempAge] > counter:
        counter = age[tempAge]
        mostOccuringAge = tempAge

print("Oldest:",oldest)
print("Youngest:", youngest)
print("Most occuring age:", mostOccuringAge, "with", counter,"participants.")


inputFile.close()



