# 星号表达式默认是一个列表
record = ('Liluan', 'Liluan@example.com', '0537-123456', '12345678900')
name, email, *phone_numbers = record
print(phone_numbers)

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4)
]


def do_foo(x, y):
    print('foo', x, y)


def do_bar(s):
    print('bar', s)


for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fileds, homedir, sh = line.split(':')
print(uname, fileds, homedir, sh)

record = ('liluan', 20, 123.45, (3, 6, 2019))
name, *_, (*_, year) = record
print(name, year)

items = [1, 2, 3, 4, 5, 6]
head, *tail = items
print(head, tail)
