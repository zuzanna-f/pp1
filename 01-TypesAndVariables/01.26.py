print("Obliczanie wskaźnika masy ciała BMI")

print("\n")

h = float(input("Podaj wzrost w cm: "))
m = float(input("Podaj wagę w kg: "))

BMI = m / (h * 0.01) ** 2

if BMI < 18.5:
    print(f"Wskaźnik BMI: {round(BMI, 2)} (niedowaga)")
    
if 18.5 < BMI < 24.99:
    print(f"Wskaźnik BMI: {round(BMI, 2)} (waga prawidłowa)")
        
if BMI >= 25:
    print(f"Wskaźnik BMI: {round(BMI, 2)} (nadwaga)")


