class Plane:
    
    def __init__(self, numer):
        self.altitude = 0
        self.numer = numer
        
    def start(self, altitude):
        self.altitude = altitude
        
    def status(self):
        print(f'Tu {self.numer}, moja wysokość lotu to {self.altitude}m')
    
    def new_altitude(self, new_altitude):
        if new_altitude >= 300 and new_altitude <= 11000:
           self.altitude =new_altitude
            
        else:
            print("Wysokość poza dozwolonym zakresem")
            
    def land(self):
        if self.altitude < 500:
            self.altitude = 0
            
        else:
            print("Zbyt duża wysokość dla lądowania. Obniż lot")         
            

s = Plane("LOT881")
s.start(1500)
#s.status()
s.new_altitude(8900)
#s.status()
#s.new_altitude(200)
#s.status()
#s.land()
s.new_altitude(400)
s.land()
s.status()
