from Validnost import *
from Inicijalizacija import *
from Interfejs import *
from Pomocne_funkcije import *

def igraj_potez(mat, poz_x, poz_y, pravac, poz_u_steku):

    poz_x = prevedi_slovo_u_broj(poz_x)
    poz_y -= 1

    podniz = mat[poz_x][poz_y][poz_u_steku - 1:]    #figure koje se pomeraju
    mat[poz_x][poz_y][poz_u_steku - 1:] = []        #brisanje ostatka

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