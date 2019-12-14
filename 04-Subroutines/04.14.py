def wystepuje(liczba, tablica):
    print("Liczba: ", liczba)
    print("Tablica: ", tablica)
    
    for x in tablica:
        if liczba==x:
            print("Rezultat: Podana liczba występuje w tablicy")
            break
        
    if liczba!=x:
        print("Rezultat: Podana liczba nie występuje w tablicy")
            
    


liczba = 23
tablica = [15, 38, 7, 23, 14]

wystepuje(liczba, tablica)