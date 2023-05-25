a = int(input('Nhap a cua pt ax+b=0 : '))
b = int(input('Nhap b cua pt ax+b=0 : '))

if not a:
    if not b:
        print('Phuong trinh vo so nghiem')
    else:
        print('Phuong trinh vo nghiem')
else:
    print('Phuong trinh co nghiem la ',-b/a)