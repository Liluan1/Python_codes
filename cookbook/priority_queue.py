import heapq


class priority_queue:
    def __init__(self):
        self._queue = []
        self._index = 0

# 队列包含了一个 (-priority, index, item) 的元组
# 优先级为负数的目的是使得元素按照优先级从高到低排序
# index 变量的作用是保证同等优先级元素的正确排序
    def push(self, priority, item):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'item({!r})'.format(self.name)


q = priority_queue()
q.push(1, Item('foo'))
q.push(5, Item('bar'))
q.push(4, Item('spam'))
q.push(1, Item('grok'))
print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())
