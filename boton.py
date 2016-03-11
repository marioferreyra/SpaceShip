# -*- coding: utf-8 -*-

import pygame


class Boton(pygame.sprite.Sprite):
    """
    Clase para los botones.
    """
    def __init__(self, path_imagen, posX=300, posY=340):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load(path_imagen)
        self.rect = self.imagen.get_rect()
        self.rect.left = posX
        self.rect.top = posY

    def dibujar(self, superficie):
        """
        Dibuja el boton en la superficie indicada.
        """
        superficie.blit(self.imagen, self.rect)
