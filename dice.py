import random
import pygame

from pygame import Surface
class Dice:
    def __init__(self):
        self.numberOnDice = 6

    def throw(self):
        self.numberOnDice = random.randint(1, 6)
    def drawItself(self, surface: Surface, color: tuple, positions):
        pygame.draw.rect(surface,color,pygame.Rect(positions))
        if(self.numberOnDice == 1):
            self.drawOne(surface, color, positions)
        elif(self.numberOnDice == 2):
            self.drawTwo(surface, color, positions)
        elif(self.numberOnDice == 3):
            self.drawOne(surface, color, positions)
            self.drawTwo(surface, color, positions)
        elif(self.numberOnDice == 4):
            self.drawFour(surface, color, positions)
        elif(self.numberOnDice == 5):
            self.drawOne(surface, color, positions)
            self.drawFour(surface, color, positions)
        elif(self.numberOnDice == 6):    
            self.drawFour(surface, color, positions)
            pygame.draw.circle(surface,(0,0,0),(positions[0]+positions[2]/4,positions[1]+positions[3]/2),5)
            pygame.draw.circle(surface,(0,0,0),(positions[0]+positions[2]*3/4,positions[1]+positions[3]/2),5)

    def drawOne(self,surface: Surface, color: tuple, positions):
        pygame.draw.circle(surface,(0,0,0),(positions[0]+positions[2]/2,positions[1]+positions[3]/2),5)
    def drawTwo(self,surface: Surface, color: tuple, positions):
        pygame.draw.circle(surface,(0,0,0),(positions[0]+positions[2]/4,positions[1]+positions[3]/4),5)
        pygame.draw.circle(surface,(0,0,0),(positions[0]+positions[2]*3/4,positions[1]+positions[3]*3/4),5)
    def drawFour(self,surface: Surface, color: tuple, positions):
        self.drawTwo(surface, color, positions)
        pygame.draw.circle(surface,(0,0,0),(positions[0]+positions[2]/4,positions[1]+positions[3]*3/4),5)
        pygame.draw.circle(surface,(0,0,0),(positions[0]+positions[2]*3/4,positions[1]+positions[3]/4),5)