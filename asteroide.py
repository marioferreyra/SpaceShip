# -*- coding: utf-8 -*-

import pygame
import random

class Asteroide(pygame.sprite.Sprite):
    """
    Clase para los Asteroides del juego.
    """
    def __init__(self, path_image, posX=0, posY=0):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load(path_image)
        self.rect = self.imagen.get_rect()

        self.rect.left = posX
        self.rect.top = posY

    def dibujar(self, superficie):
        """
        Dibuja el asteroide en la superficie indicada.
        """
        superficie.blit(self.imagen, self.rect)

    def mover(self):
        """
        Mueve el asteroide hacia abajo.
        """
        self.rect.top += 18

    def detener(self):
        """
        Mueve el asteroide a su posicion inicial.
        """
        self.rect.top = -50


def cargarAsteriodes(lista_asteriodes):
    """
    Agrega una serie de objetos asteriodes a la lista ASTERIODES.
    """
    asteroide1 = Asteroide("images/asteroide1.png", 22, -50)
    asteroide2 = Asteroide("images/asteroide2.png", 236, -50)
    asteroide3 = Asteroide("images/asteroide3.png", 450, -50)
    lista_asteriodes.append(asteroide1)
    lista_asteriodes.append(asteroide2)
    lista_asteriodes.append(asteroide3)


def elegirAsteriode(lista_asteriodes):
    """
    Elige un asteroide de forma random de una lista de asteroides.
    """
    return lista_asteriodes[random.randint(0, 2)]


def moverAsteroides(lista_asteriodes):
    """
    Mueve los asteroides de la lista de asteriodes a una posicion aleatoria.
    """
    for asteroide in lista_asteriodes:
        asteroide.rect.left = random.randint(22, 450)


def detenerAsteriodes(lista_asteriodes):
    """
    Mueve los asteroides de la lista de asteriodes a su posicion inicial.
    """
    for asteroide in lista_asteriodes:
        asteroide.detener()
