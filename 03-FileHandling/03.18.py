with open('numbers.txt', 'r') as file:
    
    tablica = []
    
    for line in file:
        tablica.append(int(line))
    
    tablica.sort()
    
    for x in range(len(tablica)):
        print(tablica[x], end=" ")
    
    
    
    
    
    
   