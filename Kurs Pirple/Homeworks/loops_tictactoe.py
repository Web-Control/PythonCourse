"""
Loops drawing TIC TAC TOE Play Board
"""
#Screen size
import tkinter as tk
root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# importing os module  
import os 
  
# Get the size 
# of the terminal 
size = os.get_terminal_size() 
terminalColumns = size.columns
terminalRows = size.lines

def drawBoard(rows,columns):
    output = False
    sizeOk = True

    if rows > terminalRows or columns > terminalColumns:
        output = False
        sizeOk = False

    if sizeOk:
        for row in range(rows):
            if row %2 == 0:
                for column in range(1,columns):
                    if column%3 == 0 or column%6 == 0:
                        print("|",end="")
                    else:
                        if column != columns-1:
                            print(" ",end="")
                        else:
                            print(" ")
            else:
                x = 1
                while x < columns+1:
                    if x < columns:
                        print("-",end="")
                    else:
                        print("-")
                    x = x+1
            
            if row == rows-1:
                output = True

    return output




board = drawBoard(8,200)
print(board)

