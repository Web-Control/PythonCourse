"""
Loops drawing TIC TAC TOE Play Board
"""

def drawBoard(rows,columns):
    output = False
    for row in range(rows): #0,1,2,3,4
        if row %2 == 0:
            for column in range(1,columns):
                if column == 3 or column == 6:
                    print("|",end="")
                else:
                    if column != 8:
                        print(" ",end="")
                    else:
                        print(" ")
        else:
            print("--------")
            
    output = True




drawBoard(5,20)
