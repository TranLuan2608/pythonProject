while True:
    a = float(input('Nhập số km: '))
    if a<0 :
        print('Nhap lai')
    else:
        if a<=120:
            if a<2:
                print(a*15000,'vnd')
                break
            elif a>2 and a<6:
                print(a*13500,'vnd')
                break
            else:
                print(a*11000,'vnd')
                break
        else:
            print((a*11000)*0.1,'vnd')
            break