# 这个方法仅仅在序列中元素为 hashable 的时候才管用。
# def dedupe(items):
#     seen = set()
#     for key in items:
#         if key not in seen:
#             yield key
#             seen.add(key)

# a = [1, 2, 3, 4, 5, 23, 2, 32, 542, 5, 234, 23, 5]
# print(list(dedupe(a)))


def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe(a, lambda d: (d['x'], d['y']))))
print(list(dedupe(a, lambda d: d['x'])))
