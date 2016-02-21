# -*- coding: utf-8 -*-

import sys
import pygame
import random
from time import sleep

ANCHO = 600
ALTO = 680


class Nave(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load("images/nave.png")
        self.imagen_explosion = pygame.image.load("images/explosion.png")
        self.rect = self.imagen.get_rect()
        
        self.rect.centerx = ANCHO/2
        self.rect.centery = 610
        print self.rect
    
    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def destruccion(self):
        self.imagen = self.imagen_explosion

    def moverDerecha(self):
        self.rect.left += 100

    def moverIzquierda(self):
        self.rect.left -= 100

    def moverArriba(self):
        self.rect.top -= 100

    def moverAbajo(self):
        self.rect.top += 100


class Asteroide(pygame.sprite.Sprite):

    def __init__(self, path_image, posX=0, posY=0):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load(path_image)
        self.rect = self.imagen.get_rect()

        self.rect.left = posX
        self.rect.top = posY

    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def movimieto(self):
        self.rect.top += 10




def main():
    pygame.init()

    # Creacion Ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # Titulo de ventana
    pygame.display.set_caption("SpaceShip")

    fondo = pygame.image.load("images/fondo.jpg")
    nave = Nave()
    asteroide1 = Asteroide("images/asteroide1.png", 22, 10)
    asteroide2 = Asteroide("images/asteroide2.png", 236, 10)
    asteroide3 = Asteroide("images/asteroide3.png", 450, 10)

    reloj = pygame.time.Clock()

    while True:
        ventana.blit(fondo, (0, 0))
        nave.dibujar(ventana)
        asteroide1.dibujar(ventana)
        asteroide2.dibujar(ventana)
        asteroide3.dibujar(ventana)
        
        aleatorio = random.randint(1, 3)
        if aleatorio == 1:
            asteroide1.movimieto()
        elif aleatorio == 2:
            asteroide2.movimieto()
        elif aleatorio == 3:
            asteroide3.movimieto()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    nave.moverIzquierda()
                elif evento.key == pygame.K_RIGHT:
                    nave.moverDerecha()
                elif evento.key == pygame.K_UP:
                    nave.moverArriba()
                elif evento.key == pygame.K_DOWN:
                    nave.moverAbajo()

        if nave.rect.colliderect(asteroide1.rect):
            nave.destruccion()
        if nave.rect.colliderect(asteroide2.rect):
            nave.destruccion()
        if nave.rect.colliderect(asteroide3.rect):
            nave.destruccion()

        reloj.tick(20) # 20 FPS
        pygame.display.update()


main()
