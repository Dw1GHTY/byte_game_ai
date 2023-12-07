from Validnost import *
from Inicijalizacija import *
from Interfejs import *
from Pomocne_funkcije import *

def igraj_potez(mat, poz_x, poz_y, pravac):
    poz_x = prevedi_slovo_u_broj(poz_x)
    poz_y -= 1
    return validan_potez(mat, poz_x, poz_y, pravac)

def kraj_igre(igrac_x, igrac_y):
    if igrac_x == 2 or igrac_y == 2:
        return True
    return False
#Ukoliko bilo ko od igraca osvoji tacno 2 steka, on je pobednik

def start_game():
    n = 0
    while True:
        try:
            n = int(input("Unesite dimenziju table (8): "))
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
            starting_player_input = input("Ko prvi igra, X ili O? ").upper()
            if starting_player_input in ['X', 'O']:
                starting_player = starting_player_input
                break
            else:
                print("Nevažeći unos. Molimo unesite X ili O.")
        except ValueError:
            print("Nevažeći unos. Molimo unesite broj.")

    tabla = inicijalizacija_matrice(n)
    inicijalizacija_stanja(tabla, n)

    irgac_x = 0 #Pamti se broj stekova osvojenih
    igrac_o = 0
    while True:
        poz_x = input("Unesi slovo reda: ").lower()
        poz_y = int(input("Unesi broj kolone: "))
        pravac = input("Unesi pravac kretanja: ")

        if igraj_potez(tabla, poz_x, poz_y, pravac) == False:
            break
        else:
            print("Potez odigran!!")
    stampaj_tabelu(tabla)