while True:
    n = int(input('Nhập N: '))
    x = int(input('Nhập x: '))
    if n<=0 or x<=0:
        print('Nhap lai')
    else:
        tmp=x
        temp=0
        for i in range(2,n+1):
            for j in range(1,i+1):
                temp+=j
            tmp += ((x ** i) / temp)
        print('S(n) =',tmp)
        break