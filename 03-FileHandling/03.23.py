import re
with open('land.txt', 'r') as file:
    
    suma = 0
    for line in file:
        cyfry = re.findall('[0-9]', line)
         
        for x in range(len(cyfry)):
            cyfry[x] = int(cyfry[x])
             
            suma = suma + cyfry[x]

print(suma)