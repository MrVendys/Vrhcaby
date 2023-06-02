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
from gameBoard import GameBoard
import dice

WIDTH, HEIGHT = 850, 800
WIN = pygame.display.set_mode((WIDTH,HEIGHT))
WIN_COLOR = (222,184,135)
FPS = 60
pygame.display.set_caption("Vrhcaby")
board = None
gamePiece = None
radius = 25


class player:
    def __init__(self, color: str):
        self.listOfPieces = [piece(color) for _ in range(15)]


class Piece:
    def __init__(self,color):
        self.color = color
        
def main():
    global board
    board = GameBoard() 
    global gamePiece
    gamePiece = Piece((0,0,0))
    board.boardList[0].queueOfPieces.put(gamePiece)
    board.boardList[0].queueOfPieces.put(gamePiece)
    #Venca = player("black")
    #Stepan = player("white")

    clock = pygame.time.Clock()
    print(board.boardList[1].color)
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw()

    pygame.quit()

#TODO: vyřešit generování piece na příslušným spike
def drawPieces():
    for i in range(board.boardList[0].queueOfPieces.qsize()):
        pygame.draw.circle(WIN,gamePiece.color,(100+radius,50+i*50+radius),radius)
def drawSpikes(startX,startY,direction):
    #horní bodce
    for i in range(12):
        if(i<6): 
            pygame.draw.polygon(WIN,board.boardList[i].color, [[WIN.get_width()-100-i*50,50],[WIN.get_width()-100-50-i*50,50],[WIN.get_width()-100-25-i*50,50+300]])
        else:
            #jakmile se vykreslí 6, udělá se místo na postřední svislou čáru a začne se dál vykreslovat
            pygame.draw.polygon(WIN,board.boardList[i].color, [[WIN.get_width()-150-i*50,50],[WIN.get_width()-150-50-i*50,50],[WIN.get_width()-150-25-i*50,50+300]])
    #spodní bodce
    for i in range (12):
        if(i+12<18):
            pygame.draw.polygon(WIN,board.boardList[i].color, [[100+i*50,WIN.get_height()-50],[100+50+i*50,WIN.get_height()-50],[100+25+i*50,WIN.get_height()-50-300]])
        else:
            pygame.draw.polygon(WIN,board.boardList[i].color, [[150+i*50,WIN.get_height()-50],[150+50+i*50,WIN.get_height()-50],[150+25+i*50,WIN.get_height()-50-300]])
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




main()
