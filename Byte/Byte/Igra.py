from Validnost import *
from Inicijalizacija import *
from Interfejs import *
from Pomocne_funkcije import *
from potez import *



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

    #tabla na kojoj se igra
    tabla = inicijalizacija_matrice(n)
    inicijalizacija_stanja(tabla, n)
    stampaj_tabelu(tabla)

    igrac_x = 0 #Pamti se broj stekova osvojenih
    igrac_o = 0
    igrac_koji_igra = starting_player   #igrac koji igra je prvo onaj sto prvi igra...sokiran
    while True:
        poz_x = input("Unesi slovo reda: ").lower()
        poz_y = int(input("Unesi broj kolone: "))
        pravac = input("Unesi pravac kretanja: ")



        if validan_potez(tabla, prevedi_slovo_u_broj(poz_x), poz_y, pravac):
            # moram da prenesem figuru, X / O u igraj potez
            igraj_potez(tabla, poz_x, poz_y, pravac)
            print("Potez odigran!!")
            stampaj_tabelu(tabla)
        else:
            break