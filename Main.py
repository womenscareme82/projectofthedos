import os
from time import sleep
import random

global player1
player1 = True


def cr():
    os.system("clear")


cr()
mode =  input("Would you like to play [1] player? Or [2] player?\n")
if mode == "1":
    dif = input("[E]asy or [h]ard?\n").lower()

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
    if mode == "2":
        count = 0
        for i in range(3):
            count = 0
            for j in range(3):
                if board[i][j] == " X ":
                    count += 1
                    if count == 3:
                        print("Player 1 WINS!")
                        exit()
        for i in range(3):
            count = 0
            for j in range(3):
                if board[j][i] == " X ":
                    count += 1
                    if count == 3:
                        print("Player 1 WINS!")
                        exit()
        for i in range(3):
            count = 0
            for j in range(3):
                if board[i][j] == " O ":
                    count += 1
                    if count == 3:
                        print("Player 2 WINS!")
                        exit()
        for i in range(3):
            count = 0
            for j in range(3):
                if board[j][i] == " O ":
                    count += 1
                    if count == 3:
                        print("Player 2 WINS!")
                        exit()
    else:
        count = 0
        for i in range(3):
            count = 0
            for j in range(3):
                if board[i][j] == " X ":
                    count += 1
                    if count == 3:
                        print("Player 1 WINS!")
                        exit()
        for i in range(3):
            count = 0
            for j in range(3):
                if board[j][i] == " X ":
                    count += 1
                    if count == 3:
                        print("Player 1 WINS!")
                        exit()
        for i in range(3):
            count = 0
            for j in range(3):
                if board[i][j] == " O ":
                    count += 1
                    if count == 3:
                        print("Bot WINS!")
                        exit()
        for i in range(3):
            count = 0
            for j in range(3):
                if board[j][i] == " O ":
                    count += 1
                    if count == 3:
                        print("Bot WINS!")
                        exit()

def diagWin(board):
    if mode == "2":
        if board[0][0] == " X " and board[1][1] == " X " and board[2][2] == " X ":
            print("Player 1 WINS!")
            exit()
        elif board[0][2] == " X " and board[1][1] == " X " and board[2][0] == " X ":
            print("Player 1 WINS!")
            exit()
        elif board[0][0] == " O " and board[1][1] == " O " and board[2][2] == " O ":
            print("Player 2 WINS!")
            exit()
        elif board[0][2] == " O " and board[1][1] == " O " and board[2][0] == " O ":
            print("Player 2 WINS!")
            exit()
    else:
        if board[0][0] == " X " and board[1][1] == " X " and board[2][2] == " X ":
            print("Player 1 WINS!")
            exit()
        elif board[0][2] == " X " and board[1][1] == " X " and board[2][0] == " X ":
            print("Player 1 WINS!")
            exit()
        elif board[0][0] == " O " and board[1][1] == " O " and board[2][2] == " O ":
            print("Bot WINS!")
            exit()
        elif board[0][2] == " O " and board[1][1] == " O " and board[2][0] == " O ":
            print("Bot WINS!")
            exit()
    
def turn(player1):
    cr()
    printBoard(board)
    if mode == "2":
        row = input("What row would you like to go to? (1-3)\n")
        if row.isnumeric() == False:
            print("Please choose a valid row")
            sleep(.5)
            turn(player1)
        row = int(row)
        if row > 3 or row < 1:
            print("Please choose a valid row")
            sleep(.5)
            turn(player1)
            
        col = input("What column would you like to go to? (1-3) \n")
        if col.isnumeric() == False:
            print("Please enter a valid column.")
            sleep(.5)
            turn(player1)
        col = int(col)
        if col > 3 or col < 1:
            print("Please enter a valid column.")
            sleep(.5)
            turn(player1)

        if board[row-1][col-1] == " - ":
            if player1:
                board[row-1][col-1] = " X "
                player1 = False
            elif player1 == False:
                board[row-1][col-1] = " O "
                print("line 162 DEBUG LINE CHING_CHONG_BING_BONG_I_LIKE_AMONG_US_SKIBIDI_GYATT")
                player1 = True
            cr()
            printBoard(board)
            winCons(board)
            diagWin(board)
            cr()
            turn(player1)
            print(board)
        else:
            print("Please choose a valid coordinate.")
            sleep(.5)
            turn(player1)
    if mode == "1":
        if player1:
            row = input("What row would you like to go to? (1-3)\n")
            if row.isnumeric() == False:
                print("Please choose a valid row")
                sleep(.5)
                turn(player1)
            row = int(row)
            if row > 3 or row < 1:
                print("Please choose a valid row")
                sleep(.5)
                turn(player1)
                
            col = input("What column would you like to go to? (1-3) \n")
            if col.isnumeric() == False:
                print("Please enter a valid column.")
                sleep(.5)
                turn(player1)
            col = int(col)
            if col > 3 or col < 1:
                print("Please enter a valid column.")
                sleep(.5)
                turn(player1)
                
            if board[row-1][col-1] == " - ":
                if player1:
                    board[row-1][col-1] = " X "
                    printBoard(board)
                    player1 = False
                    turn(player1)
        else:
            gotSpot = False
            if dif == "e":
                while gotSpot == False:
                    row = random.randint(0, 2)
                    col = random.randint(0, 2)
                    if board[row][col] == " - ":
                        board[row][col] = " O "
                        gotSpot = True
                        cr()
                        printBoard(board)
                        winCons(board)
                        diagWin(board)
                        player1 = True
cr()

makeBoard(board)

if mode == "2":
    while True:
        printBoard(board)
        turn(player1)
elif mode == "1":
    while True:
        printBoard(board)
        turn(player1)