from Validnost import *
from Inicijalizacija import *
from Interfejs import *
from Pomocne_funkcije import *

def igraj_potez(mat, poz_x, poz_y, pravac):

    poz_x = prevedi_slovo_u_broj(poz_x)
    poz_y -= 1
    figura = mat[poz_x][poz_y][0]
    mat[poz_x][poz_y].pop()             #OVDE POSTAVITI LOGIKU ZA POMERANJE VISE OD JEDNE FIGURE
                                        #trenutno samo sa vrha uzima
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
    mat[poz_x][poz_y].append(figura)

