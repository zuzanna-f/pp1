def tablica(n):
    
    tab2=[]
    d=len(tab)
    
    for i in range(d):
       powt=False
       for j in range(d):
           if tab[i]==tab[j] and i!=j:
               powt=True
               break
            
       if powt==False:
           tab2.append(tab[i])
           
     
    return tab2  
     
    
tab = [3, 5, 2, 5, 6, 7, 5, 3]
print(tablica(tab))