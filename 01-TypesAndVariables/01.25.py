print("Wyświetlanie numeru rachunku bankowego")

print("\n")

nr = int(input("Podaj nr rachunku bankowego: "))
print("Nr rachunku:", "{:,}".format(nr).replace(",", " "))
