from piece import Piece


class Player:
    def __init__(self, color: str):
        self.listOfPieces = []
        self.playerBar = None
        self.listOfSpikes = []
    def addPiece(self,piece: Piece):
        self.listOfPieces.append(piece)