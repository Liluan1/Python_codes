# d = {
#     'a': [1, 2, 3],
#     'b': [4, 5]
# }

# e = {
#     'a': [1, 2, 3],
#     'b': [4, 5]
# }

# print(d['a'])

# defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值
from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d['a'])

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['b'].add(4)
print(d)

# d = {}
# d.setdefault('a', []).append(1)
# d.setdefault('a', []).append(2)
# d.setdefault('b', []).append(4)
