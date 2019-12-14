with open('shoppinglist.txt','a') as file:
    produkt = input("Podaj produkt: ")
    file.write('\n')
    file.write(produkt)