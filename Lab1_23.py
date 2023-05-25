a = int(input('Nhap a cua pt ax^2+bx+c=0 : '))
b = int(input('Nhap b cua pt ax^2+bx+c=0 : '))
c = int(input('Nhap c cua pt ax^2+bx+c=0 : '))

delta = (b**2) - (4*a*c)

if delta<0:
    print('Phuong trinh vo nghiem')
elif not delta:
    print('Phuong trinh co nghiem kep x1=x2= ',-b/(2*a))
else:
    print('Phuong trinh co hai nghiem phan biet')
    print('x1 = ',((-(b)+(delta**(1/2)))/(2*a)))
    print('x2 = ',((-(b)-(delta**(1/2)))/(2*a)))