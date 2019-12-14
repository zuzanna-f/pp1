def transpozycja(macierz):
    
    macierz2=[[0,0,0],[0,0,0], [0,0,0]]
    for x in range(3):
        for y in range(3):
            macierz2[x][y]=macierz[y][x]
     
    return macierz2 



macierz = [[1, 2, 0], [0, 0, 3], [5, 1, 1]]


print(macierz)
print(transpozycja(macierz))

