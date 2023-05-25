n = int(input('Nhap so co 4 chu so: '))

a = n//1000
b = (n//100)%10
c = (n%100)//10
d = n%10
print('Tong so nut = ',a+b+c+d)