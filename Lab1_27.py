import  math
h = input('Nhap hinh: ')
if h == 'n':
    print('Tinh P va S cua hinh chu nhat')
    a = int(input('Nhap chieu dai: '))
    b = int(input('Nhap chieu rong: '))
    print('Chu vi hinh chu nhat = ', (a+b)*2)
    print('Dien tich hinh chu nhat = ', a*b)
elif h == 'v':
    print('Tinh P va S cua hinh vuong')
    a = int(input('Nhap canh: '))
    print('Chu vi hinh vuong = ', a*4)
    print('Dien tich hinh vuong = ', a**2)
else:
    print('Tinh P va S cua hinh tron')
    r = int(input('Nhap ban kinh: '))
    P = (r * 2) * math.pi
    S = (r ** 2) * math.pi
    print('Chu vi hinh tron = ', P)
    print('Dien tich hinh tron = ', S)