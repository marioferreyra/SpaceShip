# -*- coding: utf-8 -*-

import sys
import pygame
import random

from nave import *
from asteroide import *
from score import *
from boton import *
from cursor import *
from highscore import *

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Tamaño de la ventana del juego
ANCHO = 600
ALTO = 680

# Lista de asteriodes
ASTERIODES = []


def newText(texto, superficie, posicion=(0, 0), color=NEGRO, length=12):
    """
    Metodo generico para crear texto.
    """
    fuente = pygame.font.SysFont("comicsansms", length)
    text = fuente.render(texto, True, color)
    superficie.blit(text, posicion)


def pause(ventana, en_pausa):
    """
    Menu de Pausa del juego.
    """
    fps = pygame.time.Clock()

    while en_pausa:
        for evento in pygame.event.get():
            # Click en la "X" de la ventana
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                    # Despausa el juego
                    if evento.key == pygame.K_p:
                        en_pausa = False

        newText("Paused", ventana, (230, 300), BLANCO, 50)
        
        pygame.display.update()
        
        fps.tick(15)


def gameMenu(ventana, sound_click):
    """
    Menu principal del juego.
    """
    cursor = Cursor()

    btn_play = Boton("images/play.png", 228, 200)
    btn_help = Boton("images/help.png", 228, 300)
    btn_quit = Boton("images/quit.png", 228, 400)

    fps = pygame.time.Clock()

    fondo = pygame.image.load("images/fondo.jpg")
    logo = pygame.image.load("images/logo.png")

    click_button = False

    while not click_button:
        for evento in pygame.event.get():
            # Click en la "X" de la ventana
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Click del Mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Click en el boton de "Play Game"
                if cursor.colliderect(btn_play.rect):
                    sound_click.play() # Sonido de Click
                    click_button = True
                # Click en el boton de "Help"
                if cursor.colliderect(btn_help.rect):
                    sound_click.play() # Sonido de Click
                    helpMenu(ventana, sound_click)
                # Click en el boton de "Quit"
                if cursor.colliderect(btn_quit.rect):
                    sound_click.play() # Sonido de Click
                    pygame.quit()
                    sys.exit()

        ventana.blit(fondo, (0, 0))

        cursor.update()

        # Nombre del juego
        ventana.blit(logo, (100, 100))

        btn_play.dibujar(ventana)
        btn_help.dibujar(ventana)
        btn_quit.dibujar(ventana)

        # Muestro el High Score local
        newText("High Score: " + str(getHighScore()), ventana, (200, 500), BLANCO, 50)

        pygame.display.update()
        fps.tick(15)


def helpMenu(ventana, sound_click):
    """
    Menu de ayuda del juego.
    """
    cursor = Cursor()

    fondo = pygame.image.load("images/fondo.jpg")
    flecha_izquierda = pygame.image.load("images/flecha_izquierda.png")
    flecha_derecha = pygame.image.load("images/flecha_derecha.png")
    btn_p = pygame.image.load("images/letra_p.png")

    btn_back = Boton("images/back.png", 228, 600)

    fps = pygame.time.Clock()

    is_back = False

    while not is_back:
        for evento in pygame.event.get():
            # Click en la "X" de la ventana
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Click del Mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Click en el boton de "Play Game"
                if cursor.colliderect(btn_back.rect):
                    sound_click.play() # Sonido de Click
                    is_back = True

        ventana.blit(fondo, (0, 0))
        
        cursor.update()

        newText("Help", ventana, (210, 50), BLANCO, 100)

        ventana.blit(flecha_izquierda, (100, 200))
        newText("Ship move left", ventana, (200, 200), BLANCO, 50)

        ventana.blit(flecha_derecha, (100, 300))
        newText("Ship move right", ventana, (200, 300), BLANCO, 50)

        ventana.blit(btn_p, (100, 400))
        newText("Pause the game", ventana, (200, 400), BLANCO, 50)

        btn_back.dibujar(ventana)

        pygame.display.update()
        
        fps.tick(15)


