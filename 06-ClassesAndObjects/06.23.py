class Kontakt:
    
    def __init__(self, nazwa, email, telefon):
        self.nazwa = nazwa
        self.email = email
        self.telefon = telefon


class ListaKontaktów:
    
    def __init__(self):
        self.tablica = []
        
    def dodaj(self, kontakt):
        self.tablica.append(kontakt)
        
    def wyswietl(self):
        for x in self.tablica:
             print('{:15} {:15} {:10}'.format(x.nazwa, x.email, x.telefon))
        
        
k1 = Kontakt('Kowalski Jan', 'jank@onet.pl', '555234000')
k2 = Kontakt('Borek Patrycja', 'bp@o2.pl', '232000199')
k3 = Kontakt('Maj Piotr', 'maj@google.pl', '222999100')
k4 = Kontakt('Adamczyk Anna', 'ada@poczta.pl', '100200300')

lista = ListaKontaktów()
lista.dodaj(k1)
lista.dodaj(k2)
lista.dodaj(k3)
lista.dodaj(k4)
lista.wyswietl()