suma = 0
suman = 0
for x in range (1, 51):
    if x%2==0:
        suma = suma + x
    else:
        suman = suman + x
    
print("Suma liczb parzystych:", suma)
print("Suma liczb nieparzystych:", suman)   

    