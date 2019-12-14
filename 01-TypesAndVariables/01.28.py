print("Rzut sześciościenną kostką do gry")

print("\n")

import random

print("Liczba oczek")
rzut1 = random.randint(1, 6)
print("pierwszy rzut:", rzut1)

rzut2 = random.randint(1, 6)
print("drugi rzut:", rzut2)

rzut3 = random.randint(1, 6)
print("trzeci rzut:", rzut3)

print("\n")

suma = rzut1 + rzut2 + rzut3
print("Suma wyrzuconych oczek:", suma)