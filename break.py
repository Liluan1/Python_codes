# coding:utf-8

while True:
    s = input()  # python2中的input()只能输入数字，raw_input()只输入字符串
    if s == 'quit':
        break
    print(len(s))
