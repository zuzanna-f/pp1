def rzucKostka():
    import random
    return random.randint(1, 6)

      
print("Wyrzucone oczka: ", end='')

suma = 0
for x in range(3):
    liczba = (rzucKostka())
    print(liczba, end=' ')

    suma = suma + liczba

print()
print("Suma oczek: ", suma)