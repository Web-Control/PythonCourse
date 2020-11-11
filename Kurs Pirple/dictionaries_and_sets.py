# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
Dictionaries nad Sets
"""

#Set

sets = {"Element1","Element2","Element1","Element4"}
print(sets)

if "Element1" in sets:
    print("Yes")


countryList = []
for i in range(5):
    country = input("Please Enter Your Country:")
    countryList.append(country)

contrySet = set(countryList)

print(countryList)
print(contrySet)


#Dictionary

dictionary = {"Key":"Value", "Key2":"Value2", "Key3":"Value3"}
dictionary["Key55"] = 55
print(dictionary)

countryList2 = []
for i in range(5):
    country = input("Please Enter Your Country:")
    countryList2.append(country)

print(countryList2)

countryDictionary = {}
for country in countryList2:
    if country in countryDictionary:
        countryDictionary[country] += 1
    else:
        countryDictionary[country] = 1
        
print(countryDictionary)


#More examples

#Shoes size and quantities
blackShoes = {42:2, 41:3, 40:4, 39:1, 38:0}
print(blackShoes)

while True:
    purchaseSize = int(input("Which shoe size would you like to buy?\n"))
    if purchaseSize < 0:
        break
    if purchaseSize in blackShoes:
        if blackShoes[purchaseSize] > 0:
            blackShoes[purchaseSize] -= 1
        else:
            print("We dont have more shoe in this size")
           
    else:
        print("We dont have shoe in this size")
    print(blackShoes)
