def los():
    import random
    return random.randint(1, 50)


p=0
n=0
for x in range (1001):
    if los()%2==0:
        p += 1
        
    else:
        n += 1
        

print("Dla 1000 liczb losowych z przedziału <1,50>:")
print(f"Liczby parzyste: {(p/1000)*100}%")
print(f"Liczby nieparzyste: {(n/1000)*100}%")