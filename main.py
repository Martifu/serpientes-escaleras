import pygame, sys
from pygame.locals import *
from Jugador import *
from Dados import *
import random
import time

fondo = (204,204,0)
blanco = (0,0,0)
color_texto = (50,60,80)
jugadores = 0


def dibujar_botones_menu(lista_botones):
    for boton in lista_botones:
        if boton['on_click']:
            pantalla.blit(boton['imagen_pressed'], boton['rect'])
        else:
            pantalla.blit(boton['imagen'], boton['rect'])

def menu():
    menu = pygame.display.set_mode((1270, 720))
    otra_pantalla = True
    while otra_pantalla:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.k_1:
                    otra_pantalla = False
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                mouse = event.pos
                for boton in botones:
                    boton['on_click'] = boton['rect'].colliderect([mouse[0], mouse[1], 1, 1])
                    if boton['on_click'] == True:
                        jugadores = boton['jugadores']
                        main.jugadores = jugadores
                    elif boton['on_click'] == True:
                        jugadores = boton['jugadores']
                        main.jugadores = jugadores
                    elif boton['on_click'] == True:
                        jugadores = boton['jugadores']
                        main.jugadores = jugadores
                otra_pantalla = False
        rect_boton_1 = jugador2.get_rect()
        rect_boton_2 = jugador3.get_rect()
        rect_boton_3 = jugador4.get_rect()
        botones = []
        rect_boton_1.topleft = [300, 150]
        rect_boton_2.topleft = [300, 300]
        rect_boton_3.topleft = [300, 450]
        botones.append(
            {'texto': "Nuevo número", 'imagen': jugador2, 'imagen_pressed': jugador2,
             'rect': rect_boton_1,
             'on_click': True, 'jugadores':2},)
        botones.append(
            {'texto': "Nuevo número", 'imagen': jugador3, 'imagen_pressed': jugador3,
             'rect': rect_boton_2,
             'on_click': True, 'jugadores':3}, )
        botones.append(
            {'texto': "Nuevo número", 'imagen': jugador4, 'imagen_pressed': jugador4,
             'rect': rect_boton_3,
             'on_click': True, 'jugadores':4}, )
        pygame.display.flip()
        menu.fill(blanco)
        dibujar_botones_menu(botones)
        pygame.display.update()

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

