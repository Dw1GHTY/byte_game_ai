from Validnost import *
from Inicijalizacija import *
from Interfejs import *
from Pomocne_funkcije import *

def igraj_potez(mat, poz_x, poz_y, pravac, poz_u_steku):

    podniz = mat[poz_x][poz_y][poz_u_steku - 1:]    #figure koje se pomeraju
    mat[poz_x][poz_y][poz_u_steku - 1:] = []

    if pravac == 'GD':
        poz_x -= 1
        poz_y += 1
    elif pravac == 'GL':
        poz_x -= 1
        poz_y -= 1
    elif pravac == 'DL':
        poz_x += 1
        poz_y -= 1
    elif pravac == 'DD':
        poz_x += 1
        poz_y += 1

    for figura in podniz:
        mat[poz_x][poz_y].append(figura)

def proveri_moguci_potez(mat, igrac):
    niz_smerova = ["DD", "DL", "GD", "GL"]
    for i in range(8):
        for j in range(8):
            if len(mat[i][j]) != 0:
                for k in range(len(mat[i][j])):
                    if mat[i][j][k] == igrac:
                        for smer in niz_smerova:
                            if validan_potez(mat, i , j, smer, k + 1, igrac):
                                return True
    return False
