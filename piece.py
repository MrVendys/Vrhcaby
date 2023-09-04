
import pygame


class Piece:
    def __init__(self,color:tuple):
        self.color = color
        self.positions = []
        self.allSpikes = []
        self.radius = None
        self.isHighlighted = False
        self.HighlightedColor = (255,0,0)
    def drawItself(self, surface: pygame.Surface, position: tuple, radius):
        pygame.draw.circle(surface,self.color if self.isHighlighted == False else self.HighlightedColor,position,radius)
        self.positions = position
        self.radius = radius
    def addSpike(self,spike):
        self.allSpikes.append(spike)


