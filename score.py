# -*- coding: utf-8 -*-

import pygame


class Score(pygame.sprite.Sprite):
    """
    Clase para el puntaje del juego.
    """
    def __init__(self, posX, posY, color):
        pygame.sprite.Sprite.__init__(self)

        self.posX = posX
        self.posY = posY
        self.color = color
        self.puntaje = 0
        self.fuente = pygame.font.SysFont("comicsansms", 40)

    def getPuntaje(self):
        """
        Obtiene el puntaje actual del juego.
        """
        return self.puntaje

    def aumentar(self):
        """
        Aumenta el puntaje del juego.
        """
        self.puntaje += 1

    def reset(self):
        """
        Resetea el puntaje del juego a 0.
        """
        self.puntaje = 0

    def dibujar(self, superficie):
        """
        Dibuja el puntaje en la superficie indicada.
        """
        texto = self.fuente.render("Score: " + str(self.puntaje), True, self.color)
        superficie.blit(texto, (self.posX, self.posY))
