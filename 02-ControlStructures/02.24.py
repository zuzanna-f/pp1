tablica = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy", "Teofil"]

n = tablica[0]
i=0
for x in tablica:
    
    if len(str(x)) > len(str(n)):
        n = tablica[i]
    i = i + 1
print(n)    
        
    