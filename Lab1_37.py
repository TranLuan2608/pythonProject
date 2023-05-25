while True:
    n = int(input('Nhập N: '))
    if n<=0 :
        print('Nhap lai')
    else:
        tmp=0
        for i in range(2,n+1,2):
           tmp+=i
        print('S=',tmp)
        break