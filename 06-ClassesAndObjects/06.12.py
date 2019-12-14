class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def show_status(self):
        if self.is_on==True:
            print("Telewizor jest załączony, kanał", self.channel_no)
            
        else:
            print("Telewizor nie jest załączony")
            
t = TV()
t.show_status()
t.on()
t.show_status()
t.set_channel(5)
t.show_status()
t.off()
t.show_status()
