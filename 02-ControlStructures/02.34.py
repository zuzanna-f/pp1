pesel = "93021707231"

print(f"Podaj pesel: {pesel}")

print("Płeć: ", end="")
if int(pesel[-2]) % 2 == 1:
    print("mężczyzna")
    
else:
    print("kobieta")

print("Wiek: ", 2018 - 1900 - int(pesel[0:2])) 