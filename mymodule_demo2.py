#coding: utf-8
from mymodule import say_hi, __version__    #不建议使用这种方式，容易出现名称冲突

say_hi()
print 'version', __version__
