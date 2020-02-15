#06.22

import random
class Termometr:
    
    def __init__(self):
        self.is_on = False
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
    
    def pomiar(self):
        if self.is_on == True:
            self.temperature = round(random.uniform(34.0, 42.0), 1)
            
    def wyswietl(self):
        if self.is_on == True:
            print(f'Zmierzona temperatura: {self.temperature}C', end=' ')
        
            if self.temperature >= 37.0 and self.temperature < 41.0:
                print("(gorączka)")
            
            if self.temperature >= 41.0:
                print("(Stan zagrożenia życia!!!)")
