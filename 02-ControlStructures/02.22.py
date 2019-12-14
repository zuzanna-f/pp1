tablica = [15, 8, 31, 47, 2, 19]

suma = 0
ilość_liczb = 0

for x in tablica:
    if x % 2 == 1:
        suma += x
        ilość_liczb += 1
        
print(suma / ilość_liczb)