print("Wyznaczanie pierwiastków równania kwadratowego postaci ax2 + bx + c = 0")

print("\n")

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

delta = b**2 - 4*a*c

if delta > 0:
    x1 = (-b - delta**0.5)/(2*a)
    x2 = (-b + delta**0.5)/(2*a)
    print("x1 = ", x1)
    print("x2 = ", x2)
    
elif delta == 0:
    x0 = -b/(2*a)
    print("x0 = ", x0)
    
elif delta < 0:
    print("Brak miejsc zerowych")