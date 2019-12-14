print("Wyznaczanie temperatury wyrażonej w stopniach Celsjusza w stopniach Fahrenheita oraz Kelvina")
print("\n")
C = float(input("Temperatura w stopniach Celsjusza: "))
F = (C * 1.8) + 32.0
print("Temperatura w stopniach Fahrenheita:", round(F, 2))
K = C + 273.15
print("Temperatura w stopniach Kelvina:", round(K, 2))

