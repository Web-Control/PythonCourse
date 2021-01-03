# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 18:51:41 2021

@author: psnma
"""

import random
# import random as r - impot package with nick name
# from random import randint, uniform - importing only function randint and uniform

#random.seed(1)
randInt = random.randint(0, 100)
print(randInt)

randFloat = random.random() # number beetwen 0.0 and 1 not included
print(randFloat)

randUniform = random.uniform(0, 100)#float numbers beetwen range 
print(randUniform)


simpleList = [1,3,5,7,11]
#Choice function
pickElement = random.choice(simpleList)
print(pickElement)

#Shuffle function
print(simpleList)
random.shuffle(simpleList)
print(simpleList)

