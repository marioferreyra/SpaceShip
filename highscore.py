# -*- coding: utf-8 -*-


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
