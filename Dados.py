import pygame


class Dados:
    
    def __init__(self,pantalla,dados,dado1,dado2):
        self.pantalla = pantalla
        self.dados = dados
        self.dado1 = dado1
        self.dado2 = dado2
    

    def mostrarDados(self):
        
        dado1 = pygame.transform.scale(self.dados[self.dado1][1], [90,90])
        self.pantalla.blit(dado1,[90,320])

        dado1 = pygame.transform.scale(self.dados[self.dado2][1], [90,90])
        self.pantalla.blit(dado1,[210,320])
