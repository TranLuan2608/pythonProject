while True:
    n = int(input('Nhập N: '))
    if n<0 :
        print('Nhap lai')
    else:
        for i in range(1,n):
            if (i*i)==n:
                print(n,' là số chính phương')
                exit()
        print(n, ' không phải là số chính phương')
        break