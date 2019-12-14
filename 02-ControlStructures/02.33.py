tablica = ["zero", "jeden", "dwa", "trzy", "cztery", "pięć", "sześć", "siedem", "osiem", "dziewięć"]
liczba = "38227"

print("38227 - ", end="")
i = 0
while i < 5:
    c = int(liczba[i])
    print(tablica[c], end=" ")
    i += 1
    