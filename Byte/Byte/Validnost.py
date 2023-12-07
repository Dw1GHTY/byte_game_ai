
def validna_pozicija(row, col, n):
    return 0 <= row < n and 0 <= col < n

def prazna_pozicija(mat, row, col):
    return True if len(mat[row][col]) == 0 else False


def validan_potez(mat, poz_x, poz_y, pravac):
    if validna_pozicija(poz_x, poz_y, 8):
        if not prazna_pozicija(mat, poz_x, poz_y):
            if pravac == 'GD':
                return validna_pozicija(poz_x + 1, poz_y - 1, 8)
            elif pravac == 'GL':
                return validna_pozicija(poz_x - 1, poz_y - 1, 8)
            elif pravac == 'DL':
                return validna_pozicija(poz_x - 1, poz_y + 1, 8)
            elif pravac == 'DD':
                return validna_pozicija(poz_x + 1, poz_y + 1, 8)
            else:
                print("Nije unet validan pravac")
                return False
    return False