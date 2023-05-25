

a = float(input('Nhập a: '))
b = float(input('Nhập b: '))

x = (((a+b)/((a**(1/3))+(b**(1/3)))) - (a*b)**(1/3))/(((a**(1/3))-(b**(1/3)))**2)
print(round(x,3))


