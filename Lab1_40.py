while True:
    n = int(input('Nhập N: '))
    if n<=0 :
        print('Nhap lai')
    else:
        tmp=0
        for i in range(3,2*n+1,2):
            tmp+=(1/i)
        print('S(n) =',tmp)
        break