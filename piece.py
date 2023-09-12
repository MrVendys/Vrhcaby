
import pygame


class Piece:
    def __init__(self,color:tuple):
        self.id = None
        self.color = color
        self.position = ()
        self.allSpikes = []
        self.isHighlighted = False
        self.HighlightedColor = (255,0,0)
    def drawItself(self, surface: pygame.Surface, position: tuple, radius):
        pygame.draw.circle(surface,self.color if self.isHighlighted == False else self.HighlightedColor,position,radius)
        self.position = position
    def addSpike(self,spike):
        self.allSpikes.append(spike)


