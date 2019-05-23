mylist = [1, 4, -5, 10, -7, 2, 3, -1]

# All positive values
pos = [n for n in mylist if n > 0]      # 列表推导
print(pos)

# All negitive values
neg = [n for n in mylist if n < 0]
print(neg)

pos = (n for n in mylist if n > 0)      # 生成器表达式
for i in pos:
    print(i, end=' ')
print()

values = ['1', '2', '-3', '-', '4', 'N/A', '5']
def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values))    # filter() 函数创建了一个迭代器，因此如果你想得到一个列表的话，
                                        # 就得像示例那样使用 list() 去转换
print(ivals)


import math
sqrt = [math.sqrt(n) for n in mylist if n > 0]
print(sqrt)

clip_neg = [n if n > 0 else 0 for n in mylist]
print(clip_neg)

clip_pos = [n if n < 0 else 0 for n in mylist]
print(clip_pos)

addresses = [ '5412 N CLARK',
              '5148 N CLARK',
              '5800 E 58TH',
              '2122 N CLARK',
              '5645 N RAVENSWOOD',
              '1060 W ADDISON',
              '4801 N BROADWAY',
              '1039 W GRANVILLE',
]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

# 它以一个 iterable 对象和一个相对应的 Boolean 选择器序列作为输入参数。
# 然后输出 iterable 对象中对 应选择器为 True 的元素。
from itertools import compress
more5 = [n > 5 for n in counts]
print(list(compress(addresses, more5)))     #compress()返回一个迭代器
