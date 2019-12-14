tablica = [1,2,3,4,5,6,7,8]

liczby_parzyste = filter(lambda a: a%2==0, tablica)

for x in liczby_parzyste:
    print(x)