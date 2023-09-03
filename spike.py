import pygame
from pygame import Surface
from piece import Piece


class Spike:
    def __init__(self,color):
        self.position = []
        self.queueOfPieces = [] #pop / append
        self.surface = None
        self.color = color
        self.isHighlighted = False
        self.HighlightedColor = (255,0,0)
    def drawItself(self, WIN: Surface, position: tuple):
        self.position = position
        self.surface = WIN
        pygame.draw.polygon(WIN,self.color, position)
    def reDrawItself(self):
        pygame.draw.polygon(self.surface,self.color if self.isHighlighted == False else self.HighlightedColor , self.position)
    def addPiece(self,piece: Piece):
        popedPiece = None
        if(len(self.queueOfPieces)==5):
            popedPiece = self.queueOfPieces[4]
            self.queueOfPieces.pop()
        self.queueOfPieces.append(piece)
        return popedPiece
    def removePiece(self):
        self.queueOfPieces.pop()
                

