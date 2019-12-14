with open('numbers.txt', 'r') as file:
        
        for line in file:
            if int(line)%2 == 0:
                with open('evennumbers.txt', 'a') as file:
                    file.write(line)