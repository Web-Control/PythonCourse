# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 22:23:03 2020

@author: psnma
"""

class Pet:
    def __init__(self,petName,petAge,petHunger,petPlayful):
        self.name = petName
        self.age = petAge
        self.hunger = petHunger
        self.playful = petPlayful
    #getters   
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getHunger(self):
        return self.hunger
    def getPlayful(self):
        return self.playful
    
    #setters
    def setName(self,petName):
        self.name = petName
    def setAge(self,petAge):
        self.age = petAge
    def setHunger(self,petHunger):
        self.hunger = petHunger
    def setPlayful(self,petPlayful):
        self.playful = petPlayful
    
    def __str__(self):
        return (self.name + " is " + str(self.age) + " years old.")
        
class Dog(Pet):
    def __init__(self,petName,petAge,petHunger,petPlayful,dogBreed, dogToy):
        Pet.__init__(self,petName,petAge,petHunger,petPlayful)
        self.breed = dogBreed
        self.favoriteToy = dogToy
    def wantsToPlay(self):
        if self.playful == True:
            return ("Dog wants to play with "+ self.favoriteToy)
        else:
            return ("Dog doesn't want to play")
        
        
class Cat(Pet):
    def __init__(self,petName, petAge, petHunger, petPlayful,petPlaceToSit):
        Pet.__init__(self, petName, petAge, petHunger, petPlayful)
        self.favoritePlaceToSit = petPlaceToSit
    def wantsToSit(self):
        if self.playful == False:
            print("The cat wants to sit in ",self.favoritePlaceToSit + ".")
        else:
            print("The cat wants to play")
    def __str__(self):
         return (self.name + " like to sit in "+ self.favoritePlaceToSit+".")
            

class Human:
    def __init__(self, name, Pets):
        self.name = name
        self.Pets = Pets
        
    def hasPets(self):
        if len(self.Pets) != 0:
            return "yes"
        else:
            return "no"


Pet1 = Pet("Jim",3,False,True)

HuskyDog = Dog("Snowball",3,False,True,"Husky","Stick")

play = HuskyDog.wantsToPlay()
print(play)

TypicalCat = Cat("Fluffy",3,False,False,"the sun ray")

TypicalCat.wantsToSit()
print(TypicalCat)
print(HuskyDog)

youAverageHuman = Human("Alice", [HuskyDog,TypicalCat])
hasPet = youAverageHuman.hasPets()

print(hasPet)

print(youAverageHuman.Pets[1].name)