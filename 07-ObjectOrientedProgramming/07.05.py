class Music:

    def __init__(self, wykonawca, utwor, album, rok):
        self.wykonawca = wykonawca
        self.utwor = utwor
        self.album = album
        self.rok = rok
    
    
    def __str__(self):
        return "Wykonawca: " + self.wykonawca + '\n'+ "Utwór: " + self.utwor + '\n' + "Album: " + self.album + '\n' + "Rok: " + self.rok
    
     
    
    
u1 = Music('Dawid Podsiadło', 'Nie ma fal', 'Małomiasteczkowy', '2018')
print(u1)
