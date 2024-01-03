import copy
import random
from Validnost import *
from potez import *
from Inicijalizacija import *
from Interfejs import *
from Pomocne_funkcije import *

def heuristika(mat, igrac):
    h = 0
    for i in range (8):
        for j in range(8):
            if len(mat[i][j]) > 0:
                if len(mat[i][j]) == 8:
                    if mat[i][j][-1] == igrac:
                        return 1000
                    else:
                        return -1
                else:
                    if mat[i][j][0] == igrac:
                        h += len(mat[i][j])
                    if mat[i][j][-1] == igrac:
                        h += len(mat[i][j])
    return h

def max_stanje(lista):
    return max(lista, key=lambda x: x[1])

def min_stanje(lista):
    return min(lista, key=lambda x: x[1])

def minimax(mat, dubina, moj_potez):
    igrac = "O" if moj_potez else "X"
    igrac_za_heuristiku = "X" if moj_potez else "O"
    func = max_stanje if moj_potez else min_stanje

    if dubina == 0:
        return mat, heuristika(mat, igrac_za_heuristiku), None

    lp = nova_stanja(mat, igrac)

    if len(lp) == 0:
        return mat, heuristika(mat, igrac_za_heuristiku), None

    naj_potez = func([minimax(x[0], dubina - 1, not moj_potez) for x in lp])

    if dubina == 3:
        proba = next((tupl for tupl in lp if tupl[0] == naj_potez[0]), None)
        return naj_potez[0], naj_potez[1], proba
    else:
        return mat, naj_potez[1], None


def nova_stanja(mat, igrac):
    lista_poteza = []
    niz_smerova = ["DD", "DL", "GD", "GL"]
    for i in range(8):
        for j in range(8):
            if len(mat[i][j]) != 0:
                for k in range(len(mat[i][j])):
                    if mat[i][j][k] == igrac:
                        for smer in niz_smerova:
                            if validan_potez(mat, i, j, smer, k + 1, igrac):
                                kopija_mat = copy.deepcopy(mat)
                                igraj_potez(kopija_mat, i, j, smer, k + 1)
                                potez_info = {
                                    "poz_x": i,
                                    "poz_y": j,
                                    "pozicija_steka": k + 1,
                                    "smer": smer
                                }
                                lista_poteza.append((kopija_mat, potez_info))
    return lista_poteza



