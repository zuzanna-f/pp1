import statistics
class Statystyka:
    def __init__(self, tablica):
        self.tablica = tablica
        
    def dodaj_liczbe(self):
        liczba = input("Podaj liczbę która ma być dodana do tablicy: ")
        self.tablica.append(int(liczba))
        
    def wyswietl_tablice(self):
        print("liczby: ", end='')
        for x in self.tablica:
            print(x, end=' ')
        print()

    def maksimum(self):
        self.maksimum = max(self.tablica)        
        
    def minimum(self):
        self.minimum = min(self.tablica)
                
    def srednia(self):
        self.srednia = statistics.mean(self.tablica)
          
    def mediana(self):
        self.mediana = statistics.median(self.tablica)
        
    def wyswietl(self):
        print(f'maksimum: {self.maksimum}')
        print(f'minimum: {self.minimum}')
        print(f'srednia arytmetyczna liczb: {self.srednia}')
        print(f'mediana liczb: {self.mediana}')    



z = Statystyka([12, 37, 6, 9, 17])
z.dodaj_liczbe()
z.dodaj_liczbe()
z.dodaj_liczbe()
z.wyswietl_tablice()
z.maksimum()
z.minimum()
z.srednia()
z.mediana()
z.wyswietl()
        