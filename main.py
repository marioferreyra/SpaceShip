# -*- coding: utf-8 -*-

import sys
import pygame
import random
from time import sleep

BLANCO = (255, 255, 255)
ANCHO = 600
ALTO = 680
ASTERIODES = []
ventana = pygame.display.set_mode((ANCHO, ALTO))


class Nave(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load("images/nave.png")
        self.imagen_explosion = pygame.image.load("images/explosion.png")
        self.rect = self.imagen.get_rect()
        
        self.rect.centerx = ANCHO/2
        self.rect.centery = 610
    
    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def destruccion(self):
        self.imagen = self.imagen_explosion

    def moverDerecha(self):
        if self.rect.left <= 450:
            self.rect.left += 25

    def moverIzquierda(self):
        if self.rect.left >= 22:
            self.rect.left -= 25


class Asteroide(pygame.sprite.Sprite):

    def __init__(self, path_image, posX=0, posY=0):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load(path_image)
        self.rect = self.imagen.get_rect()

        self.rect.left = posX
        self.rect.top = posY

    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)

    def mover(self):
        self.rect.top += 10

    def detener(self):
        self.rect.top = 0


class Score(pygame.sprite.Sprite):

    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)

        self.posX = posX
        self.posY = posY
        self.puntaje = 0
        self.fuente = pygame.font.SysFont("comicsansms", 40)

    def getPuntaje(self):
        return self.puntaje

    def aumentar(self):
        self.puntaje += 1

    def resetear(self):
        self.puntaje = 0

    def dibujar(self, superficie):
        texto = self.fuente.render("Score: " + str(self.puntaje), True, BLANCO)
        superficie.blit(texto, (self.posX, self.posY))


class Cursor(pygame.Rect):

    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)

    def update(self):
        self.left, self.top = pygame.mouse.get_pos()


class Boton(pygame.sprite.Sprite):

    def __init__(self, imagen, posX=300, posY=340):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load(imagen)
        self.rect = self.imagen.get_rect()
        self.rect.left = posX
        self.rect.top = posY

    def update(self, superficie):
        superficie.blit(self.imagen, self.rect)


def moverAsteroides(lista_asteriodes):
    for asteroide in lista_asteriodes:
        asteroide.rect.left = random.randint(22, 450)


def cargarAsteriodes():
    asteroide1 = Asteroide("images/asteroide1.png", 22, -50)
    asteroide2 = Asteroide("images/asteroide2.png", 236, -50)
    asteroide3 = Asteroide("images/asteroide3.png", 450, -50)
    ASTERIODES.append(asteroide1)
    ASTERIODES.append(asteroide2)
    ASTERIODES.append(asteroide3)


def elegirAsteriode(lista_asteriodes):
    return lista_asteriodes[random.randint(0, 2)]


def gameName(superficie):
    fuente = pygame.font.SysFont("comicsansms", 50)
    texto = fuente.render("Space Ship", True, BLANCO)
    superficie.blit(texto, (200, 100))


def gameOver(superficie):
    fuente = pygame.font.SysFont("comicsansms", 50)
    texto = fuente.render("GAME OVER", True, BLANCO)
    superficie.blit(texto, (200, 340))


def printHighScore(superficie):
    fuente = pygame.font.SysFont("comicsansms", 50)

    with open("highscore.txt", "r") as f:
        lineas = f.readlines()
        for l in lineas:
            texto = fuente.render("High Score: " + l, True, BLANCO)
        f.close()

    superficie.blit(texto, (200, 400))



def getHighScore():
    with open("highscore.txt", "r") as f:
        lineas = f.readlines()
        for l in lineas:
            return int(l)
        f.close()

def setHighScore(new_score):
    with open("highscore.txt", "w") as f:
        f.writelines(str(new_score))
        f.close()


def gameIntro():
    cursor = Cursor()

    btn_play = Boton("images/btn_play.png", 228, 200)
    btn_quit = Boton("images/btn_quit.png", 228, 300)

    clock = pygame.time.Clock()

    fondo = pygame.image.load("images/fondo.jpg")

    click = False

    while not click:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if cursor.colliderect(btn_play.rect):
                    click = True
                if cursor.colliderect(btn_quit.rect):
                    pygame.quit()
                    quit()

        ventana.blit(fondo, (0, 0))

        cursor.update()
        gameName(ventana)
        btn_play.update(ventana)
        btn_quit.update(ventana)
        printHighScore(ventana)

        pygame.display.update()
        clock.tick(15)


def gameLoop():
    # Creacion Ventana
    # Ver de acomodar bien las variables
    # ventana = pygame.display.set_mode((ANCHO, ALTO))

    # Titulo de ventana
    pygame.display.set_caption("Space Ship")

    fondo = pygame.image.load("images/fondo.jpg")
    fps = pygame.time.Clock()

    en_juego = True

    nave = Nave()
    score = Score(0, 0)
    cargarAsteriodes()

    asteroide = elegirAsteriode(ASTERIODES)

    while True:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if en_juego:
                # Movimientos
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_LEFT:
                        nave.moverIzquierda()
                    elif evento.key == pygame.K_RIGHT:
                        nave.moverDerecha()

        # Cargo el fondo
        ventana.blit(fondo, (0, 0))
        
        # Dibujo la nave
        nave.dibujar(ventana)
        score.dibujar(ventana)

        if en_juego:
            asteroide.dibujar(ventana)
            asteroide.mover()

        # GAME OVER
        if asteroide.rect.colliderect(nave.rect):
            nave.destruccion()
            en_juego = False
            gameOver(ventana)

            # Seteo el nuevo puntaje mas alto
            mi_puntaje = score.getPuntaje() # Tipo int
            if mi_puntaje > getHighScore():
                setHighScore(score.getPuntaje())

        if asteroide.rect.top > ANCHO + 100:
            if en_juego:
                score.aumentar()
            asteroide.rect.top = 10
            moverAsteroides(ASTERIODES)
            asteroide = elegirAsteriode(ASTERIODES)


        fps.tick(20) # 20 FPS

        pygame.display.update()


def main():
    pygame.init()
    gameIntro()
    gameLoop()


main()
