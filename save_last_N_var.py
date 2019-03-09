from collections import deque


# deque(maxlen=N)会新建一个固定大小的队列，默认无限大小
def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)


if __name__ == '__main__':
    with open(r'./poem.txt') as f:
        for line, prevlines in search(f, 's'):
            for pline in prevlines:
                print(pline, end='')
            print(line, end='')
            print('-' * 20)
