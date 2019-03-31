# 尽管字典的 values() 方法也是类似，但是它并不支持这里介绍的集合操作。
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

print(a.keys() & b.keys())
print(a.keys() - b.keys())
print(a.items() & b.items())

c = {key: a[key] for key in a.keys() & b.keys() - {'z', 'w'}}
print(c)
