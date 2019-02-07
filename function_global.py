x = 50

def func():
    global x
    print 'x is', x
    x = 2
    print 'change globle x to', x

func()
print 'x is', x
