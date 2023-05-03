# git config user.email "vasik.ptak@gmail.com"
# git config user.name "MrVendys"
# git add . -> přidá všechny soubory od Gitu
# git commit -m "přidal jsem soubor vrhcaby"
# git push
# git pull


import queue
import random


class gameBoard:
    def __init__(self):
        self.dice1 = dice()
        self.dice2 = dice()
        self.boardList = []
        for i in range(24):
            self.boardList.append(queue.LifoQueue(5))

    def throwDices(self):
        self.dice1.throw()
        self.dice2.throw()
        return print(" Number on dice 1:", self.dice1.numberOnDice, "\n", "Number on dice 2:", self.dice2.numberOnDice)


class player:
    def __init__(self, color: str):
        self.listOfPieces = [piece(color) for _ in range(15)]


class piece:
    def __init__(self, pieceColor: str):
        self.pieceColor = pieceColor


class dice:
    def __init__(self):
        self.numberOnDice = 1

    def throw(self):
        self.numberOnDice = random.randint(1, 6)


def playGame():
    board = gameBoard()
    Venca = player("black")
    Stepan = player("white")
    # gameIsOn = True
    print("Game is on")
    # while (gameIsOn):
    print("Throwing dices...")
    gameBoard.throwDices()


playGame()
