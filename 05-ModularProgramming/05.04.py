#a
import math
x = 3.7
y = 4

#a
print("a.", end=' ')
sqrtX = math.sqrt(x)
print(f'Pierwiastek kwadratowy z {x} wynosi {sqrtX}')

#b
print("b.", end=' ')
powX=math.pow(x,y)
print(f'{x} podniesione do potęgi {y} wynosi {powX}')

#c
print("c.", end=' ')
pierwiastekX=math.pow(x,1/y)
print(f'Pierwiastek {y}-tego stopnia z {x} wynosi {pierwiastekX}')

#d
print("d.", end=' ')
pole=math.pi*math.sqrt(y)
print(f'Pole koła o promieniu {y} wynosi {pole}')

#e
print("e.", end=' ')
factorialY=math.factorial(y)
print(f'Silnia {y} wynosi {factorialY}')

#f
print("f.", end=' ')
floorX=math.floor(x)
print(f'Największa możliwa liczba całkowita, mniejsza bądź równa {x} wynosi {floorX}')
