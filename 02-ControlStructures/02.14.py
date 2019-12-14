x = int(input("Podaj wiek psa w ludzkich latach: "))

if x == 1:
    print("Wiek psa w psich latach to 10,5 roku")
    
elif x == 2:
    print("Wiek psa w psich latach to 21 lat")
    
elif x > 2:
    print(f"Wiek psa w psich latach to {21 + (x-2)*4} lata")
    