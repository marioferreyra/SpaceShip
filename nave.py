# -*- coding: utf-8 -*-

import pygame


class Nave(pygame.sprite.Sprite):
    """
    Clase para la Nave espacial.
    """
    def __init__(self, ancho_pantalla):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load("images/nave.png")
        self.imagen_explosion = pygame.image.load("images/explosion.png")
        self.rect = self.imagen.get_rect()
        
        self.rect.centerx = ancho_pantalla/2
        self.rect.centery = 610

        self.sonido_explosion = pygame.mixer.Sound("sounds/explosion.wav")

    def dibujar(self, superficie):
        """
        Dibuja la nave espacial en la superficie indicada.
        """
        superficie.blit(self.imagen, self.rect)

    def destruccion(self):
        """
        Cambia la imagen principal de la nave por una explosion.
        """
        self.imagen = self.imagen_explosion

    def sonidoDestruccion(self, is_destroy):
        """
        Reproduce el sonido de destruccion de la nave.
        """
        if is_destroy:
            self.sonido_explosion.play()


    def moverDerecha(self):
        """
        Mueve la nave hacia la derecha.
        """
        if self.rect.left <= 450:
            self.rect.left += 25

    def moverIzquierda(self):
        """
        Mueve la nave hacia la izquierda.
        """
        if self.rect.left >= 22:
            self.rect.left -= 25
