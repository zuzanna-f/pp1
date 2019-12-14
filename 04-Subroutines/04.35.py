def suma(n):
    if n==0:
        return 0
    
    if n>0:
        return n%10 + suma(n//10)
         
        
liczba = 1546      
print(suma(liczba))  