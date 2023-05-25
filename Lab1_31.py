while True:
    a = int(input('Nhập a(a>0): '))
    b = int(input('Nhập b(b>0): '))
    c = int(input('Nhập c(c>0): '))
    if a<0 or b<0 or c<0:
        print('Nhap lai')
    else:
        if a+b>c and a+c>b and b+c>a:
            if a==b and b==c:
                print('Tam giac deu')
                break
            elif( a==b and b!=c) or (b==c and a!=b):
                print('Tam giac can')
                break
            elif (a**2+b**2==c**2) or (b**2+c**2==a**2) or (a**2+c**2==b**2):
                print('Tam giac vuong')
                break
            else:
                print('Tam giac thuong')
                break
        else:
            print('Khong phai tam giac')
            break