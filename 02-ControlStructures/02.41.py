x=1
tablica=[]
while x!=0:
    x=int(input("Podaj liczbę: "))
    tablica.append(x)
    
a=len(tablica)
b=sum(tablica)
c=b/a

print(f"REZULTAT: Liczb={a}, Suma={b}, Średnia={c}")
  

