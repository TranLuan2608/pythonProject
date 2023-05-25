a = int(input('Nhap so a: '))
b = int(input('Nhap so b: '))
c = int(input('Nhap so c: '))
d = int(input('Nhap so d: '))

max = a
if b>max and b>c and b>d:
    print('Max = ',b)
elif c>max and c>b and c>d:
    print('Max = ',c)
elif d>max and d>c and d>b:
    print('Max = ',d)
else:
    print('Max = ',max)
