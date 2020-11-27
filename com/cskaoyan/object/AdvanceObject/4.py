
class Student(object):

    def __init__(self,name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    # 用于直接打印
    __repr__ = __str__


print(Student('Michael'))

s = Student('Michael')
s


class Fib(object):

    def __init__(self):
        self.a,self.b = 0 ,1
    #当一个类用于 for ...in 循环  类似list 和 tuple那样 则需要实现一个__iter__()方法
    # __iter__()方法返回一个迭代对象,然后python的for循环就会不断调用该迭代对象的__next()方法
    # 拿到下一个值  直到遇到StopIteration 错误时退出循环
    def __iter__(self):
        return self #实例本身就是迭代对象 返回自己

    def __next__(self):
        self.a,self.b = self.b, self.a + self.b

        if self.a > 100000:
            raise StopIteration()

        return self.a
#   用于类的 类似 list 的调用  Fib()[5]
    def __getitem__(self, item):
        # a , b = 1 , 1
        # for x in range(item):
        #     a, b = b , a + b
        #
        # return a
        #------------------------
        #-----Fib用于切片---
        if isinstance(item,int):
            a,b = 1, 1
            for x in range(item): #item是索引
                a, b = b, a + b
            return a

        if isinstance(n, slice): #item是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []

            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b

            return L

for n in Fib():
    print(n)

f = Fib()
print('-------------')
print(f[1])
print(f[5])
print(f[10])