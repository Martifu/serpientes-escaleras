import pygame, sys
from pygame.locals import *
import random
import time
import easygui as eg

class Jugador:
    
    def __init__(self,pantalla,posiciones,posicionRnd, color,anterior):
        self.pantalla = pantalla
        self.posiciones = posiciones
        self.posicionRnd = posicionRnd
        self.anterior = anterior
        self.color = color
    
    def moverPosicion(self):     
        if self.anterior < self.posicionRnd:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            self.anterior = self.anterior + 1
            if self.anterior >=100:
                print('ganaste')
                eg.msgbox(msg='Ganaste',
                            title='Felicidades', 
                            ok_button='Continuar',
                            image='img/winner.png',
                            )
            time.sleep(.3)
        elif self.anterior == 5:
                self.anterior = self.anterior + 30
                pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 9:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior + 42
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 23:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior + 19
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 36:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior- 31
            self.posicionRnd = 5
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 49:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior= self.anterior - 42
            self.posicionRnd = 7
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 56:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior - 48
            self.posicionRnd = 8
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 48:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior  = self.anterior + 38
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 62:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior + 21
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 69:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior + 22
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 87:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior - 21
            self.posicionRnd = 66
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 82:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior - 62
            self.posicionRnd = 20
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        elif self.anterior == 95:
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
            time.sleep(.5)
            self.anterior = self.anterior - 57
            self.posicionRnd = 38
            pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        else: pygame.draw.circle(self.pantalla,self.color,[self.posiciones[self.anterior][0],self.posiciones[self.anterior][1]],20,0)
        return self.anterior