import pygame, sys
from pygame.locals import *
import random

class Jugador:
    
    def __init__(self,pantalla,posiciones,posicionRnd, color):
        self.pantalla = pantalla
        self.posiciones = posiciones
        self.posicionRnd = posicionRnd
        self.color = color
    
    def moverPosicion(self):
        pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        
        return self.posicionRnd