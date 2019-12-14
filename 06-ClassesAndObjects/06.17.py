class Fraction:
    def __init__(self, licznik, mianownik):
        self.licznik = licznik
        self.mianownik = mianownik
                          
    def create_fraction(self):
        self.ulamek = f'{self.licznik}/{self.mianownik}'
        
    def simplify_fraction(self):
        import math
        nwd = math.gcd(self.licznik, self.mianownik)
        self.licznik = int(self.licznik / nwd)
        self.mianownik = int(self.mianownik / nwd)
        self.ulamek = f'{self.licznik}/{self.mianownik}'
    
    def show_fraction(self):  
        print(self.ulamek)
    
                 
u = Fraction(1, 2)
u.create_fraction()
u.show_fraction()

u2 = Fraction(12, 21)
u2.create_fraction()
u2.show_fraction()
u2.simplify_fraction()
u2.show_fraction()


