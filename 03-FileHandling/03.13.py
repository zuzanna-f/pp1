tablica = [32, 16, 5, 8, 24, 7]

with open('tablica10.txt', 'w') as file:
    for i in range(6):
        file.write(str(tablica[i])+'\n')