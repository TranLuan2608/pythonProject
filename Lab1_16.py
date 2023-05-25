n = input("Nhap gio theo dinh dang hps: ")

h = n.split('h')[0]
m = n.split('p')
p = m[0].split('h')[1]
s = m[1].split('s')[0]

tong = (int(h)*60*60) + (int(p)*60) + int(s)

print(tong, 'giây')