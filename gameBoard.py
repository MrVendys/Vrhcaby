import pygame
from pygame import Surface
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
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        self.createSpikes()
        self.createPieces()
        
    def createPieces(self):
        for i in range(24):
            if(i == 0):
                for j in range(2):
                    piece = Piece((0,0,0))
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 5):
                for j in range(5):
                    piece = Piece((255,255,255))
                    self.playerPieceList.append(piece)
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 7):
                for j in range(3):
                    piece = Piece((255,255,255))
                    self.playerPieceList.append(piece)
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 11):
                for j in range(5):
                    piece = Piece((0,0,0))
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 12):
                for j in range(5):
                    piece = Piece((255,255,255))
                    self.playerPieceList.append(piece)
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 16):
                for j in range(3):
                    piece = Piece((0,0,0))
                    self.boardList[i].queueOfPieces.append(piece)            
            if(i == 18):
                for j in range(5):
                    piece = Piece((0,0,0))
                    self.boardList[i].queueOfPieces.append(piece)
            if(i == 23):
                for j in range(2):
                    piece = Piece((255,255,255))
                    self.playerPieceList.append(piece)
                    self.boardList[i].queueOfPieces.append(piece)
    def createSpikes(self):
         for i in range(24):
            gameSpike = Spike()
            self.boardList.append(gameSpike)
            

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

        startX = WIN.get_width()-100
        startY = 50
        radius = 25
        for i in range(12):
            if(i==6): 
                startX -= 50
            self.boardList[i].drawItself(WIN,(139,69,19) if i%2 == 0 else (205,133,63),[[startX-i*50,startY],[startX-50-i*50,startY],[startX-25-i*50,startY+300]])
            if len(self.boardList[i].queueOfPieces) > 0:
                for j in range(len(self.boardList[i].queueOfPieces)):
                    self.boardList[i].queueOfPieces[j].drawItself(WIN,(startX-i*50-radius,startY+j*50+radius),radius)

        #spodní bodce
        startX = 100
        startY = WIN.get_height()-50
        for i in range(12):
            if(i==6): 
                startX += 50
            self.boardList[i].drawItself(WIN,(139,69,19) if i%2 == 0 else (205,133,63),[[startX+i*50,startY],[startX+50+i*50,startY],[startX+25+i*50,startY-300]])
            if len(self.boardList[i+12].queueOfPieces) > 0:
                for j in range(len(self.boardList[i+12].queueOfPieces)):
                    self.boardList[i+12].queueOfPieces[j].drawItself(WIN,(startX+i*50+radius,startY-j*50-radius),radius)
            
        
        

        """
        for i in range(24):
            gameSpike = Spike((139,69,19) if i%2 == 0 else (205,133,63))
            if(i == 0):
                for j in range(2):
                    gameSpike.queueOfPieces.append(blackGamePiece)
            if(i == 5):
                for j in range(5):
                    gameSpike.queueOfPieces.append(whiteGamePiece)
            if(i == 7):
                for j in range(3):
                    gameSpike.queueOfPieces.append(whiteGamePiece)
            if(i == 11):
                for j in range(5):
                    gameSpike.queueOfPieces.append(blackGamePiece)
            if(i == 12):
                for j in range(5):
                    gameSpike.queueOfPieces.append(whiteGamePiece)
            if(i == 16):
                for j in range(3):
                    gameSpike.queueOfPieces.append(blackGamePiece)
            if(i == 18):
                for j in range(5):
                    gameSpike.queueOfPieces.append(blackGamePiece)
            if(i == 23):
                for j in range(2):
                    gameSpike.queueOfPieces.append(whiteGamePiece)
            self.boardList.append(gameSpike)
"""
    def throwDices(self):
        self.dice1.throw()
        self.dice2.throw()
        return print(" Number on dice 1:", self.dice1.numberOnDice, "\n", "Number on dice 2:", self.dice2.numberOnDice)



   