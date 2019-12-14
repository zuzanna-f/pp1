def fib(n):
    if n==0:
        return 0
    
    if n==1 or n==2:
        return 1
    
    if n>2:
        return fib(n-1) + fib(n-2)
    
    
for x in range(20):
    print(fib(x))