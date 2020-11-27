

#对象实例的属性和方法
class Student(object):
    def __init__(self,name):
        self.name = name

#任何类只需要定义一个__call__()方法 就可以对实例进行调用
    def __call__(self):
        print('My name is %s' %self.name)

s = Student('Michael')
#可以把对象看成函数，把函数看成对象
s()
#判断一个变量是对象还是函数
#通过Callable对象  判断一个对象是否能被调用

print(callable(Student('shagou')))