class Student():
    licznik = 100000
    uczelnia = "UEK Kraków"
    
    def __init__(self, imie, nazwisko, kierunek):
        self.imie = imie
        self.nazwisko = nazwisko
        self.kierunek = kierunek
        self.album = Student.licznik
        Student.licznik += 1
        
    def __str__(self):
        return f'{self.imie} {self.nazwisko} ({Student.licznik}), {self.kierunek}, {Student.uczelnia})'
    
    
u1 = Student('Wacław', 'POTOCKI', 'Informatyka Stosowana')
print(u1)

u2 = Student('Jan', 'KOWALSKI', 'Ekonomia')
print(u2)

u2 = Student('Marta', 'NOWAK', 'Prawo')
print(u2)

