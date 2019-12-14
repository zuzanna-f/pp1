kwota=int(input("Podaj kwotę w zł: "))

a=kwota%5

if a==0:
    b=kwota/5
    d=0
    e=0

else:
    b=kwota//5
    c=(kwota-b*5)%2
    
    if c==0:
        d=(kwota-b*5)/2
        e=0
        
    else:
        d=(kwota-b*5)//2
        e=kwota-b*5-d*2
    
       
print(f'Kwota {kwota} zł w monetach:')
print(f'5 zł - {int(b)} szt')
print(f'2 zł - {int(d)} szt')
print(f'1 zł - {int(e)} szt')