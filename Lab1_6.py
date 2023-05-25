from datetime import date

current_year = date.today().year

n  = int(input('Nhap vao nam sinh:'))

print('Ban sinh nam',n,' vay ban ',current_year-n,' tuoi')
