
a=0
b=1
print(a, b, end=' ')

for x in range(49):
    c=a+b
    print(c, end=' ')
    a=b
    b=c
    
    