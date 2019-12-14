N=int(input("ilość początkowych liczb pierwszych N = "))

for val in range(N):
    if val>1:
        for n in range(2,val):
            if (val%n)==0:
                break          
            
        else:
            print(val)
    
    