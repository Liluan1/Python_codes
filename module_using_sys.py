#coding :utf-8
import sys  #尽量避免使用 from...import

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe python path is', sys.path, '\n')
