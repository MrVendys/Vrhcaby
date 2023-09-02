
import pygame


class Piece:
    def __init__(self,color):
        self.color = color
        self.x = 0
        self.y = 0
        self.positions = []
    def drawItself(self, surface: pygame.Surface, position: tuple, radius):
        pygame.draw.circle(surface,(self.color),position,radius)
        self.x = position[0]
        self.y = position[1]
        self.positions = position

