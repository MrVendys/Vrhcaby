# git config user.email "vasik.ptak@gmail.com"
# git config user.name "MrVendys"
# git add . -> přidá všechny soubory od Gitu
# git commit -m "přidal jsem soubor vrhcaby"
# git push
# git pull


import queue
import random
import pygame

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WIN_COLOR = (222,184,135)
FPS = 60
pygame.display.set_caption("Vrhcaby")

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

def draw():
    WIN.fill(WIN_COLOR)
    for i in range (6):
        pygame.draw.polygon(WIN,(139,69,19) if i%2 == 0 else (205,133,63), [[50+i*50,50],[100+i*50,50],[75+i*50,350]])
    pygame.display.update()

def main():
    board = gameBoard()
    Venca = player("black")
    Stepan = player("white")

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()


main()
