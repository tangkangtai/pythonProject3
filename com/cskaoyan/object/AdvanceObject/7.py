
#枚举类
from enum import Enum, unique

Month = Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct',
                      'Nov','Dec'))
#这样我们过得了Month的枚举类,可以直接使用Month.jan来引用一个常量
#     __members__  属性返回一个dict字典 然后利用items()方法可以遍历所有键值对
#  value属性  是系统自动赋予给int类型的
for name,member in Month.__members__.items():
    print(name,'=>',member, ',' , member.value)

#  @unique装饰器 可以帮助我们检查保证没有重复值

@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6

#访问枚举类型的若干方法
day1 = Weekday.Mon
print(day1)

print(Weekday.Tue)

print(Weekday['Tue'])

print(Weekday.Tue.value)

print(day1 == Weekday.Mon)

print(day1 == Weekday.Tue)

print(Weekday(1))

print(day1 == Weekday(1))

#print(Weekday(7))

print('---------------')
for name ,member in Weekday.__members__.items():
    print(name,'=>',member)

#-----------------------
print('---------------')
#-----------------------

class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

bart = Student('Bart',Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过')
else:
    print('测试失败')
