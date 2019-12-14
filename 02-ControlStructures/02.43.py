a=int(input("Podaj pierwszą liczbę: "))
b=int(input("Podaj drugą liczbę: "))
c=int(input("Podaj trzecią liczbę: "))

liczby=[a, b, c]
liczby.sort()

print("Liczby w kolejności rosnącej: ", end='')
for x in liczby:
    print(x, end=' ')





