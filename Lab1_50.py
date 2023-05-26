def checkNum(z):
    """Nhap vao mot so neu
    gia tri am, so le = -1
    gia tri duong, so chan = 1
    con lai  = 0"""
    if z>0 and (z%2)==0:
        return 1
    elif z<0 and (z%2)!=0:
        return -1
    else:
        return 0

print(checkNum.__doc__)
a = int(input('n = '))
print(checkNum(a))