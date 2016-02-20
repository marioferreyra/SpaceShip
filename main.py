# -*- coding: utf-8 -*-

import sys
import pygame

ANCHO = 600
ALTO = 680


class Nave(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load("images/nave.png")
        self.rect = self.imagen.get_rect()
        
        self.rect.centerx = ANCHO/2
        self.rect.centery = 610
        print self.rect
    
    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def moverDerecha(self):
        self.rect.left += 100

    def moverIzquierda(self):
        self.rect.left -= 100




def main():
    pygame.init()

    # Creacion Ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # Titulo de ventana
    pygame.display.set_caption("SpaceShip")

    fondo = pygame.image.load("images/fondo.jpg")
    nave = Nave()
    asteroide1 = pygame.image.load("images/asteroide1.png")
    asteroide2 = pygame.image.load("images/asteroide2.png")
    asteroide3 = pygame.image.load("images/asteroide3.png")
    
    reloj = pygame.time.Clock()

    posX, posY = 225, 550

    while True:
        ventana.blit(fondo, (0, 0))
        ventana.blit(asteroide1, (0, 0))
        ventana.blit(asteroide2, (225, 0))
        ventana.blit(asteroide3, (470, 0))
        nave.dibujar(ventana)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    nave.moverIzquierda()
                elif evento.key == pygame.K_RIGHT:
                    nave.moverDerecha()

        reloj.tick(20) # 20 FPS
        pygame.display.update()


main()