# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 11:47:30 2020

Dictionaries and Sets

@author: schomej
"""
mySong = {
    "artist":"Kwiat Jabłoni",
    "title": "Dziś Późno Pójdę Spać",
    "genre":"Alternative",
    "album": "Niemożliwe",
    "originCountry": "Poland",
    "releaseYear":2019,
    "durationsInSeconds": 232,
    "youTubeViews": 22223205,
    "mySonLikeIt": "True"}

for key in mySong:
    print(key + ": " + str(mySong[key]))
    
def guessMySong(key, value):
    output = False
    if key in mySong:
        if str(mySong[key])== value:
            output = True
    
    return output

while True:
    print("Press x for exit.")
    key = input("Guess my song parameter:")
    if key == "x":
        print("Thanks for playing")
        break
    value = input("Guess the " + key + " value:")
    
    print(guessMySong(key,value))
    
    