while True:
    n = int(input('Nhập N: '))
    if n<=0 :
        print('Nhap lai')
    else:
        tmp=1
        for i in range(2,2*n+2):
           tmp+=(1/i)
        print('S(n) =',tmp)
        break