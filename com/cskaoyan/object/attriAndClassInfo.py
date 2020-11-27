#实例属性和类属性

class Student(object):
    #测试
    count = 0

    def __init__(self,name):
        self.name = name
        Student.count += 1

#给实例绑定属性的方法是通过实例变量 或者self变量
s = Student('Bob')
s.score = 90

#----------
class Student_1(object):
    #类属性,归类所有，且所有实例都可以访问
    name = 'Student'

s = Student_1()

print(s.name)

print(Student_1.name)

s.name = 'Michael'
print(s.name)#实例属性优先级比类属性高

print(Student_1.name)#类属性并未消失，通过类名.属性仍可以访问


del s.name #删除实例属性
print(s.name) #再次调用

s1 = Student('s1')
print(Student.count)
s2 = Student('s2')
print(Student.count)
s3 = Student('s3')
print(Student.count)