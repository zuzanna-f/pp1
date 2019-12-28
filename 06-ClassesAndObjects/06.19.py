class Banking_account:
    def __init__(self, numer):
        self.numer = numer
        self.saldo = 0
        
    def show_status(self):
        print(f'Rachunek nr: {self.numer}')
        print(f'Saldo: {self.saldo} zł')
        
    def pay_in(self, deposit):
        self.saldo = self.saldo + deposit
        
    def withdraw(self, withdrawal):
        if self.saldo >= withdrawal:
            self.saldo = self.saldo - withdrawal
            
        else:
            print("Niewystarczająca ilość środków na rachunku")
            
            
r = Banking_account("12 3456 5555 9090 1111 0000 7722")
#r.show_status()
r.pay_in(25.30)
#r.show_status()
#r.withdraw(31.70)
#r.show_status()
r.withdraw(14)
r.show_status()