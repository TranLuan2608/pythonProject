while True:
    n = int(input('Nhập N: '))
    if n<=0 :
        print('Nhap lai')
    else:
        tmp=1
        for i in range(1,n+1,2):
           tmp*=i
        print('S=',tmp)
        break