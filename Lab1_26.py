a = int(input('Nhap a: '))
b = int(input('Nhap b: '))
c = int(input('Nhap c: '))

if a<=b and a<c and b<=c:
    print(a,b,c)
elif a<b and a<=c and c<=b:
    print(a, c, b)
elif b<=a and b<c and a<=c:
    print(b,a,c)
elif b<a and b<=c and c<=a:
    print(b,c,a)
elif c<=a and c<b and a<=b:
    print(c,a,b)
else:
    print(c,b,a)

N = int(input('Nhập số N: '))
x = N//1000
y = (N//100)%10
z = (N%100)//10
t = N%10
A = [x,y,z,t]
A.sort()
b = A[0]*1000 + A[1]*100 + A[2]*10 + A[3]
print(b)