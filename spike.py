import pygame
from pygame import Surface


class Spike:
    def __init__(self):
        self.points = []
        self.queueOfPieces = []
    def drawItself(self, WIN: Surface,color, position: tuple):
        pygame.draw.polygon(WIN,color, position)
                

