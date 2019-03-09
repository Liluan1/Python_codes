def print_max(x, y):
    '''print the max num of two nums'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximun')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
