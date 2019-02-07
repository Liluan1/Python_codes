#coding: utf-8
#因为在 Teacher 和 Student 子类中定义了 __init__ 方法，Python不会自动调用基类 SchoolMermber 的构造函数，你必须显式调用

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print '(Initialized SchoolMember: {})'.format(self.name)

    def tell(self):
        print 'Name: {} Age: {}'.format(self.name, self.age),

class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary
        print '(Initialized Teacher: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Salary: {:d}'.format(self.salary)

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print '(Initialized Student: {})'.format(self.name)

    def tell(self):
        SchoolMember.tell(self)
        print 'Marks: {:d}'.format(self.marks)

t = Teacher('Mrs.Shrividya', 40, 30000)
s = Student('Liluan', 19, 75)

print

members = [t, s]
for member in members:
    member.tell()
