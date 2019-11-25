import pygame, sys
from pygame.locals import *
from Jugador import *
from Dados import *
import random
import time

fondo = (204,204,0)
blanco = (0,0,0)
color_texto = (50,60,80)

def dibujar_panel():
    panel = pygame.transform.scale(imagen_panel, [1280,700])
    pantalla.blit(panel,[0,0])

def dibujar_botones(lista_botones):
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])

def dibujar_tablero():
    tablero = pygame.transform.scale(imagen_tablero, [800,600])
    pantalla.blit(tablero,[390,50])
 
def main():
    game_over = False
    click = False
    rect_boton_1 = imagen_boton.get_rect()
    rect_tablero = imagen_tablero.get_rect()
    botones = []
    rect_boton_1.topleft = [120, 450]
    botones.append(
        {'texto': "Nuevo número", 'imagen': imagen_boton, 'imagen_pressed': imagen_boton_pressed, 'rect': rect_boton_1,
         'on_click': True})
    posiciones = [
        [350,625],

        [450,625],
        [520,625],
        [600,625],
        [680,625],
        [760,625],
        [840,625],
        [910,625],
        [1000,625],
        [1070,625],
        [1140,625],

        [1140,550],
        [1070,550],
        [1000,550],
        [910,550],
        [840,550],
        [760,550],
        [680,550],
        [600,550],
        [520,550],
        [450,550],

        [450,500],
        [520,500],
        [600,500],
        [680,500],
        [760,500],
        [840,500],
        [910,500],
        [1000,500],
        [1070,500],
        [1140,500],

        [1140,440],
        [1070,440],
        [1000,440],
        [910,440],
        [840,440],
        [760,440],
        [680,440],
        [600,440],
        [520,440],
        [450,440],

        [450,380],
        [520,380],
        [600,380],
        [680,380],
        [760,380],
        [840,380],
        [910,380],
        [1000,380],
        [1070,380],
        [1140,380],

        [1140,320],
        [1070,320],
        [1000,320],
        [910,320],
        [840,320],
        [760,320],
        [680,320],
        [600,320],
        [520,320],
        [450,320],

        [450,270],
        [520,270],
        [600,270],
        [680,270],
        [760,270],
        [840,270],
        [910,270],
        [1000,270],
        [1070,270],
        [1140,270],

        [1140,210],
        [1070,210],
        [1000,210],
        [910,210],
        [840,210],
        [760,210],
        [680,210],
        [600,210],
        [520,210],
        [450,210],

        [450,150],
        [520,150],
        [600,150],
        [680,150],
        [760,150],
        [840,150],
        [910,150],
        [1000,150],
        [1070,150],
        [1140,150],

        [1140,90],
        [1070,90],
        [1000,90],
        [910,90],
        [840,90],
        [760,90],
        [680,90],
        [600,90],
        [520,90],
        [450,90],
    ]

    x=350
    y=625

    posicion1=0
    posicion2=0
    
    jugador1 = Jugador(pantalla,posiciones,0,blanco)
    jugador2 = Jugador(pantalla,posiciones,0,color_texto)
    dadoImg = Dados(pantalla,dados,0,0)
    turno = 1
    while not game_over:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_over = True
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])    
                click = True
            if event.type == MOUSEBUTTONUP:
                for boton in botones:
                    boton['on_click'] = False
        
        if click :
            if turno == 1:
                dado1 = random.randrange(1,7)
                dado2 = random.randrange(1,7)
                posicion1 = posicion1 + dado1+dado2
                dadoImg = Dados(pantalla,dados,dado1,dado2)
                jugador1 = Jugador(pantalla,posiciones,posicion1,blanco)
                turno = 0
                
            else:
                dado1 = random.randrange(1,7)
                dado2 = random.randrange(1,7)
                posicion2 = posicion2+ dado1+dado2
                dadoImg = Dados(pantalla,dados,dado1,dado2)
                jugador2 = Jugador(pantalla,posiciones,posicion2,color_texto)
                turno = 1
                
            
            click = False
        pantalla.fill(fondo)
        dibujar_panel()
        dibujar_tablero()
        dibujar_botones(botones)
        
        
        posicion1= jugador1.moverPosicion()
        posicion2 =jugador2.moverPosicion()
        dadoImg.mostrarDados()
        
        
        

          
        pygame.display.flip()
    pygame.quit()

pygame.init()
dimensiones = [1280, 700]
pantalla = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("Serpientes y escaleras")
imagen_panel = pygame.image.load("img/fondo.jpg")
imagen_tablero = pygame.image.load('img/tablero.jpg')
imagen_boton = pygame.image.load("img/pressed.png")
imagen_boton_pressed = pygame.image.load("img/unpressed.png")

inicio = pygame.image.load("img/dados/inicio.png")
dado1 = pygame.image.load("img/dados/1.png")
dado2 = pygame.image.load("img/dados/2.png")
dado3 = pygame.image.load("img/dados/3.png")
dado4 = pygame.image.load("img/dados/4.png")
dado5 = pygame.image.load("img/dados/5.png")
dado6 = pygame.image.load("img/dados/6.png")
dados = [
    [0,inicio],
    [1,dado1],
    [2,dado2],
    [3,dado3],
    [4,dado4],
    [5,dado5],
    [6,dado6],
]

if __name__ == '__main__':
    main()