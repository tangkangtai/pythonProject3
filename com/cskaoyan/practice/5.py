#--------------函数-----
print(int('123'))

print(int(12.34))

print(str(123))

print(str(1.23))


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

#---------返回多个值----------
import math

def move(x, y, step, angle):
    nx = x + step * math.cos(angle)

    ny = y - step * math.sin(angle)

    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

#------------------多返回值为一个tuple----
r = move(100, 100, 60, math.pi / 6)
print(r)


def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

print(fact(1))

print(fact(5))

#print(fact(100))

#--------------汉若塔---
#---n个圆盘从a借助b移动到c
def move(n ,a, b, c):
    if n == 1 :
        print(a, '-->', c)
        return
    move(n-1, a ,c , b)
    print(a , '-->', c)
    move(n-1 ,b ,a , c)

move(4,'A','B','C')


#-----------进制转换----
print(int('123',8))

#----计算x的N次方----
# def power(x , n):
#     s = 1
#     while n > 0:
#         n = n -1
#         s = s * n
#     return s

def power(x , n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
x = power(5)
print(x)


#-----函数参数匹配问题--
#函数的参数从左到右的顺序匹配，默认参数只能定义在必须参数的后面
def fn1(a, b=1, c=2):
    pass

#Error
# def fn2(a = 1, b):
#     pass


#-----可变参数------------
def fn(*args):
    print(args)
#解释器白变量args看成一个tuple
print(fn('你好','hello','fuck you','baby'))


def average(*args):
    sum = 0.0
    if len(args) == 0:
        return sum

    for x in args:
        sum = sum + x

    return sum / len(args)

print(average())

print(average(1,2))

print(average(1,2,2,3,4))
