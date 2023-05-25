a = int(input('Nhap so a: '))
b = int(input('Nhap so b: '))
c = int(input('Nhap so c: '))
d = int(input('Nhap so d: '))

min = a
if b<min and b<c and b<d:
    print('Min = ',b)
elif c<min and c<b and c<d:
    print('Min = ',c)
elif d<min and d<c and d<b:
    print('Min = ',d)
else:
    print('Min = ',min)
