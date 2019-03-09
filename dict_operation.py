prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

# 使用 zip() 函数先将键和值反转过来
min_price = min(zip(prices.values(), prices.keys()))
max_price = max(zip(prices.values(), prices.keys()))
print(min_price, max_price)

# zip() 函数创建的是一个只能访问一次的迭代器
prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

# 可以在 min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的键的信息
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

# 如果还想要得到最小值，你又得执行一次查找操作
print(prices[min(prices, key=lambda k: prices[k])])

# 当多个实体拥有相同的值的时候，键会决定返回结果
