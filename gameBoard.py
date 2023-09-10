import pygame
from pygame import Surface
from bar import Bar
from dice import Dice
from spike import Spike
from piece import Piece
from player import Player 
import sys

class GameBoard:
    def __init__(self, playerB: Player, playerW: Player):
        self.playerB = playerB
        self.playerW = playerW
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.boardList = []
        self.playerPieceList = []
        self.playerBBar = Bar((410,50,30,300),-1)
        self.playerWBar = Bar((410,450,30,300),24)
        playerB.playerBar = self.playerBBar
        playerW.playerBar = self.playerWBar
        self.createSpikes()
        self.createPieces()
        
    def createPieces(self):
        testPiece = Piece((255,255,255))
        testPiece.allSpikes.append(self.playerW.playerBar)
        self.playerW.playerBar.addPiece(testPiece)
        self.playerW.addPiece(testPiece)
        for i in range(24):
            if(i == 0):
                for j in range(2):
                    self.managePiece((0,0,0),i)
            if(i == 5):
                for j in range(5):
                    self.managePiece((255,255,255),i)
            if(i == 7):
                for j in range(3):
                    self.managePiece((255,255,255),i)
            if(i == 9): #vymazat
                    self.managePiece((0,0,0),i)       
            if(i == 10): #vymazat
                    self.managePiece((0,0,0),i)
            if(i == 11):
                for j in range(5):
                    self.managePiece((0,0,0),i)
                    
            if(i == 12):
                for j in range(5):
                    self.managePiece((255,255,255),i)
                    
            if(i == 16):
                for j in range(3):
                    self.managePiece((0,0,0),i)
                                
            if(i == 18):
                for j in range(5):
                    self.managePiece((0,0,0),i)
                    
            if(i == 23):
                for j in range(2):
                    self.managePiece((255,255,255),i)
                    
    def managePiece(self,color: tuple, index):
        piece = Piece(color)
        piece.addSpike(self.boardList[index])
        self.boardList[index].listOfPieces.append(piece)
        if(color == (255,255,255)):
            self.playerW.addPiece(piece)
        else:
            self.playerB.addPiece(piece)
    def createSpikes(self):
        for i in range(24):
            gameSpike = Spike((139,69,19) if i%2 == 0 else (205,133,63),i)
            self.boardList.append(gameSpike)
    def throwDices(self):
        self.dice1.throw()
        self.dice2.throw()
            
    def drawGameBoard(self,WIN: Surface):
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

        pygame.draw.rect(WIN,(0,0,0),self.playerB.playerBar.position,5)
        pygame.draw.rect(WIN,(0,0,0),self.playerW.playerBar.position,5)
        #pygame.draw.rect(WIN,(0,0,0),(WIN.get_width()-75,50,50,300))

        #Vykreslování kamenů na 
        for i in range(len(self.playerB.playerBar.listOfPieces)):
            radius = 25
            piece = self.playerB.playerBar.listOfPieces[i]
            piece.drawItself(WIN,\
            (self.playerB.playerBar.position[0]+15,self.playerB.playerBar.position[1]+15+i*radius*2),radius)
        for i in range(len(self.playerW.playerBar.listOfPieces)):
            radius = 25
            self.playerW.playerBar.listOfPieces[i].drawItself(WIN,\
            (self.playerW.playerBar.position[0]+15,self.playerW.playerBar.position[1]-15-i*radius*2),radius)
            
        #horní bodce
        startX = WIN.get_width()-100
        startY = 50
        radius = 25
        width = 50
        for i in range(12):
            if(i==6): 
                startX -= 50
            self.boardList[i].drawItself(WIN,[[startX-i*width,startY],[startX-width-i*width,startY],[startX-25-i*width,startY+300]])
            if len(self.boardList[i].listOfPieces) > 0:
                for j in range(len(self.boardList[i].listOfPieces)):
                    self.boardList[i].listOfPieces[j].drawItself(WIN,(startX-i*width-radius,startY+j*width+radius),radius)

        #spodní bodce
        startX = 100
        startY = WIN.get_height()-50
        for i in range(12):
            if(i==6): 
                startX += 50
            self.boardList[i+12].drawItself(WIN,[[startX+i*width,startY],[startX+width+i*width,startY],[startX+width/2+i*width,startY-300]])
            if len(self.boardList[i+12].listOfPieces) > 0:
                for j in range(len(self.boardList[i+12].listOfPieces)):
                    self.boardList[i+12].listOfPieces[j].drawItself(WIN,(startX+i*width+radius,startY-j*width-radius),radius)
            
        self.dice1.drawItself(WIN,(255,255,255),(550,360,80,80))
        self.dice2.drawItself(WIN,(255,255,255),(650,360,80,80))
    def drawAIplays(self,WIN:Surface):
        pygame.font.init()
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        TRANSPARENT = (0, 0, 0, 0)  # Průhledná barva

        # Font pro text
        font = pygame.font.Font(None, 36)

        # Text pro zobrazení
        text = "Hraje počítač"
        text_surface = font.render(text, True, WHITE)

        # Čtverec pro indikaci tahu hráče
        square_width = 200
        square_height = 100
        square_x = (WIN.get_width() - square_width) // 2
        square_y = (WIN.get_height() - square_height) // 2
        square_color = TRANSPARENT  # Počáteční průhledný čtverec

        # Časovač pro zobrazení čtverce
        show_square_delay = 3  # Zobrazení na 3 sekundy
        show_square_start_time = None
        text_x = (WIN.get_width() - text_surface.get_width()) // 2
        text_y = (WIN.get_height() - text_surface.get_height()) // 2
        pygame.draw.rect(WIN, square_color, (square_x, square_y, square_width, square_height))
        WIN.blit(text_surface, (text_x, text_y))

        # Vykreslení čtverce
        pygame.display.flip()




   