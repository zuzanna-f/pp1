import re

komunikat = 'wtorek - 23C, środa - 17C, czwartek 25C'
cyfry = re.findall('\d{2}', komunikat)

i = 0
for i in range(0, len(cyfry)):
    cyfry[i] = int(cyfry[i])
    
print(sum(cyfry)/len(cyfry))
