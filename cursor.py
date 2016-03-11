# -*- coding: utf-8 -*-

import pygame


class Cursor(pygame.Rect):
    """
    Clase para el cursor del mouse.
    """
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        """
        Obtiene la posicion actual del cursor.
        """
        self.left, self.top = pygame.mouse.get_pos()
