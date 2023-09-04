import pygame

from piece import Piece


class Bar:
    def __init__(self,position: tuple):
        self.listOfPieces = []
        self.position = position
        self.id = -1
    def addPiece(self,piece: Piece):
        self.listOfPieces.append(piece)
        piece.positions = (self.position[0]+self.position[2]/2,self.position[1]+self.position[2]/2)
        piece.spikeId = None
    def removePiece(self):
        return self.listOfPieces.pop()