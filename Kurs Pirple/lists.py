"""
Lists in Python
"""
#TestList = ["element1","element2","element3"]
#TestList = [0,1,2]

Scores = [70,85,67.5,90,80]
print(Scores[1])
print(Scores[-2])
print(Scores[0:2]) #range - not inlcuded 2
print(Scores[2:]) #range to the end of the list

Scores[0] = 75
print(Scores[0])

Scores[1:3] = [] #delete value in list
print(Scores)
Scores[2] = ["Hello","World"] #change element in the list and it can be another list

print(Scores)
print(Scores[2][1])

Scores = [70,85,67.5,90,80]
Scores.append(82) #add next elemnt to the end of list
print(Scores)


