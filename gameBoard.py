import dice
import spike
import queue

class gameBoard:
    def __init__(self):
        self.dice1 = dice()
        self.dice2 = dice()
        self.boardList = []
        for i in range(24):
            Spike = spike((139,69,19) if i%2 == 0 else (205,133,63),queue.LifoQueue(5))
            self.boardList.append(spike)

    def throwDices(self):
        self.dice1.throw()
        self.dice2.throw()
        return print(" Number on dice 1:", self.dice1.numberOnDice, "\n", "Number on dice 2:", self.dice2.numberOnDice)
