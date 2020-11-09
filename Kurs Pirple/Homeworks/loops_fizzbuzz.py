"""
FizzBuzz Prime Task
"""

def isItPrime(number):
    output = False
    for x in range(2,number+1):
        if x == number:
            output = True
        elif number%x == 0:
            break
    return output

def FizzBuzz():
    for x in range(1,101):
        if isItPrime(x):
            print("Prime")
            continue
        
        if x%3 == 0 and x%5 == 0:
            print("FizzBuzz")    
        elif x%3 == 0:
            print("Fizz")
        elif x%5 == 0:
            print("Buzz")
        else:
            print(x)

FizzBuzz()