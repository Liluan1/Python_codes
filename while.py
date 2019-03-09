#coding:utf-8
number = 23
running = True

while running :     #while可以使用else
    guess = int(eval(input()))
    if guess == number:
        print('yes')
        running = False
    elif guess < number:
        print('no,too small')
    else :
        print('no, too big')
