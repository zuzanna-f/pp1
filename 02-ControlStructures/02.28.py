a = int(input("a="))
b = int(input("b="))

for x in range(1, a+1):
    if x==1 or x==a:
        print(b * '*')
        
    else:
        print('*' + (b-2) * ' ' + '*')
