
from types import MethodType



class Student(object):
    pass

s1 = Student()
#python 3目前不可用
#s1.set_age = MethodType(set_age,s1,Student)
# s1.set_age(23)
# print(s1.age)

#这种绑定 只将方法绑定到s1对象上面
# s2 = Student()
# s2.set_age(24)
# print(s2.age)

def set_age(self,age):
    self.age = age
#-----------------------
print('------------------')
#-----------------------

#------将set_age方法绑定到类上-
#应该为  类属性
Student.set_age = MethodType(set_age,Student)
s1 = Student()
s2 = Student()
s1.set_age(12)
s2.set_age(13)

print(s1.age)
print(s2.age)
