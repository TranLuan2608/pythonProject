
while True:
    n = int(input('Nhập n(n>0): '))
    if n<0:
        print('Nhap lai n')
    else:
        A = []
        for i in range(1, n):
            if n % i == 0:
                A.append(i)
        if not len(A):
            print('Khong co uoc so')
        else:
            print('Uoc so cua n la: ', A)
        break

