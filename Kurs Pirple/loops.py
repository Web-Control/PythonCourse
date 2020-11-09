#Loops in Python

word = "Hello"
letters = []

for i in word:
    print(i)

    if i == "e":
        print("What a funny letter")

    letters.append(i)

print(letters)

for n in letters:
    print(n)


numbers = [1,2,3,4,5]

for n in numbers:
    if n%2 == 1:    # % - modulo
        print(n)

#range(start,stop,steps)
numbersList = []
for num in range(1,10,2):
    numbersList.append(num)
    print(num)

print(numbersList)


#While loop

counter = 1
sume = 0
while counter <= 10:
    print(counter)
    sume = sume + counter
    counter = counter+1

print(sume)



lettersPack = ["a","b","c","d","e"]
index = 0

while index < len(lettersPack):
    print(index)
    print(lettersPack[index])
    index =index +1


height = 5000
velocity = 50
time = 0
while height > 0:
    height = height -velocity
    time = time+1

print(height)
print(time)

#Breaking and Countinuing

participants = ["Jen","Alex","Tina","Joe","Ben"]
position = 1

for name in participants:
    if name == "Tina":
        break
    position = position + 1

print(position)

###
participants = ["Jen","Alex","Tina","Joe","Ben"]
index = 0

for currentIndex in range(len(participants)):
    if participants[currentIndex] == "Joe":
        break
        
print(currentIndex)


###

for number in range(10):
    if number%3 == 0:
        print(number)
        print("Divisible by 3")
        continue
    print(number)
    print("Not Diviisble by 3")


#Making Shapes with Loops

#Triangle
length = 10
toPrint = "a"

for pos in range(1,length+1):
    print(toPrint*pos)

for pos in range(length,0,-1):
    print(toPrint*pos)



#Nested Lopps

#TicTacToe Fields
#  /  /  0
#------- 1
#  /  /  2
#------- 3
#  /  /  4

for row in range(5): #0,1,2,3,4
    if row %2 == 0:
        for column in range(1,9):
            if column == 3 or column == 6:
                print("|",end="")
            else:
                if column != 8:
                    print(" ",end="")
                else:
                    print(" ")
    else:
        print("--------")




w=1


