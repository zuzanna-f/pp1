a=int(input("Podaj limit prędkości (km/h): "))
b=int(input("Podaj prędkość pojazdu (km/h): "))

c=b-a

if c>0 and c<=10:
    mandat=5*c

elif c>10:
    mandat=15*(c-10) + 50
    
print("Mandat (zł): ", mandat)    
    
    