import random
class dice:
    def __init__(self):
        self.numberOnDice = 1

    def throw(self):
        self.numberOnDice = random.randint(1, 6)
