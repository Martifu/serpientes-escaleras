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

        if self.posicionRnd == 5:
            self.posicionRnd + 31
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 9:
            self.posicionRnd + 42
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 36:
            self.posicionRnd - 32
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 23:
            self.posicionRnd + 20
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 49:
            self.posicionRnd - 42
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 56:
            self.posicionRnd - 48
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 48:
            self.posicionRnd + 38
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 62:
            self.posicionRnd + 21
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 69:
            self.posicionRnd + 22
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 87:
            self.posicionRnd - 21
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 82:
            self.posicionRnd - 62
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        elif self.posicionRnd == 95:
            self.posicionRnd - 57
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        else:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.posicionRnd][0],self.posiciones[self.posicionRnd][1]],20,0)
        return self.posicionRnd