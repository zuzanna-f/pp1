class TV:
    def __init__(self):
        self.is_on = False
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def show_status(self):
        if self.is_on==True:
            print("Telewizor jest załączony")
            
        else:
            print("Telewizor nie jest załączony")
        
        
#stworzenie telewizora i wyświetlenie jego stanu
t = TV()
t.show_status()

#załączenie telewizora
t.on()
t.show_status()

#wyłączenie telewizroa
t.off()
t.show_status()