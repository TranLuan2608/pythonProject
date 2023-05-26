def a(n):
    """S = 1+2+3+4+...+n"""
    tmp=0
    for i in range(1,n+1):
        tmp+=i
    return tmp

def b(n):
    """S = 12+22+32+42+...+n2"""
    tmp=0
    for i in range(1,n+1):
        tmp+=(i*10+2)
    return tmp
def c(n):
    """S = 1+1/2+1/2+1/3+1/4+...+1/n"""
    tmp=0
    for i in range(1,n+1):
        tmp+=(1/i)
    return tmp

def d(n):
    """S = 1!+2!+3!+...+n!"""
    tmp=0
    for i in range(1,n+1):
        tmp+=(a(i))
    return tmp

def e(n):
    """S = 1*2*3*...*n"""
    tmp=1
    for i in range(2,n+1):
        tmp*=i
    return tmp
print(e.__doc__)
A = int(input('n = '))
print(e(A))
