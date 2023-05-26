def canBacX(n):
    """Tinh can bac x cua so n"""
    x = int(input('x = '))
    return n**(1/x)
def daoSo(n):
    """Tra ve so dao cua n"""
    a = int(str(n)[::-1])
    return a
def checkSoChinhPhuong(n):
    """Kiem tra co phai so chinh phuong khong"""
    if n ==0 or n==1:
        return True
    for i in range(1, n//2+1):
        if (i * i) == n:
            return True
    return False
def checkSoNguyenTo(n):
    """Kiem tra co phai so nguyen to khong"""
    tmp = 0
    for i in range(1, n + 1):
        if n % i == 0:
            tmp += 1
    if tmp == 2:
        return True
    else:
        return False
def tichSoLe(n):
    """Tinh tich cac chu so le"""
    tmp=1
    while True:
        if (n%10)%2!=0:
            tmp*=(n%10)
            n =  n// 10
        elif n//10 ==0:
            return tmp
        else:
            n = n//10
def sumSoNguyenTo(n):
    """Tong cac so nguyen to nho hon n"""
    tmp=0
    for i in range(1,n):
        if checkSoNguyenTo(i):
            tmp+=i
    return tmp
def sumSoChinhPhuong(n):
    """Tong cac so nguyen to nho hon n"""
    tmp=0
    for i in range(1,n):
        if checkSoChinhPhuong(i):
            tmp+=i
    return tmp
def sumUocSoDuong(n):
    """Tong uoc so cua n"""
    tmp=0
    for i in range(1,n+1):
        if (n%i)==0 :
            tmp+=i
    return tmp

print(sumUocSoDuong.__doc__)
b = int(input('n = '))
print(sumUocSoDuong(b))