def gameLoop(ventana, sound_click):
    """
    Loop principal del juego.
    """
    # Fondo del juego
    fondo = pygame.image.load("images/fondo.jpg")
    
    # FPS en que se movera el juego
    fps = pygame.time.Clock()

    en_juego = True
    en_pausa = False

    cursor = Cursor()
    nave = Nave(ANCHO)
    score = Score(0, 0, BLANCO)

    btn_play_again = Boton("images/play_again.png", 235, 250)
    btn_quit = Boton("images/quit.png", 235, 320)

    cargarAsteriodes(ASTERIODES)
    moverAsteroides(ASTERIODES)

    asteroide = elegirAsteriode(ASTERIODES)

    is_highscore = False
    is_destroy = True # Para que solo reproduzca el sonido una sola vez

    while True:
        for evento in pygame.event.get():
            # Click en la "X" de la ventana
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if en_juego:
                if evento.type == pygame.KEYDOWN:
                    # Pausa el juego
                    if evento.key == pygame.K_p:
                        en_pausa = True
                        pause(ventana, en_pausa)
                    # Mover nave a la izquierda
                    if evento.key == pygame.K_LEFT:
                        nave.moverIzquierda()
                    # Mover nave a la derecha
                    elif evento.key == pygame.K_RIGHT:
                        nave.moverDerecha()

            # Click del Mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Click en el boton de "Play Again"
                if cursor.colliderect(btn_play_again.rect):
                    sound_click.play() # Sonido de Click
                    detenerAsteriodes(ASTERIODES)
                    pygame.mixer.music.play() # Musica de fondo
                    gameLoop(ventana, sound_click)
                # Click en el boton de "Quit"
                if cursor.colliderect(btn_quit.rect):
                    sound_click.play() # Sonido de Click
                    pygame.quit()
                    sys.exit()


        # Cargo el fondo
        ventana.blit(fondo, (0, 0))
        
        # Dibujo la nave
        nave.dibujar(ventana)
        # Dibujo el puntaje
        score.dibujar(ventana)

        # Si estoy jugando, dibujo los asteroides y los muevo
        if en_juego:
            asteroide.dibujar(ventana)
            asteroide.mover()

        # Si choco con un asteroide
        if asteroide.rect.colliderect(nave.rect):
            nave.destruccion()
            nave.sonidoDestruccion(is_destroy)
            en_juego = False
            is_destroy = False # Para que solo reproduzca el sonido una sola vez
            newText("GAME OVER", ventana, (200, 200), BLANCO, 50)
            btn_play_again.dibujar(ventana)
            btn_quit.dibujar(ventana)
            
            # Obtengo el puntaje obtenido
            mi_puntaje = score.getPuntaje() # Tipo int

            # Seteo el nuevo puntaje mas alto
            if mi_puntaje > getHighScore():
                is_highscore = True
                setHighScore(score.getPuntaje())

            # Si obtuve un nuevo High Score lo muestro
            if is_highscore:
                newText("New High Score: " + str(mi_puntaje), ventana, (170, 390), BLANCO, 50)

        # Si el asteroide no choca con la nave
        if asteroide.rect.top > ANCHO + 100:
            if en_juego:
                score.aumentar()

            asteroide.rect.top = 10 # Coloco el asteriode en su posicion original
            moverAsteroides(ASTERIODES)
            asteroide = elegirAsteriode(ASTERIODES)

        if not en_juego:
            # De a poco se va apagando la musica de fondo
            pygame.mixer.music.fadeout(3000)

        cursor.update()

        fps.tick(20) # 20 FPS

        pygame.display.update()


def main():
    pygame.init() # Inicializacion del los modulos de Pygame
    
    # Creacion Ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    
    # Nombre de la ventana
    pygame.display.set_caption("Space Ship")
    
    # Icono del juego
    icon = pygame.image.load("images/icon.png")
    pygame.display.set_icon(icon)

    # Musica de fondo
    pygame.mixer.music.load("sounds/sonido_fondo.mp3")
    pygame.mixer.music.play()
    
    sound_click = pygame.mixer.Sound("sounds/click.wav") # Sonido de click

    gameMenu(ventana, sound_click)
    gameLoop(ventana, sound_click)


main()
