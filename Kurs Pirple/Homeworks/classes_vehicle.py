# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 18:39:44 2021

@author: psnma
"""

class Vehicle:
    def __init__(self,make,model,year,weight):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = False
        self.tripsSinceMaintenance = 0
        self.error = False
        
    #setters
    def setMake(self,make):
        self.make = make
    def setModel(self,model):
        self.model = model
    def setYear(self,year):
        self.year = year
    def setWeight(self,weight):
        self.weight = weight
    
    #other methods
    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False
        self.error = False
    def __str__(self):
        return (self.make + " " + self.model + " " + str(self.year) +" which weight " + str(self.weight) + "kg:\n" + "Need maintenance:"+ str(self.needsMaintenance) + "\n" + "Trips since last maintenance: " + str(self.tripsSinceMaintenance))

class Cars(Vehicle):
    def __init__(self,make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = False
    
    def drive(self):
        self.isDriving = True
    def stop(self):
        self.isDriving = False
        self.tripsSinceMaintenance += 1
        if self.tripsSinceMaintenance > 100:
            self.needsMaintenance = True

class Plane(Vehicle):
    def __init__(self,make, model, year, weight):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = False
        self.errorMessage = "Plane can't fly until it's repaired"
        
    def flying(self):
        if self.needsMaintenance != True:
            self.isFlying = True
        else:
            self.error = True            
            
    def landing(self):
        if self.isFlying == True:
            self.isFlying = False
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
                
        
    
MyCar = Cars("Honda","Civic",2015,1350)
SuperCar = Cars("Ferrari","F430",2007,1890)
CarIwant = Cars("Honda","Civic Type R",2020,1204)

#Drive MyCar
for n in range(102):
    MyCar.drive()
    MyCar.stop()

print(MyCar)

print(" ")

#Drive SuperCar
for n in range(49):
    SuperCar.drive()
    SuperCar.stop()

print(SuperCar)

print(" ")

#Drive CarIwant
for n in range(345):
    CarIwant.drive()
    CarIwant.stop()

print(CarIwant) 

print(" ")

DreamPlane = Plane("Boeing", "787-8 Dreamliner", 2019, 101000)
#Lets fly
for n in range(1002):
    if DreamPlane.error != True:
        DreamPlane.flying()
        DreamPlane.landing()
    else:
        print(DreamPlane.errorMessage)
        break
    
print(DreamPlane)
DreamPlane.repair()
print(" ")
print(DreamPlane)

