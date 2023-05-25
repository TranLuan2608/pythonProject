my = input('Nhap thang nam(mm yy): ')
m = int(my.split()[0])
y = int(my.split()[1])

if (y%4==0 and y%100!=0) or (y%400==0):
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        print('Thang ',m,' co 31 ngay')
    elif m==2:
        print('Thang ',m,' co 29 ngay')
    else:
        print('Thang ', m, ' co 30 ngay')
else:
    if m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
        print('Thang ',m,' co 31 ngay')
    elif m==2:
        print('Thang ',m,' co 28 ngay')
    else:
        print('Thang ', m, ' co 30 ngay')