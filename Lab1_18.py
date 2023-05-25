a = input("Nhap gio theo dinh dang hps 1: ")
b = input("Nhap gio theo dinh dang hps 2: ")

h1 = a.split('h')[0]
m1 = a.split('p')
p1 = m1[0].split('h')[1]
s1 = m1[1].split('s')[0]

h2 = b.split('h')[0]
m2 = b.split('p')
p2 = m2[0].split('h')[1]
s2 = m2[1].split('s')[0]

tong1 = (int(h1)*60*60) + (int(p1)*60) + int(s1)
tong2 = (int(h2)*60*60) + (int(p2)*60) + int(s2)
tongp = (tong1+tong2)//60
tongh = (tongp)//60
hieup = (tong1-tong2)//60
hieuh = (hieup)//60

print('Tong = ',tongh,'h',tongp-tongh*60,'p',(tong1+tong2)%60,'s')
print('Hieu = ',hieuh,'h',hieup-hieuh*60,'p',(tong1-tong2)%60,'s')
