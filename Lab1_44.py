while True:
    n = int(input('Nhập N: '))
    if n<=0 :
        print('Nhap lai')
    else:
        tmp=0
        for i in range(1,2*n+3,2):
           tmp+=(i/(i+1))
        print('S(n) =',tmp)
        break