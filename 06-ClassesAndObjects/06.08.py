class University:
    
    # konstruktor obiektu (metoda __init__)
    def __init__(self):
        # cechy obiektu (pola)
        self.name = 'UEK'
        self.fullname = 'Uniwersytet Ekonomiczny w Krakowie'
        
        # zachowania obiektu (metody)
    def print_name(self):
        print(self.name)
        
    def set_name(self, new_name):
        self.name = new_name
        
    
              
u2 = University()
u2.set_name('AGH')
u2.print_name()
