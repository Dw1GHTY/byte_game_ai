def inicijalizacija_matrice(n):
    mat = list()
    for i in range(n):
        row = list()
        for j in range(n):
            row.append(list())
        mat.append(row)

    return mat

def inicijalizacija_stanja(mat, n):
    for i in range(n):
        for j in range(n):
            if i == 0 or i == n - 1:
                mat[i][j] = []  # postavljeni prazan prvi i zadnji red
            else:
                if i % 2 == 0 and j % 2 == 0:
                    mat[i][j] = ['O']  # beli na parne
                elif i % 2 != 0 and j % 2 != 0:
                    mat[i][j] = ['X']  # crni na neparne