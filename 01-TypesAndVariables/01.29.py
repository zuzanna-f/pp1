print("Gra z komputerem")

print("\n")

import random
los = random.randint(1, 6)

liczba = int(input("Podaj, ile oczek kostki wyrzucił komputer: "))

print("Komputer wyrzucił:", los)

if liczba == los:
    print("Zgadłeś: True")
    
else: print("Zgadłeś: False")