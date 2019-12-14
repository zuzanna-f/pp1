with open('students.txt', 'r') as file:
    
    file.readline()
    
    for line in file:
        temp = line.split(',')
        
        if int(temp[2]) < 30:
            print(temp[0], temp[1], temp[4], end='')
            
            