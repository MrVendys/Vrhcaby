import pygame
from pygame import Surface
from piece import Piece


class Spike:
    def __init__(self,color, id):
        self.id = id
        self.color = color
        self.position = ()
        self.listOfPieces = []
        self.isHighlighted = False
        self.HighlightedColor = (255,0,0)
    def drawItself(self, WIN: Surface, position: tuple):
        pygame.draw.polygon(WIN,self.color if self.isHighlighted == False else self.HighlightedColor , position)
        self.position = position
    def addPiece(self,piece: Piece):
        self.listOfPieces.append(piece)
        piece.id = self.listOfPieces.index(self.listOfPieces[-1])
    def removePiece(self):
        return self.listOfPieces.pop()
                

