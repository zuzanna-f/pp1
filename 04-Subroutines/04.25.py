def jestImie(imie,imiona):
    
    print("Imiona: ", imiona)
    print("Imię: ", imie)
    
    for x in imiona:
        if imie in imiona:
            print("Rezultat: imię zawarte jest w wykazie imion")
            break
                    
    if imie not in imiona:
        print("Rezultat: imię nie jest zawarte w wykazie imion")
        

imiona = ["Janek", "Ania", "Wojtek", "Zosia"]
imie = "Wojtek"
jestImie(imie, imiona)
