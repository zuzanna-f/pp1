with open('universities.txt', 'r') as file:
    
    tablica = []
    
    for line in file:
        tablica.append(str(line))
        
    tablica.sort()
    print(tablica)
    
with open('universities.txt', 'w') as file:
    
    for line in tablica:
        file.write(line)