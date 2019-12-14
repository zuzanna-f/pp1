def spr(n, x, y):
    
    if n >= x and n <= y:
        print(f"Liczba {n} mieści się w zakresie <{x}, {y}>")
        
    else:
        print(f"Liczba {n} nie mieści się w zakresie <{x}, {y}>")
    
    
spr(24, 20, 100)


