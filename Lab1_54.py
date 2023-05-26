def fibo(n):
    """In ra n phần tử của dãy Fibonacy"""
    a,b = 0,1;
    while a<n:
        print(a, end =' ')
        a,b = b,a+b

print(fibo.__doc__)
A = int(input('n = '))
fibo(A)