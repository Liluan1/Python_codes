#coding: utf-8
print 'simple assignment'
shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist

del shoplist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist

print 'copy by making a full silce'

mylist = shoplist[:]    #如果希望创建一份诸如序列等复杂对象的副本，必须使用切片操作来制作副本，对列表的赋值语句不会创建一份副本，而是一个引用

del mylist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
