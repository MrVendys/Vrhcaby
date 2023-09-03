import pygame
from pygame import Surface
from piece import Piece


class Spike:
    def __init__(self,color, id):
        self.id = id
        self.position = []
        self.queueOfPieces = [] #pop / append
        self.surface = None
        self.color = color
        self.isHighlighted = False
        self.HighlightedColor = (255,0,0)
    def drawItself(self, WIN: Surface, position: tuple):
        self.position = position
        self.surface = WIN
        pygame.draw.polygon(WIN,self.color if self.isHighlighted == False else self.HighlightedColor , position)
    def reDrawItself(self):
        pygame.draw.polygon(self.surface,self.color if self.isHighlighted == False else self.HighlightedColor , self.position)
    def addPiece(self,piece: Piece):
        self.queueOfPieces.append(piece)
    def removePiece(self):
        popedPiece = None
        popedPiece = self.queueOfPieces.pop()
        return popedPiece
                

