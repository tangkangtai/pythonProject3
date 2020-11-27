#模块导入
from com.cskaoyan.object.AdvanceObject.hello import Hello

h = Hello()
h.hello()

print(type(Hello)) #类

print('---------------')

print(type(h)) #实例

print('---------------')

#class的定义是运行时动态创建的，而创建class的方法就是使用type()函数

#type()函数既可以返回一个对象的类型，又可以创建出新的类型
def fn(self, name = 'world'):
    print('Hello,%s' %name)
#class的方法名称与函数绑定，这里我们把函数fn绑定到方法名hello上
Hello = type('Hello',(object,),dict(hello = fn)) #创建Hello class

#------------元类------------------
#metaclass         控制类的创建行为

class ListMetaclass(type):

    def __new__(cls, name, bases, attrs):
        attrs['add'] = lambda self,value : self.append(value)
        return type.__new__(cls, name,bases,attrs)

#当我们传入关键字参数metaclass时，魔术就生效了，它指示Python解释器在创建MyList时，
# 要通过ListMetaclass.__new__()来创建，在此，我们可以修改类的定义，
# 比如，加上新的方法，然后，返回修改后的定义。
# __new__()方法接受的参数
# 1.当前准备创建的类的对象；
# 2.类的名字；
# 3.类继承的父类集合；
# 4.类的方法集合。
class MyList(list , metaclass=ListMetaclass):
    pass

L = MyList()
L.add(1)
print(L)



