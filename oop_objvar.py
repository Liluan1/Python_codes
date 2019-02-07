#coding: utf-8
#所有的类成员都是公开的，但如果在变量名前加双下划线，如 __parivatevar ,python会使用名称调整来时起有效的成为一个私有变量，所有方法都是虚拟的
class Robot:
    '''表示一个带有名字的机器人'''

    #一个类变量用来计数机器人的数量
    population = 0

    def __init__(self, name):   #name 变量属于一个对象变量
        '''初始化数据'''
        self.name = name
        print "(Initializing {})".format(self.name)

        Robot.population += 1

    def die(self):
        print "{} is being destroyed".format(self.name)

        Robot.population -= 1

        if Robot.population == 0:
            print "{} was the last one".format(self.name)
        else:
            print "There are still {} robots working".format(Robot.population)

    def say_hi(self):
        print "Greetings, my master call me {}".format(self.name)

    @classmethod    #使用装饰器定义类方法等价于 how_many = classmethod(how_many)
    def how_many(cls):
        print "We have {:d} robots".format(cls.population)

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()

droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()

print "\nRobots can do some work here\n"

print "Robots have finished their work.So let's sedtoryed them"
droid1.die()
droid2.die()

Robot.how_many()
