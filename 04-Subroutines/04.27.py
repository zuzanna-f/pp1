import re

tekst = 'Nam strzelać nie kazano. Wstąpiłem na działo. I spojrzałem na pole, dwieście armat grzmiało. Artyleryji ruskiej ciągną się szeregi, Prosto, długo, daleko, jako morza brzegi.'
samogłoski = re.findall('[eyuioa]', tekst)


tab_sam = ["e", "y", "u", "i", "o", "a"]

for y in tab_sam:
    suma=0
    for x in samogłoski:
        if x==y:
            suma+=1

    print(f'{y} = {round((suma/len(samogłoski))*100, 2)}%')