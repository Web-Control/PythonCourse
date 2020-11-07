"""
Lists Homework
"""
myUniqueList = []
myLeftOvers = []
print(myUniqueList)

def AddToLeftOvers(Element):
    myLeftOvers.append(Element)

def AddToTheList(Element):
    Output = True
    ListLenght = len(myUniqueList)
    LastIndex = ListLenght -1

    if ListLenght == 0:
        myUniqueList.append(Element)
    else:
        i = 0
        while i < LastIndex+1:
            if myUniqueList[i] == Element:
                Output = False
                AddToLeftOvers(Element)
                break
            if i == LastIndex:
                myUniqueList.append(Element)
            i = i+1
            
    return Output

AddIt = AddToTheList(3)
print(AddIt)
print(myUniqueList)

AddIt = AddToTheList(5)
print(AddIt)
print(myUniqueList)

AddIt = AddToTheList(5)
print(AddIt)
print(myUniqueList)

print(myLeftOvers)

