import pygame

from piece import Piece


class Bar:
    def __init__(self,position: tuple):
        self.listOfPieces = []
        self.position = position
    def addPiece(self,piece: Piece):
        self.listOfPieces.append(piece)
        piece.positions = (self.position[0]+15,self.position[1]+15)
        piece.spikeId = None
    def removePiece(self):
        return self.listOfPieces.pop