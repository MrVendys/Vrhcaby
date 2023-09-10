import pygame
from pygame import Surface
from piece import Piece


class Spike:
    def __init__(self,color, id):
        self.id = id
        self.position = []
        self.listOfPieces = []
        self.surface = None
        self.color = color
        self.isHighlighted = False
        self.HighlightedColor = (255,0,0)
    def drawItself(self, WIN: Surface, position: tuple):
        self.position = position
        self.surface = WIN
        pygame.draw.polygon(WIN,self.color if self.isHighlighted == False else self.HighlightedColor , position)
    def addPiece(self,piece: Piece):
        self.listOfPieces.append(piece)
    def removePiece(self):
        return self.listOfPieces.pop()
                

