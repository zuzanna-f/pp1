import math
print("Wyznaczanie największego wspólnego dzielnika")

print("\n")

a = int(input("liczba a: "))
b = int(input("liczba b: "))

NWD = math.gcd(a, b)

print(f"Największy wspólny dzielnik liczby {a} i {b} to {NWD}")