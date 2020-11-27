#判断对象类型  type()函数
# from com.cskaoyan.object.inheritanceAndPolymorphism import inheritanceAndPloymorphism
from com.cskaoyan.object.inheritanceAndPolymorphism.inheritanceAndPloymorphism import Animal, Dog, Cat

print(type(123))

print(type('str'))

print(type(None))
#----指向函数
print(type(abs))




print('-----------------------')


print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abc') == str)

print(type('abc') == type(123))

#--------------------------------
print('------------------------')
#--------------------------

import  types
def fn():
    pass

print(type(fn) == types.FunctionType)

print(type(abs) == types.BuiltinFunctionType)

print(type(lambda x : x) == types.LambdaType)

print(type((x for x in range(10))) == types.GeneratorType)

#------------------------------
print('-----------------------')
#------------------------------


a = Animal()
d = Dog()
c = Cat()

#--------type能判断的基本类型也能用isinstance()判断


#判断一个变量是否是某类型中的一种
print(isinstance([1,2,3],(list,tuple)))

#------------------------------
print('--------------------')
#------------------------------


#获取一个对象的所有属性和方法  可以使用dir函数 返回一个包含字符串的list
print(dir('ABC'))

print('ABC'.__len__())
print(len('ABC'))

print('ABC'.lower())

class MyObject(object):
    def __init__(self):
        self.x = 9
    def power(self):
        return self.x * self.x

obj = MyObject()

#---利用getattr()   setattr()   hasattr() 我们可以直接操作一个对象的状态

print(hasattr(obj,'x')) #有属性 'x'吗

print(obj.x)

print(hasattr(obj,'y'))

setattr(obj,'y',19)
print(hasattr(obj,'y'))

print(getattr(obj,'y'))

#如果试图访问不存在的属性 会跑出AttributeError的错误

#传入一个默认参数 如果属性不存在  就返回默认值
getattr(obj,'z',404)


#也可以获取对象的方法
print(hasattr(obj,'power'))

getattr(obj,'power')
#fn 指向obj.power
fn = getattr(obj,'power')
print(fn)
#直接调用 fn()与调用obj.power()是一样的
print(fn())


#------end----------------
#判断fp对象是否存在read方法,存在则读取
def readImage(fp):
    if hasattr(fp,'read'):
        pass 
        # return readData(fp)
    return None