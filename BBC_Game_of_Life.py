import tkinter
import time
import threading

time = 0

# Allow user to input starting conditions by clicking on cells in the grid.

def toggle(event):
    global board
    cell = event.widget
    row = int(cell.grid_info()["row"])
    column = int(cell.grid_info()["column"])

# If the clicked cell is dead, make it a live cell.
    if board[row][column] == 0:
        cell.config(bg = "white")
        board[row][column] = 1

# If the cell is live, change it to dead.
    else:
        cell.config(bg = "black")
        board[row][column] = 0

# This function carries out the calculations for the next frame,
# and then changes the display.
def runApp(event):
    global board
    global boardNext
    global time

    cellNum = 0

# This goes individually through each cell and
# counts the living cells neighbouring it.
    for i in range(0,19):
        for j in range(0,19):
            life = 0
            if i > 0:
                if board[i - 1][j] == 1:
                    life = life + 1
            if i < 19:
                if board[i+1][j] == 1:
                    life = life + 1
            if j > 0:
                if board[i][j-1] == 1:
                    life = life + 1
            if j < 19:
                if board[i][j+1] == 1:
                    life = life + 1
            if i > 0 and j > 0:
                if board[i-1][j-1] == 1:
                    life = life + 1
            if i > 0 and j < 19:
                if board[i-1][j+1] == 1:
                    life = life + 1
            if i < 19 and j > 0:
                if board[i+1][j-1] == 1:
                    life = life + 1
            if i < 19 and j < 19:
                if board[i+1][j+1] == 1:
                    life = life + 1

# With the live neighbours counted, the program determines if the
# current cell should be alive in the next state of the board.
            if board[i][j] == 1:
                if life < 2 or life > 3:
                    boardNext[i][j] = 0
                else:
                    boardNext[i][j] = 1
            else:
                if life == 3:
                    boardNext[i][j] = 1
                else:
                    boardNext[i][j] = 0

# This updates the board using the next state that we calculated.
    for i in range(0,20):
        for j in range(0,20):
            if boardNext[i][j] == 1:
                board[i][j] = 1
            else:
                board[i][j] = 0

# Finally this changes each of the cells to reflect the current state of
# the board. Once again, white cells are live, black cells are dead.
    for i in range(0,20):
        for j in range(0,20):
            if board[i][j] == 0:
                cell = (widgetIdents[cellNum])
                cell.config(bg = "black")
            else:
                cell = (widgetIdents[cellNum])
                cell.config(bg = "white")
            cellNum = cellNum + 1

# This repeats the function again whilst preventing an infinite loop.
    if time < 101:
        time = time+1
        window.update()
        window.after(1000, runApp(window), window)
    

# Here we generate a 20x20 matrix of zeroes and a corresponding grid to display.
# This matrix shall be the board, handling the positions of live and dead cells.
# We also create an identical matrix that will hold results for the next time step.

board = []
boardNext = []

for i in range(0,20):
    boardRow = []
    for j in range(0,20):
        boardRow.append(0)
        
    board.append(boardRow)

for i in range(0,20):
    boardNRow = []
    for j in range(0,20):
        boardNRow.append(0)
        
    boardNext.append(boardNRow)

# This creates the GUI.

window = tkinter.Tk()
window.title("Conway's Game of Life")

widgetIdents = []

# This creates the cells and places them in the GUI in a grid. It also allows the
# cells to be clicked, toggling them between the live and dead states.

for rowNumber, boardRow in enumerate(board):
    for columnNumber, columnEntry in enumerate(boardRow):
        cell = tkinter.Button(window, text = "       ", bg = "black")
        cell.grid(row = rowNumber, column = columnNumber)
        widgetIdents.append(cell)
        cell.bind("<Button-1>", toggle)

# This creates a button that runs the actual simulation of Conway's game of life.

runButton = tkinter.Button(window, text = "Run")
runButton.grid(row = 21, column = 0)
runButton.bind("<Button-1>", runApp)

# This creates a button which allows the user to close the GUI.

quitButton = tkinter.Button(window, text = "Quit", command = window.destroy)
quitButton.grid(row = 21, column = 1)


window.mainloop()
