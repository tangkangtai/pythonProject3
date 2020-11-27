from types import MethodType

class Student(object):
    pass

def set_age(self,age):
    self.age = age

#------------------
s = Student()
s.name = 'Michael'
print(s.name)
#-------------------
print('-----------------')
#-------------------
#MethodType(x1,x2,x3(可选))
# 第一个参数是要绑定的方法，第二个参数是要绑定的对象，第三个参数是类名(可省略)
s.set_age = MethodType(set_age,s) #给实例绑定方法
s.set_age(25)#调用实例方法
print(s.age)

#------------------
print('--------------------')
#------------------
s1 = Student()#创建新的实例
#s1.set_age(25)#尝试调用方法  报错

#-----       __slots__

#限制实例属性 只允许Student实例添加name和age属性

# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Student_1(object):
    __slots__ = ('name','age')

s = Student()
s.name = 'Michael'
s.age = 25
#s.score = 99 #绑定属性score

class GraduateStudent(Student):
    pass

g = GraduateStudent()
g.score = 999
print(g.score)
