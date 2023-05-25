n = input('Nhập ngày tháng năm: ')
date = n.split()[0]
month = n.split()[1]
year = int(n.split()[2])
print('a) ',date,'/',month,'/',year)
print('b) ',date,'/',month,'/',year%100)
print('c) ',year,'/',month,'/',date)
