while True:
    n = int(input('Nhập N: '))
    if n<0 :
        print('Nhap lai')
    else:
        tmp=0
        for i in range(1,n+1):
            if n%i==0:
                tmp+=1
        if tmp==2:
            print(n,'la so nguyen to')
            exit()
        else:
            print(n,'khong phai la so nguyen to')
            exit()