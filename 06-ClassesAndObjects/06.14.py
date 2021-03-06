class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        self.channels = []
        
    def on(self):
        self.is_on = True
        
    def off(self):
        self.is_on = False
        
    def set_channel(self, new_channel_no):
        self.channel_no = new_channel_no
        
    def set_channels(self, channels_list):
        self.channels = channels_list
        
    def show_channels(self):
        if self.channels==[]:
            print("Telewizor niezaprogramowany, brak dostępnych kanałów")
        
        else:
            print("LISTA KANAŁÓW TV")
            i=1
            for x in self.channels:
                print(f'{i}. {x}')
                i+=1
        
    def show_status(self):
        if self.is_on==True and self.channel_no <= len(self.channels):
            print(f'Telewizor jest załączony, kanał {self.channel_no} ({self.channels[self.channel_no - 1]})')
        
        if self.is_on==True and self.channel_no > len(self.channels):
            print(f'Telewizor jest załączony, kanał {self.channel_no}')
            
        if self.is_on == False:
            print("Telewizor nie jest załączony")

t = TV()
t.on()
t.set_channels(['TVP1', 'TVP2', 'Polsat', 'TVN', 'Filmbox'])
t.set_channel(4)
t.show_status()

