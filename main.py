# -*- coding: utf-8 -*-

import sys
import pygame

ANCHO = 600
ALTO = 680


# class Nave(pygame.sprite.Sprite):

#     def __init__(self, posX, posY):
#         pygame.sprite.Sprite.__init__(self)

#         self.posX = posX
#         self.posY = posY
#         self.imagen = pygame.image.load("image/nave.png")

#         self.rectangulo = self.imagen.get_rect()

#     def movimientoDerecha(self):
#         pass

#     def movimientoIzquierda(self):
#         pass

#     def dibujar(self, superficie):
#         superficie.blit()



def main():
    pygame.init()

    # Creacion Ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # Titulo de ventana
    pygame.display.set_caption("SpaceShip")

    fondo = pygame.image.load("images/fondo.jpg")
    nave = pygame.image.load("images/nave.png")
    asteroide1 = pygame.image.load("images/asteroide1.png")
    asteroide2 = pygame.image.load("images/asteroide2.png")
    asteroide3 = pygame.image.load("images/asteroide3.png")
    
    reloj = pygame.time.Clock()

    posX, posY = 225, 550

    while True:
        ventana.blit(fondo, (0, 0))
        ventana.blit(nave, (posX, posY))
        ventana.blit(asteroide1, (0, 0))
        ventana.blit(asteroide2, (225, 0))
        ventana.blit(asteroide3, (470, 0))
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    if posX == 470:
                        posX = 225
                    elif posX == 225:
                        posX = 0
                elif evento.key == pygame.K_RIGHT:
                    if posX == 0:
                        posX = 225
                    elif posX == 225:
                        posX = 470
                elif evento.key ==  pygame.K_UP:
                    posY -= 30
                elif evento.key ==  pygame.K_DOWN:
                    posY += 30

        reloj.tick(20) # 20 FPS
        pygame.display.update()


main()