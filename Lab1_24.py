n = input("Nhap gio theo dinh dang hh mm ss: ")

h = int(n.split()[0])
m = int(n.split()[1])
s = int(n.split()[2])

if h>=0 and h<24:
    if m>=0 and m<60:
        if s>=0 and s<60:
            print(h,'h',m,'m',s,'s la hop le')
        else:
            print(h,'h',m,'m',s,'s la khong hop le')
    else:
        print(h, 'h', m, 'm', s, 's la khong hop le')
else:
    print(h,'h',m,'m',s,'s la khong hop le')