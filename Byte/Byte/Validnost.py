def validan_potez(mat, poz_x, poz_y, pravac, poz_steka, igrac):
    if not okvir_table(poz_x, poz_y, 8):
        return False

    if len(mat[poz_x][poz_y]) < poz_steka:
        return False

    if igrac == "X" and mat[poz_x][poz_y][poz_steka - 1] == "O":
        return False

    if igrac == "O" and mat[poz_x][poz_y][poz_steka - 1] == "X":
        return False

    dest_stack = tuple()
    if pravac == "GL":
        dest_stack = (poz_x - 1, poz_y - 1)
    elif pravac == "GD":
        dest_stack = (poz_x - 1, poz_y + 1)
    elif pravac == "DL":
        dest_stack = (poz_x + 1, poz_y - 1)
    elif pravac == "DD":
        dest_stack = (poz_x + 1, poz_y + 1)

    if not okvir_table(dest_stack[0], dest_stack[1], 8):
        return False

    if not prazna_pozicija(mat, dest_stack[0], dest_stack[1]):
        len_src = len(mat[poz_x][poz_y]) - poz_steka + 1
        if len_src + len(mat[dest_stack[0]][dest_stack[1]]) > 8:
            return False
        if len(mat[dest_stack[0]][dest_stack[1]]) < poz_steka:
            return False
        return True

    if not prazna_susedna_polja(mat, poz_x, poz_y):
        return False

    # Sva susedna polja su prazna i sad treba da se proveri gde se nalazi najblizi stek
    niz_validnih_smerova = najbliza_polja(mat, poz_x, poz_y)
    for smer in niz_validnih_smerova:
        if (dest_stack[0] - poz_x, dest_stack[1] - poz_y) == smer:
            return True

    return False
def okvir_table(row, col, n):
    return 0 <= row < n and 0 <= col < n
def prazna_pozicija(mat, row, col):
    return True if len(mat[row][col]) == 0 else False
def prazna_susedna_polja(mat, x, y):
    # Vraca True ako postoji minimum jedno susedno polje koje nije prazno
    niz = [(x - 1, y - 1), (x + 1, y + 1), (x - 1, y + 1), (x + 1, y - 1)]
    for poz in niz:
        if okvir_table(poz[0], poz[1], 8):
            if not prazna_pozicija(mat, poz[0], poz[1]):
                return False

    return True
def najbliza_polja(mat, startni_red, startna_kolona):
    red = [(startni_red, startna_kolona, 0, (0, 0))]
    poseteni = set()

    najbliza = []  # cuva skup smerova koji su dozvoljeni
    min_broj_skokova = float('inf')

    while red:
        trenutni_red, trenutna_kolona, broj_skokova, poc_smer = red.pop(0)
        poseteni.add((trenutni_red, trenutna_kolona))

        if len(mat[trenutni_red][trenutna_kolona]) != 0:
            if broj_skokova < min_broj_skokova:
                najbliza = [poc_smer]
                min_broj_skokova = broj_skokova
            elif broj_skokova == min_broj_skokova:
                najbliza.append(poc_smer)

        smerovi = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for smer in smerovi:
            novo_polje = (trenutni_red + smer[0], trenutna_kolona + smer[1])
            zapisani_smer = tuple()
            if poc_smer == (0, 0):
                zapisani_smer = smer
            else:
                zapisani_smer = poc_smer
            # Zapisani smer sluzi kako bi se zapamtio smer u odnosu na pocetnu poziciju koji dovodi do najblizeg polja
            if okvir_table(novo_polje[0], novo_polje[1], 8) and novo_polje not in poseteni:
                red.append((novo_polje[0], novo_polje[1], broj_skokova + 1, zapisani_smer))

    return najbliza
