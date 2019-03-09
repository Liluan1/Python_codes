p = (4, 5)
x, y = p
print(x, y)

data = ['liluan', 50, 19.9, (2019, 3, 6)]
name, shares, price, date = data
print(date)

name, shares, price, (year, mon, day) = data
print(year, mon, day)

s = "liluan"
a, b, c, d, e, f = s
print(a, b, c, d, e, f)

# 通常使用‘_’、‘ign’表示丢弃该变量
data = ['liluan', 50, 19.9, (2019, 3, 6)]
_, shares, price, _ = data
print(shares, price)
