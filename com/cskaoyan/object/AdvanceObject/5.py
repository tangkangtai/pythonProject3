class Student(object):
    def __init__(self):
        self.name = 'Michael'

#   当调用不存在的属性'score'时候  python解释器会试图调用__getattr__(self,'score')
    #来尝试获得属性
    def __getattr__(self, item):
        if item == 'score':
            #也可以返回函数
        # if item = 'age'
            # return lambda :25
            return
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % item)


s = Student()
print(s.name)

print(s.score)

#
# s.age()  调用age


#--------------------------
#只有在没有找到属性的情况下才调用__getattr__


#动态
class Chain(object):
    def __init__(self, path= ''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' %(self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__

print(Chain().status.user.timeline.list)