tablica = [['Marek','Zelnik','zelnik@sed.pl'],['Ewa','Maj','maje@wp.pl'],['Piotr','Wyga','wygap@gop.pl']]

with open('tablica2w.txt', 'w') as file:
    
    file.write("Imie,Nazwisko,Email\n")
    
    for w in range(3):
        for k in range(3):
            file.write(str(tablica[w][k]))
            if k < 2:
                file.write(',')

        file.write("\n")
        