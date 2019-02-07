#coding:utf-8
import string
while True:
    s = raw_input() #python2中的input()只能输入数字，raw_input()只输入字符串
    if s == 'quit':
        break
    print len(s)
