print("Obliczanie pola trójkąta dla podanych boków a, b oraz c, z wykorzystaniem wzoru Herona")
print("\n")

a = float(input("bok a: "))
b = float(input("bok b: "))
c = float(input("bok c: "))

p = 0.5 * (a + b + c)
P = (p * ((p - a) * (p - b) * (p - c))) ** 0.5

print("\n")

print(f"Pole trójkąta wynosi {P}")