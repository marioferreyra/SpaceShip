# -*- coding: utf-8 -*-

import sys
import pygame
import random

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Tamaño de la ventana del juego
ANCHO = 600
ALTO = 680

# Lista de asteriodes
ASTERIODES = []


class Nave(pygame.sprite.Sprite):
    """
    Clase para la Nave espacial.
    """
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.imagen = pygame.image.load("images/nave.png")
        self.imagen_explosion = pygame.image.load("images/explosion.png")
        self.rect = self.imagen.get_rect()
        
        self.rect.centerx = ANCHO/2
        self.rect.centery = 610
    
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
        self.rect.top += 10

    def detener(self):
        """
        Mueve el asteroide a su posicion inicial.
        """
        self.rect.top = -50


class Score(pygame.sprite.Sprite):
    """
    Clase para el puntaje del juego.
    """
    def __init__(self, posX, posY):
        pygame.sprite.Sprite.__init__(self)

        self.posX = posX
        self.posY = posY
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
        texto = self.fuente.render("Score: " + str(self.puntaje), True, BLANCO)
        superficie.blit(texto, (self.posX, self.posY))


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


def cargarAsteriodes():
    """
    Agrega una serie de objetos asteriodes a la lista ASTERIODES.
    """
    asteroide1 = Asteroide("images/asteroide1.png", 22, -50)
    asteroide2 = Asteroide("images/asteroide2.png", 236, -50)
    asteroide3 = Asteroide("images/asteroide3.png", 450, -50)
    ASTERIODES.append(asteroide1)
    ASTERIODES.append(asteroide2)
    ASTERIODES.append(asteroide3)


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


def newText(texto, superficie, posicion=(0, 0), color=NEGRO, length=12):
    """
    Metodo generico para crear texto.
    """
    fuente = pygame.font.SysFont("comicsansms", length)
    text = fuente.render(texto, True, color)
    superficie.blit(text, posicion)


def getHighScore():
    """
    Obtiene el puntaje del archivo 'high_score.txt'.
    """
    with open("high_score.txt", "r") as f:
        lineas = f.readlines()
        for l in lineas:
            return int(l)
        f.close()

def setHighScore(new_score):
    """
    Setea un nuevo puntaje en el archivo 'high_score.txt'.
    """
    with open("high_score.txt", "w") as f:
        f.writelines(str(new_score))
        f.close()


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
                quit()

            if evento.type == pygame.KEYDOWN:
                    # Despausa el juego
                    if evento.key == pygame.K_p:
                        en_pausa = False

        newText("Paused", ventana, (230, 300), BLANCO, 50)
        
        pygame.display.update()
        
        fps.tick(15)


def helpMenu(ventana):
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
                quit()

            # Click del Mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Click en el boton de "Play Game"
                if cursor.colliderect(btn_back.rect):
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


def gameMenu(ventana):
    """
    Menu principal del juego.
    """
    cursor = Cursor()

    btn_play = Boton("images/play.png", 228, 200)
    btn_help = Boton("images/help.png", 228, 300)
    btn_quit = Boton("images/quit.png", 228, 400)

    fps = pygame.time.Clock()

    fondo = pygame.image.load("images/fondo.jpg")

    click_button = False

    while not click_button:
        for evento in pygame.event.get():
            # Click en la "X" de la ventana
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit()

            # Click del Mouse
            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Click en el boton de "Play Game"
                if cursor.colliderect(btn_play.rect):
                    click_button = True
                # Click en el boton de "Help"
                if cursor.colliderect(btn_help.rect):
                    helpMenu(ventana)
                # Click en el boton de "Quit"
                if cursor.colliderect(btn_quit.rect):
                    pygame.quit()
                    quit()

        ventana.blit(fondo, (0, 0))

        cursor.update()

        # Nombre del juego
        newText("Space Ship", ventana, (200, 100), BLANCO, 50)
        btn_play.dibujar(ventana)
        btn_help.dibujar(ventana)
        btn_quit.dibujar(ventana)

        # Muestro el High Score local
        newText("High Score: " + str(getHighScore()), ventana, (200, 500), BLANCO, 50)

        pygame.display.update()
        fps.tick(15)


def gameLoop(ventana):
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
    nave = Nave()
    score = Score(0, 0)

    btn_play_again = Boton("images/play_again.png", 235, 250)
    btn_quit = Boton("images/quit.png", 235, 320)

    cargarAsteriodes()

    asteroide = elegirAsteriode(ASTERIODES)

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
                    detenerAsteriodes(ASTERIODES)
                    gameLoop(ventana)
                # Click en el boton de "Quit"
                if cursor.colliderect(btn_quit.rect):
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
            en_juego = False
            newText("GAME OVER", ventana, (200, 200), BLANCO, 50)
            btn_play_again.dibujar(ventana)
            btn_quit.dibujar(ventana)
            
            # Seteo el nuevo puntaje mas alto
            mi_puntaje = score.getPuntaje() # Tipo int

            if mi_puntaje > getHighScore():
                setHighScore(score.getPuntaje())

        # Si el asteroide no choca con la nave
        if asteroide.rect.top > ANCHO + 100:
            if en_juego:
                score.aumentar()
            asteroide.rect.top = 10
            moverAsteroides(ASTERIODES)
            asteroide = elegirAsteriode(ASTERIODES)

        cursor.update()

        fps.tick(20) # 20 FPS

        pygame.display.update()


def main():
    pygame.init() # Inicializacion del los modulos de Pygame
    
    # Creacion Ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    # Nombre de la ventana
    pygame.display.set_caption("Space Ship")
    
    gameMenu(ventana)
    gameLoop(ventana)


main()
