def podatek(dochod):
    
    if dochod==5000 or dochod<5000:
        podatek = 0.17*dochod
        
    elif dochod>5000:
        podatek = 0.32*dochod
        
    print("Podatek należny: ", podatek, "zł")
    
    
    
dochod = int(input("Podaj dochód: "))
podatek(dochod)