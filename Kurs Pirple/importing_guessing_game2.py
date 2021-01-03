# -*- coding: utf-8 -*-
"""
Created on Sun Jan  3 16:59:00 2021

@author: psnma
"""

from random import random
from time import perf_counter

randVal = random()

upper = 1.0
lower = 0.0

currentTime = perf_counter()

while(True):
    guess = (upper+lower)/2
    if guess == randVal:
        print("That is it !!! Guess =",guess)
        break
    elif guess < randVal:
        lower = guess
    else:
        upper = guess
 
print(" ")

afterTime = perf_counter()
executeTime = afterTime - currentTime
print("This program take: "+ str(executeTime) +" seconds.")
    
    
    
