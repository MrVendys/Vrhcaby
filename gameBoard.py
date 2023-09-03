import pygame
from pygame import Surface
from bar import Bar
from dice import Dice
from spike import Spike
from piece import Piece
from player import Player 

class GameBoard:
    def __init__(self, playerB: Player, playerW: Player):
        self.playerB = playerB
        self.playerW = playerW
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.boardList = []
        self.playerPieceList = []
        self.playerBBar = Bar((410,50,30,300))
        self.playerWBar = Bar((410,450,30,300))
        testPiece = Piece((255,255,255))
        testPiece.allSpikes.append(self.playerWBar)
        self.playerWBar.listOfPieces.append(testPiece)
        self.createSpikes()
        self.createPieces()
        
    def createPieces(self):
        for i in range(24):
            if(i == 0):
                for j in range(2):
                    piece = Piece((0,0,0))
                    piece.addSpike(self.boardList[i])
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 5):
                for j in range(5):
                    piece = Piece((255,255,255))
                    piece.addSpike(self.boardList[i])
                    self.playerPieceList.append(piece)
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 7):
                for j in range(3):
                    piece = Piece((255,255,255))
                    piece.addSpike(self.boardList[i])
                    self.playerPieceList.append(piece)
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 9): #vymazat
                    piece = Piece((0,0,0))
                    piece.addSpike(self.boardList[i])
                    self.boardList[i].queueOfPieces.append(piece)        
            if(i == 10): #vymazat
                    piece = Piece((0,0,0))
                    piece.addSpike(self.boardList[i])
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 11):
                for j in range(5):
                    piece = Piece((0,0,0))
                    piece.addSpike(self.boardList[i])
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 12):
                for j in range(5):
                    piece = Piece((255,255,255))
                    piece.addSpike(self.boardList[i])
                    self.playerPieceList.append(piece)
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 16):
                for j in range(3):
                    piece = Piece((0,0,0))
                    piece.addSpike(self.boardList[i])
                    self.boardList[i].queueOfPieces.append(piece)            
            if(i == 18):
                for j in range(5):
                    piece = Piece((0,0,0))
                    piece.addSpike(self.boardList[i])
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 23):
                for j in range(2):
                    piece = Piece((255,255,255))
                    piece.addSpike(self.boardList[i])
                    self.playerPieceList.append(piece)
                    self.boardList[i].queueOfPieces.append(piece)
    def createSpikes(self):
         for i in range(24):
            gameSpike = Spike((139,69,19) if i%2 == 0 else (205,133,63),i)
            self.boardList.append(gameSpike)
    def throwDices(self):
        self.dice1.throw()
        self.dice2.throw()
        return print(" Number on dice 1:", self.dice1.numberOnDice, "\n", "Number on dice 2:", self.dice2.numberOnDice)     
            
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

        pygame.draw.rect(WIN,(0,0,0),self.playerBBar.position,5)
        pygame.draw.rect(WIN,(0,0,0),self.playerWBar.position,5)

        for i in range(len(self.playerBBar.listOfPieces)):
            self.playerBBar.listOfPieces[i].drawItself(WIN,(self.playerBBar.position[0]+15,self.playerBBar.position[1]+15+i*self.playerBBar.listOfPieces[i].radius*2),self.playerBBar.listOfPieces[i].radius)
        for i in range(len(self.playerWBar.listOfPieces)):
            self.playerWBar.listOfPieces[i].drawItself(WIN,(self.playerWBar.position[0]+15,self.playerWBar.position[1]-15-i*25*2),25)
            self.playerPieceList.append(self.playerWBar.listOfPieces[i])


        startX = WIN.get_width()-100
        startY = 50
        radius = 25
        for i in range(12):
            if(i==6): 
                startX -= 50
            self.boardList[i].drawItself(WIN,[[startX-i*50,startY],[startX-50-i*50,startY],[startX-25-i*50,startY+300]])
            if len(self.boardList[i].queueOfPieces) > 0:
                for j in range(len(self.boardList[i].queueOfPieces)):
                    self.boardList[i].queueOfPieces[j].drawItself(WIN,(startX-i*50-radius,startY+j*50+radius),radius)

        #spodní bodce
        startX = 100
        startY = WIN.get_height()-50
        for i in range(12):
            if(i==6): 
                startX += 50
            self.boardList[i+12].drawItself(WIN,[[startX+i*50,startY],[startX+50+i*50,startY],[startX+25+i*50,startY-300]])
            if len(self.boardList[i+12].queueOfPieces) > 0:
                for j in range(len(self.boardList[i+12].queueOfPieces)):
                    self.boardList[i+12].queueOfPieces[j].drawItself(WIN,(startX+i*50+radius,startY-j*50-radius),radius)
            
        self.dice1.drawItself(WIN,(0,255,0),(550,360,80,80))
        self.dice2.drawItself(WIN,(255,255,255),(650,360,80,80))
    



   