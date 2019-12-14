class University:
    
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
        
        # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
        
    def print_fullname(self):
        print(self.fullname)
        
    def set_name(self, new_name):
        self.name = new_name
        
    def set_fullname(self, new_fullname):
        self.fullname = new_fullname
        
    
              
u = University()
u.print_fullname()

u2 = University()
u2.set_fullname('Akademia Górniczo-Hutnicza')
u2.print_fullname()
