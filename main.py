# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

ANCHO = 600
ALTO = 680
FONDO = (255, 255, 255) # BLANCO


def main():
    pygame.init()

    # Creacion Ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # Titulo de ventana
    pygame.display.set_caption("SpaceShip")

    nave = pygame.image.load("images/nave.png")
    asteroide1 = pygame.image.load("images/asteroide1.png")
    asteroide2 = pygame.image.load("images/asteroide2.png")
    asteroide3 = pygame.image.load("images/asteroide3.png")
    
    while True:
        ventana.fill(FONDO)
        ventana.blit(nave, (225, 470))
        ventana.blit(asteroide1, (0, 0))
        ventana.blit(asteroide2, (225, 0))
        ventana.blit(asteroide3, (470, 0))
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


main()