import os
from time import sleep


game_run = True
player1 = True


def cr():
    os.system("clear")


cr()
mode =  input("Would you like to play [1] player? Or [2] player?\n")

board = []
def makeBoard(board):
    for i in range(3):
        temp = []
        for j in range(3):
            temp.append(" - ")
        board.append(temp)

def printBoard(board):
    for i in range(3):
        for j in range(3):
            print(board[i][j], end="")
        print()
    
def winCons(board):
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == " X ":
                count += 1
                if count == 3:
                    print("Player 1 WINS")
                    exit()
    for i in range(3):
        for j in range(3):
            if board 


def turn(player1):
    cr()
    printBoard(board)
    row = input("What row would you like to go to? (1-3)\n")
    if row.isnumeric() == False:
        print("Please choose a valid row")
        turn(player1)
    row = int(row)
    if row > 3 or row < 1:
        print("Please choose a valid row")
        turn(player1)
        
    col = input("What column would you like to go to? (1-3) \n")
    if col.isnumeric() == False:
        print("Please enter a valid column.")
        turn(player1)
    col = int(col)
    if col > 3 or col < 1:
        print("Please enter a valid column.")
        turn(player1)

    if board[row-1][col-1] == " - ":
        if player1:
            board[row-1][col-1] = " X "
            player1 = False
        elif player1 == False:
            board[row-1][col-1] = " O "
            player1 = True
        turn(player1)
        print(board)
    else:
        print("Please choose a valid coordinate.")
        sleep(.5)
        turn(player1)



cr()



makeBoard(board)

if mode == "2":
    while game_run:
        printBoard(board)
        turn(player1)