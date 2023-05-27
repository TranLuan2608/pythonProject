print('Bộ nghiệm của phương trình 2x+7y+9z = 979 (x,y,z)>0')

for x in range(1,(979//2-7-9)+1):
    for y in range(1,(979//7-2-9)+1):
        for z in range(1,(979//9-2-7)+1):
            if(2*x)+(7*y)+(9*z)==979:
                print(x,y,z)