def informacion(turno):
    fuente = pygame.font.Font(None, 30)
    totaljugadores = fuente.render("total de jugadores" + str(main.jugadores), 0, (0, 0, 0))
    pantalla.blit(totaljugadores, (90, 300))
    if main.jugadores == 2:
        if turno == 0:
            jugador = fuente.render("Turno del jugador: Player 1", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))
        if turno == 1:
            jugador = fuente.render("Turno del jugador: Player 2", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))
    if main.jugadores  == 3:
        if turno == 0:
            jugador = fuente.render("Turno del jugador: Player 1", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))
        if turno == 1:
            jugador = fuente.render("Turno del jugador: Player 2", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))
        if turno == 2:
            jugador = fuente.render("Turno del jugador: Player 3", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))
    if main.jugadores  == 4:
        if turno == 0:
            jugador = fuente.render("Turno del jugador: Player 1", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))
        if turno == 1:
            jugador = fuente.render("Turno del jugador: Player 2", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))
        if turno == 2:
            jugador = fuente.render("Turno del jugador: Player 3", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))
        if turno == 4:
            jugador = fuente.render("Turno del jugador: Player 4", 0, (0, 0, 0))
            pantalla.blit(jugador, (90, 200))


 
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

        [450,625], #Casilla 1
        [520,625], #casilla 2
        [600,625], #casilla 3
        [680,625], #casilla 4
        [760,625], #casilla 5
        [840,625], #casilla 6
        [910,625], #casilla 7
        [1000,625], #casilla 8
        [1070,625], #casilla 9
        [1140,625], #casilla 10

        [1140,550], #casilla 11
        [1070,550], #casilla 12
        [1000,550], #casilla 13
        [910,550], #casilla 14
        [840,550], #casilla 15
        [760,550], #casilla 16
        [680,550], #casilla 17
        [600,550], #casilla 18
        [520,550], #casilla 19
        [450,550], #casilla 20

        [450,500], #casilla 21
        [520,500], #casilla 22
        [600,500], #casilla 23
        [680,500], #casilla 24
        [760,500], #casilla 25
        [840,500], #casilla 26
        [910,500], #casilla 27
        [1000,500], #casilla 28
        [1070,500], #casilla 29
        [1140,500], #casilla 30

        [1140,440], #casilla 31
        [1070,440], #casilla 32
        [1000,440], #casilla 33
        [910,440], #casilla 34
        [840,440], #casilla 35
        [760,440], #casilla 36
        [680,440], #casilla 37
        [600,440], #casilla 38
        [520,440], #casilla 39
        [450,440], #casilla 40

        [450,380], #casilla 41
        [520,380], #casilla 42
        [600,380], #casilla 43
        [680,380], #casilla 44
        [760,380], #casilla 45
        [840,380], #casilla 46
        [910,380], #casilla 47
        [1000,380], #casilla 48
        [1070,380], #casilla 49
        [1140,380], #casilla 50

        [1140,320], #casilla 51
        [1070,320], #casilla 52
        [1000,320], #casilla 53
        [910,320], #casilla 54
        [840,320], #casilla 55
        [760,320], #casilla 56
        [680,320], #casilla 57
        [600,320], #casilla 58
        [520,320], #casilla 59
        [450,320], #casilla 60

        [450,270], #casilla 61
        [520,270], #casilla 62
        [600,270], #casilla 63
        [680,270], #casilla 64
        [760,270], #casilla 65
        [840,270], #casilla 66
        [910,270], #casilla 67
        [1000,270], #casilla 68
        [1070,270], #casilla 69
        [1140,270], #casilla 70

        [1140,210], #casilla 71
        [1070,210], #casilla 72
        [1000,210], #casilla 73
        [910,210], #casilla 74
        [840,210], #casilla 75
        [760,210], #casilla 76
        [680,210], #casilla 77
        [600,210], #casilla 78
        [520,210], #casilla 79
        [450,210], #casilla 80

        [450,150], #casilla 81
        [520,150], #casilla 82
        [600,150], #casilla 83
        [680,150], #casilla 84
        [760,150], #casilla 85
        [840,150], #casilla 86
        [910,150], #casilla 87
        [1000,150], #casilla 88
        [1070,150], #casilla 89
        [1140,150], #casilla 90

        [1140,90], #casilla 91
        [1070,90], #casilla 92
        [1000,90], #casilla 93
        [910,90], #casilla 94
        [840,90], #casilla 95
        [760,90], #casilla 96
        [680,90], #casilla 97
        [600,90], #casilla 98
        [520,90], #casilla 99
        [450,90], #casilla 100
    ]
    menu()
    x=350
    y=625

    posicion1=0
    posicion2=0
    anterior1 = 0
    anterior2 = 0
    jugador1 = Jugador(pantalla,posiciones,0,blanco,anterior1)
    jugador2 = Jugador(pantalla,posiciones,0,color_texto,anterior1)
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
        
        if click:
            if turno == 1:
                dado1 = random.randrange(1,7)
                dado2 = random.randrange(1,7)
                anterior1= posicion1
                posicion1 = posicion1 + dado1+dado2
                dadoImg = Dados(pantalla,dados,dado1,dado2)
                jugador1 = Jugador(pantalla,posiciones,posicion1,blanco,anterior1)
                turno = 0
                
            else:
                dado1 = random.randrange(1,7)
                dado2 = random.randrange(1,7)
                anterior2 = posicion2
                posicion2 = posicion2+ dado1+dado2
                dadoImg = Dados(pantalla,dados,dado1,dado2)
                jugador2 = Jugador(pantalla,posiciones,posicion2,color_texto,anterior2)
                turno = 1
                
            
            click = False
        
        pantalla.fill(fondo)
        dibujar_panel()
        dibujar_tablero()
        dibujar_botones(botones)
        informacion(turno)
        
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
jugador2 = pygame.image.load('img/jugador2.png')
jugador3 = pygame.image.load('img/jugador3.png')
jugador4 = pygame.image.load('img/jugador4.png')

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