from dice import Dice
from spike import Spike
from piece import Piece 

class GameBoard:
    def __init__(self):
        self.dice1 = Dice()
        self.dice2 = Dice()
        self.boardList = []
        BLACK = (0,0,0)
        WHITE = (255,255,255)
        blackGamePiece = Piece(BLACK)
        whiteGamePiece = Piece(WHITE)
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

    def throwDices(self):
        self.dice1.throw()
        self.dice2.throw()
        return print(" Number on dice 1:", self.dice1.numberOnDice, "\n", "Number on dice 2:", self.dice2.numberOnDice)
