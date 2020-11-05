#Functions

# def FunctionName(Input):
#     Action

#     return Output

def addOne(Number):
    Output = Number +1
    return Output

var = 0
print(var)
var2 = addOne(var)
print(var2)

def addOneAddTwo(NumberOne,NumberTwo):
    Output = NumberOne +1
    Output += NumberTwo + 2
    return Output

sum = addOneAddTwo(1,2)
print(sum)


def printMessage(message, ntimes =1):
    print(message * ntimes)

printMessage("Hello" * 5)