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
from piece import Piece

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

        
def main():
    global board
    board = GameBoard() 
    global gamePiece
    #Venca = player("black")
    #Stepan = player("white")
    print(len(board.boardList))
    clock = pygame.time.Clock()
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
        pygame.draw.circle(WIN,(0,0,0),(100+radius,50+radius),radius)
def drawSpikes():
    #horní bodce
    startX = WIDTH-100
    startY = 50
    for i in range(12):
        if(i<6): 
            pygame.draw.polygon(WIN,board.boardList[i].color, [[startX-i*50,startY],[startX-50-i*50,startY],[startX-25-i*50,startY+300]])
            if len(board.boardList[i].queueOfPieces) > 0:
                for j in range(len(board.boardList[i].queueOfPieces)):
                    pygame.draw.circle(WIN,board.boardList[i].queueOfPieces[j].color,(startX-i*50-radius,startY+j*50+radius),radius)

        else:
            #jakmile se vykreslí 6, udělá se místo na postřední svislou čáru a začne se dál vykreslovat
            startX = WIDTH-150
            pygame.draw.polygon(WIN,board.boardList[i].color, [[startX-i*50,50],[startX-50-i*50,50],[startX-25-i*50,50+300]])
            if len(board.boardList[i].queueOfPieces) > 0:
                for j in range(len(board.boardList[i].queueOfPieces)):
                    pygame.draw.circle(WIN,board.boardList[i].queueOfPieces[j].color,(startX-i*50-radius,startY+j*50+radius),radius)
    #spodní bodce
    startX = 100
    startY = HEIGHT-50
    for i in range (12):
        if(i+12<18):
            pygame.draw.polygon(WIN,board.boardList[i].color, [[startX+i*50,startY],[startX+50+i*50,startY],[startX+25+i*50,startY-300]])
            if len(board.boardList[i+12].queueOfPieces) > 0:
                for j in range(len(board.boardList[i+12].queueOfPieces)):
                    pygame.draw.circle(WIN,board.boardList[i+12].queueOfPieces[j].color,(startX+i*50+radius,startY-j*50-radius),radius)
        else:
            startX = 150
            pygame.draw.polygon(WIN,board.boardList[i].color, [[startX+i*50,startY],[startX+50+i*50,startY],[startX+25+i*50,startY-300]])
            if len(board.boardList[i+12].queueOfPieces) > 0:
                for j in range(len(board.boardList[i+12].queueOfPieces)):
                    pygame.draw.circle(WIN,board.boardList[i+12].queueOfPieces[j].color,(startX+i*50+radius,startY-j*50-radius),radius)
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
    drawSpikes()
    drawSpikes()
def draw():
    WIN.fill(WIN_COLOR)
    drawGameBoard()
    #drawPieces()
    pygame.display.update()




main()
