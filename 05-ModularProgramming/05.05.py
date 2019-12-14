wynagrodzenia=[21600, 4350, 3920, 5590, 3250, 4010]

import statistics

#a
print("a.", end=' ')
mean=statistics.mean(wynagrodzenia)
print(f'Średnia wynagrodzeń wynosi {mean}')

#b
print("b.", end=' ')
median=statistics.median(wynagrodzenia)
print(f'Mediana wynagrodzeń wynosi {median}')

#c
print("c.", end=' ')
odchylenie=statistics.pstdev(wynagrodzenia)
print(f'Odchylenie standardowe wynagrodzeń wynosi {odchylenie}')