import random

tablica=[]
for x in range(100):
    x=random.randint(1,6)
    tablica.append(x)

print(f"Szóstka: {tablica.count(6)}")
print(f"Piątka: {tablica.count(5)}")
print(f"Czwórka: {tablica.count(4)}")
print(f"Trójka: {tablica.count(3)}")
print(f"Dwójka: {tablica.count(2)}")
print(f"Jedynka: {tablica.count(1)}")