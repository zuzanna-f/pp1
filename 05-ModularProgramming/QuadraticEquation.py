#05.10

import math
def wczytajWspolczynniki():
    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))
    print(f'Równanie kwadratowe postaci: {a}x2+({b})x+({c})=0')
    tablica=[a,b,c]
    return tablica


def obliczDelte(tablica):
    a=tablica[0]
    b=tablica[1]
    c=tablica[2]
    delta = b**2-4*a*c
    return delta


def obliczPierwiastki(tablica):
    a=tablica[0]
    b=tablica[1]
    c=tablica[2]
    if obliczDelte(tablica)< 0:
        tab=[]
        return tab
    if obliczDelte(tablica) == 0:
        x1 = -b / 2 * a
        tab=[x1]
        return tab
    if obliczDelte(tablica) > 0:
        x1 = (-b - math.sqrt(obliczDelte(tablica))) / (2 * a)
        x2 = (-b + math.sqrt(obliczDelte(tablica))) / (2 * a)
        tab=[x1,x2]
        return tab
    
def wyswietlPierwiastki(tab):
    if len(tab)==0:
        print("Brak pierwiastków")
        
    if len(tab)==1:
        print(f'Pierwiastek równania: x1={tab[0]}')
        
    if len(tab)==2:
        print(f'Pierwiastki równania: x1={tab[0]}, x2={tab[1]}')
   
