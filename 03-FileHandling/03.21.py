with open('numbersinrows.txt', 'r') as file:
    
    ile = 0
    suma = 0
    
    for line in file:
        temp = []
        temp = line.split(',')
        
    
        for i in range(len(temp)):
            temp[i] = int(temp[i])
            
            suma = suma + temp[i]
            ile = ile + 1

print("Suma liczb: ", suma)
print("Ilość licz: ", ile)
        