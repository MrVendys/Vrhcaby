from pygame import Surface
import pygame
from piece import Piece


class Home:
    def __init__(self):
        self.position = None
        self.listOfPieces = []
        self.isHighlighted = False
    def addPiece(self,piece: Piece):
        self.listOfPieces.append(piece)
    def drawItSelf(self, WIN: Surface, color: tuple, pieceColor: tuple, position: tuple):
        pygame.draw.rect(WIN,color if self.isHighlighted == False else (255,0,0),position)
        for i in range(len(self.listOfPieces)):
            pygame.draw.rect(WIN,pieceColor,(position[0]+5,position[1]+5+i*15,40,10))
        self.position = position