# git config user.email "vasik.ptak@gmail.com"
# git config user.name "MrVendys"
# git add . -> přidá všechny soubory od Gitu
# git commit -m "přidal jsem soubor vrhcaby"
# git push
# git pull


import queue
import random
import pygame
import spike

WIDTH, HEIGHT = 850, 800
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
            Spike = spike((139,69,19) if i%2 == 0 else (205,133,63),queue.LifoQueue(5))
            self.boardList.append(spike)

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

def drawPieces():
    radius = 25
    pygame.draw.circle(WIN,(0,0,0),(100+radius,50+radius),radius)
def drawSpikes(startX,startY,direction):
    #horní bodce
    for i in range (13):
        if(i==6): i+=1
        pygame.draw.polygon(WIN,(139,69,19) if i%2 == 0 else (205,133,63), [[100+i*50,50],[100+50+i*50,50],[100+25+i*50,50+300]])
    #spodní bodce
    for i in range (13):
        if(i==6): i+=1
        pygame.draw.polygon(WIN,(205,133,63) if i%2 == 0 else (139,69,19), [[100+i*50,WIN.get_height()-50],[100+50+i*50,WIN.get_height()-50],[100+25+i*50,WIN.get_height()-50-300]])
def drawGameBoard():
    #horní vodorovná
    pygame.draw.rect(WIN,(139,69,19),(0,0,WIN.get_width(),50))
    #spodní vodorovná
    pygame.draw.rect(WIN,(139,69,19),(0,WIN.get_height()-50,WIN.get_width(),50))
    #levá svislá
    pygame.draw.rect(WIN,(139,69,19),(0,0,100,WIN.get_height()))
    #prostřední svislá
    pygame.draw.rect(WIN,(139,69,19),(400,50,50,WIN.get_height()-100))
    #pravá svislá
    pygame.draw.rect(WIN,(139,69,19),(750,0,100,WIN.get_height()))
    drawSpikes(100,50,"down")
    drawSpikes(100,WIN.get_height()-50,"up")
def draw():
    WIN.fill(WIN_COLOR)
    drawGameBoard()
    drawPieces()
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
