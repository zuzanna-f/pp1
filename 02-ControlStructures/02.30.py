PIN = "0805"

for x in range(3):
    y = str(input("Podaj kod PIN: "))
    
    if y == PIN:
        print("Kod PIN jest poprawny.")
        break
    
    if y != PIN:
        print("Kod PIN jest niepoprawny.")
        
if x==2:
    print("Karta płatnicza zostaje zablokowana.")        

    
  
        
        
           
        
    
       

    
    


      