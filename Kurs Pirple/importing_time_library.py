# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 19:36:48 2021

@author: psnma
"""

import time

#Measure time
currentTime = time.clock()
print("Hello")
pastTime = time.clock()
print(pastTime - currentTime)

#Timer on delay - sleep function
print("1")
time.sleep(3)#wait 1 second
print("2")

for i in range(1,11):
    print(i)
    time.sleep(1)
    
