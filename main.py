# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

ANCHO = 500
ALTO = 600
FONDO = (0, 0, 0) # NEGRO

def main():
    pygame.init()

    # Creacion Ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # Titulo de ventana
    pygame.display.set_caption("SpaceShip")

    while True:
        ventana.fill(FONDO)
        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()


main()