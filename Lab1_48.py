print('Bộ nghiệm của phương trình 2x+7y+9z = 979 (x,y,z)>0 với x+y+x nho nhat')

for x in range((979 // 2)+1):
    for y in range((979 // 7) + 1):
        for z in range((979 // 9),-1,-1):
            if (2 * x) + (7 * y) + (9 * z) == 979:
                print(x, y, z)
                exit()