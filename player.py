from piece import Piece


class Player:
    def __init__(self):
        self.listOfPieces = []
        self.playerBar = None
    def addPiece(self,piece: Piece):
        self.listOfPieces.append(piece)