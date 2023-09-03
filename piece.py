
import pygame


class Piece:
    def __init__(self,color:tuple):
        self.color = color
        self.x = 0
        self.y = 0
        self.positions = []
        self.spikeId = None
        self.allSpikes = []
        self.surface = None
        self.radius = None
        self.isHighlighted = False
        self.HighlightedColor = (255,0,0)
    def drawItself(self, surface: pygame.Surface, position: tuple, radius):
        pygame.draw.circle(surface,self.color if self.isHighlighted == False else self.HighlightedColor,position,radius)
        self.x = position[0]
        self.y = position[1]
        self.positions = position
        self.surface = surface
        self.radius = radius
    def reDrawItself(self):
        pygame.draw.circle(self.surface,self.color if self.isHighlighted == False else self.HighlightedColor,self.positions,self.radius)
    def addSpike(self,spike):
        self.allSpikes.append(spike)


