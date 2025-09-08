import os
from time import sleep

def cr():
    os.system("clear")

bboard = []
def makeBoard(bboard):
    for i in range(3):
        for i in range(3):
            bboard.append("-")
    print()

cr()

print("")