def checkNum(n):
    """Nhap vao mot so trong doan [-89,90] va kiem tra no"""
    while True:
        if n<-89 or n>90:
            a = int(input('Nhap lai n = '))
            n = a
        else:
            return True

print(checkNum.__doc__)
b = int(input('n = '))
print(checkNum(b))