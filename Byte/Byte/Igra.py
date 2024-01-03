import copy
import time

from Validnost import *
from Inicijalizacija import *
from Interfejs import *
from Pomocne_funkcije import *
from potez import *
from AI_ver2 import *

def kraj_igre(igrac_x, igrac_y):
    if igrac_x == 2 or igrac_y == 2:
        return True
    return False

def proveri_stek(mat, igrac_x, igrac_o):
    n = len(mat)
    for i in range(n):
        for j in range(n):
            if len(mat[i][j]) == 8:
                poslednji_element = mat[i][j][-1]
                if poslednji_element == 'X':
                    igrac_x += 1
                elif poslednji_element == 'O':
                    igrac_o += 1
                #isprazni element matrice
                mat[i][j] = []

    return igrac_x, igrac_o

def promeni_igraca(trenutni_igrac):
    if trenutni_igrac[0] == 'X':
        trenutni_igrac[0] = 'O'
    else:
        trenutni_igrac [0] = 'X'


def start_game():
    n = 0
    while True:
        try:
            n = int(input("\033[93mUnesite dimenziju table (8): \033[0m"))
            if n == 8:
                break
            else:
                print("Nevažeća dimenzija")
        except ValueError:
            print("Nevažeći unos. Molimo unesite broj.")

    # Unos pocetnog igraca
    starting_player = ''
    while True:
        try:
            starting_player_input = input("\033[93mKo prvi igra, X ili O? \033[0m").upper()
            if starting_player_input in ['X', 'O']:
                starting_player = starting_player_input
                break
            else:
                print("Nevažeći unos. Molimo unesite X ili O.")
        except ValueError:
            print("Nevažeći unos. Molimo unesite broj.")

    tabla = inicijalizacija_matrice(n)
    inicijalizacija_stanja(tabla, n)

    racunar = False
    covek_racunar = input("\033[93mDa li zelite da igrate protiv racunara? \033[0m").upper()
    if covek_racunar == "DA":
        racunar = True
        print("Igrate igru protiv racunara. Racunar je ->O<-")


    igrac_x = 0
    igrac_o = 0
    trenutni_igrac = list()
    trenutni_igrac.append(starting_player)
    while not kraj_igre(igrac_x, igrac_o):
        if proveri_moguci_potez(tabla, trenutni_igrac[0]):
            stampaj_tabelu(tabla)
            if not (racunar is True and trenutni_igrac[0] == "O"):
                while True:
                    try:
                        print(f"Na redu je igrac: {trenutni_igrac[0]}")
                        poz_x_input = input("Unesi slovo reda: ").upper()
                        if poz_x_input in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
                            poz_x = prevedi_slovo_u_broj(poz_x_input)
                            break
                        else:
                            print("Nevažeći unos. Molimo unesite slovo reda A-H.")
                    except ValueError:
                        print("Nevažeći unos. Molimo unesite slovo.")
                while True:
                    try:
                        poz_y_input = int(input("Unesi broj kolone: "))
                        if 1 <= poz_y_input <= 8:
                            poz_y = poz_y_input - 1
                            break
                        else:
                            print("Nevažeći unos. Molimo unesite broj kolone 1-8")
                    except ValueError:
                        print("Nevažeći unos. Molimo unesite broj.")
                while True:
                    try:
                        poz_steka_input = int(input("Unesi poziciju figure na steku: "))
                        if 1 <= poz_steka_input <= 7:
                            poz_steka = poz_steka_input
                            break
                        else:
                            print("Nevažeći unos. Molimo unesite broj od 1 do 7")
                    except ValueError:
                        print("Nevazeci unos.")

                while True:
                    try:
                        pravac_input = input("Unesi pravac kretanja: ").upper()
                        if pravac_input in ['GL', 'GD', 'DL', 'DD']:
                            pravac = pravac_input
                            break
                        else:
                            print("Nevažeći unos. Molimo unesite jedan od četiri pravca kretanja: GL/GD/DL/DD")
                    except ValueError:
                        print("Nevažeći unos. Molimo unesite slova.")

            else:
                print("Razmišljam...")
                pocetak_vremena = time.time()
                pomocna = minimax(tabla, 3, True)
                poz_x = pomocna[2][1]["poz_x"]
                poz_y = pomocna[2][1]["poz_y"]
                poz_steka = pomocna[2][1]["pozicija_steka"]
                pravac = pomocna[2][1]["smer"]
                kraj_vremena = time.time()
                ukupno_vreme = kraj_vremena - pocetak_vremena
                if ukupno_vreme < 1.5:
                    time.sleep(1.7)

            print("")
            if validan_potez(tabla, poz_x, poz_y, pravac, poz_steka, trenutni_igrac[0]):
                igraj_potez(tabla, poz_x, poz_y, pravac, poz_steka)
                print(f"\033[93m {trenutni_igrac[0]}, potez odigran!!\033[0m")
                igrac_x, igrac_o = proveri_stek(tabla, igrac_x, igrac_o)
                print(f"Broj stekova nakon odigranog poteza: igrac X: {igrac_x}, igrac O: {igrac_o}")
                if(kraj_igre(igrac_x, igrac_o)):
                    stampaj_tabelu(tabla)
                    pobednik = ''
                    if igrac_x == 2:
                        pobednik = 'Igrac X'
                    elif igrac_o == 2:
                        pobednik = 'Igrac O'
                    print(f"\033[93m Pobednik je: {pobednik}")
                    print(" KRAJ IGRE!")
                    return 0

                promeni_igraca(trenutni_igrac)
            else:
                print("\033[91m Potez nije validan!\033[0m")

        else:
            print("Nemate moguci potez!")
            promeni_igraca(trenutni_igrac)

