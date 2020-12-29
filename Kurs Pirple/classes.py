# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 13:28:14 2020

@author: psnma
"""

# =============================================================================
# class ClassName:
    
#     def __init__(self):
#         self.Attribute = 0
#     
#     def AnotherFunction(self):
#         Action(s)
# =============================================================================
     
class Team:
    def __init__(self,name = "NaN",origin = "NaN"):
        self.teamName = name
        self.teamOrigin = origin
    
    def defineTeamName(self,name):
        self.teamName = name
    def defineTeamOrigin(self,origin):
        self.teamOrigin = origin
    
        
        

Team1 = Team("Tiger","Chicago")
Team2 = Team("Hawks", "New York")
Team3 = Team()

print(Team1.teamName)
Team1.defineTeamName("Dolphin")
print(Team1.teamName)

print(Team1.teamOrigin)
Team1.defineTeamOrigin("Boston")
print(Team1.teamOrigin)

print(Team2.teamName)
print(Team2.teamOrigin)

print(Team3.teamName)
print(Team3.teamOrigin)

#class inheritance

# =============================================================================
# class inheritanceClassName(ParentClass):
#     def __init__(self,Input1,Input2):
#         ParentClass.__init__(self)
#         self.attribute1 = Input1
#         self.attribute2 = Input2
#         self.attribute3 = 0
#     
#     def anotherMethod(self):
#         Action(s)
# =============================================================================
    

class Player(Team):
    def __init__(self,playerName,playerPoints,teamName,teamOrigin):
        Team.__init__(self,teamName,teamOrigin)
        self.playerName = playerName
        self.playerPoints = playerPoints
        
    def scorePoint(self):
        self.playerPoints += 1
    def setName(self,name):
        self.playerName = name
    def __str__(self): #This allow function print to return this function like this print(object)  
        return self.playerName + " Player has scored: "+ str(self.playerPoints) + " points."
        
        
        
player1 = Player("Sid",0,"Sharks","Chicago")
print(player1.playerName)
print(player1.playerPoints)
print(player1.teamName)
print(player1.teamOrigin)

player1.scorePoint()
print(player1.playerPoints)
print(player1)#connect with __str__ in Player method