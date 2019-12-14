class Dice:
    def throw(self):
        import random
        self.liczba_oczek = random.randint(1, 6)
        return self.liczba_oczek
    
k1 = Dice()
k2 = Dice()
k3 = Dice()

tablica = [k1.throw(), k2.throw(), k3.throw()]

suma=0
for x in tablica:
    suma = suma + x   
    
print("k1 = ", tablica[0])
print("k2 = ", tablica[1])
print("k3 = ", tablica[2])  
print("suma wyrzuconych oczek:", suma)
        
        
