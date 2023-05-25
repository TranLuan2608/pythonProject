n = input("Nhap gio theo dinh dang hh:mm:ss: ")

h = n.split(':')
m = n.split(':')
s = n.split(':')
tong = (int(h[0])*60*60) + (int(m[1])*60) + int(s[2])

print('Tong so giay =',tong)



