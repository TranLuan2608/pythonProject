while True:
    n = int(input('Nhập n(n>0): '))
    if n<0:
        print('Nhap lai n')
    else:
        tmp=0
        while True:
            if not n:
                break
            else:
                tmp+=(n%10)
                n = n//10
        print('Tong = ',tmp)
        break

