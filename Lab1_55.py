def chuViHCN(a,b):
    """Tinh chu vi hinh chu nhat"""
    return (a+b)*2
def dienTichHCN(a,b):
    """Tinh dien tich hinh chu nhat"""
    return a*b
def drawHCN(a,b):
    """Ve hinh chu nhat"""
    for i in range(a):
        print('*',end=' ')
        for j in range(1,b-1):
            if i==0 or i==a-1:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print('*')

print(drawHCN.__doc__)
A = int(input('a = '))
B = int(input('b = '))
drawHCN(A,B)