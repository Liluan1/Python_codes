number = 23
guess = int(eval(input()))

if guess == number:
    print('yes')
elif guess < number:
    print('no,too small')
else :
    print('no, too big')
