x=input("Podaj pierwszą liczbę: ")
y=input("Podaj drugą liczbę: ")
z=input("Podaj trzecią liczbę: ")

tablica=[x, y, z]
tablica.sort()

print(f"Mediana wynosi {tablica[1]}")