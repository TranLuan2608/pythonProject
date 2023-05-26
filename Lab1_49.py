def checkNum(z):
    """Nhap vao mot so kiem tra xem so do co chan khong am khong"""
    if z>0 and (z%2)==0:
        return True
    else:
        return False

print(checkNum.__doc__)
a = int(input('n = '))
print(checkNum(a))