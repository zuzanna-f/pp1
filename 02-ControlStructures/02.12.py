print("Sprawdzenie, czy któraś z wprowadzonych liczb posiada wartość ujemną")

print("\n")

x = float(input("Wpisz pierwszą liczbę: "))
y = float(input("Wpisz drugą liczbę: "))

if x < 0 or y < 0:
    print("Co najmniej jedna liczba posiada wartość ujemną")
else:
    print("Żadna z tych liczb nie posiada wartości ujemnej")
    
          