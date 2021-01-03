# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:46:33 2021

@author: psnma
"""

from random import randint

randVal = randint(0,100)

while(True):
    guess = int(input("Please enter your guess: "))
    if guess == randVal:
        print("That it is!!!")
        break
    elif guess < randVal:
        print("Your guess is to low.")
    else:
        print("Your guess is to high.")
        
