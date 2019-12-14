liczba=int(input("Liczba: "))

print(f'{liczba}(10)=', end='')

tablica=[]

while liczba>0:
    if liczba%2==0:
        tablica.append(0)
    
    else:
        tablica.append(1)
    
    liczba=liczba//2
    

tablica.reverse()


for x in tablica:
    print(x, end='')
print('(2)')
    