#coding:utf-8
print "hello world"
age = 20;
name = "swaroop"

print '{} was {} years old when he wrote this book'.format(name, age)
print 'why is {} playing with that python?'.format(name)

print '{0:.3f}'.format(1.0/3)
print '{0:_^11}'.format('hello'))   #使用下划线填充文本，保持文字处于中间位置
print '{name} wrote {book}'.format(name='swaroop', book='a byte of python')
