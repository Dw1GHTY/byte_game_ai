def stampaj_tabelu(mat):
    niz = ["A", "B", "C", "D", "E", "F", "G", "H"]
    print("   ", end="")
    for i in range(1, 9):
        print("\033[91m", end="")
        print(i, end="")  #Crvena boja
        print("\033[0m", end="")
        print("  ", end="")
    print("")
    for i in range(0, 8):
        for j in range(2, -1, -1):
            if j == 1:
                print("\033[91m", end="")
                print(niz[i] + " ", end="")  #Crvena boja
                print("\033[0m", end="")
            else:
                print("  ", end="")
            for k in range(0, 8):
                stampaj_pomocna(i, j, k, mat)
            print("")
def stampaj_pomocna(i, j, k, mat):
  pom_niz = [0, 1, 2]
  pom_niz = list(map(lambda x: x + 3*j, pom_niz))
  if (i + k) % 2 == 0:
    for index in pom_niz:
      if len(mat[i][k]) >= index + 1:
        if mat[i][k][index] == "X":
            print("\033[94m", end="")  #Plava boja
        else:
            print("\033[92m", end="")  #Zelena boja
        print(mat[i][k][index], end="")
        print("\033[0m", end="")
      else:
        print(".", end="")
  else:
    print("   ", end="")