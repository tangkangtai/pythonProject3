#itertools  提供了非常有用的用于操作迭代对象的函数

import itertools
#它们的返回值不是list，而是Iterator

# #count()会创建一个无限的迭代器
# natuals = itertools.count(1)
# for n in natuals:
#     print(n)
#
# #cycle会把传入的一个序列无限重复下去
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)
#
#
# #repeat()负责把一个元素无限重复下去 第二个参数就可以限定重复次数
# ns = itertools.repeat('A',3)
# for n in ns:
#     print(n)
#

#takewile函数根据条件判断来截取出一个有限的序列
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x <= 10, natuals)
print(list(ns))

n1 = itertools.takewhile(lambda x : x<5 ,[1,4,6,4,1])
print(list(n1))

#chain() 可以把一组迭代对象串联起来 形成一个更大的迭代器
for c in itertools.chain('ABC','XYZ'):
    print(c)

#groupby() 把迭代器中相邻的重复元素挑出来放一起
for key ,group in itertools.groupby('AAABBBCCAAA'):
    print(key,list(group))

for key ,group in itertools.groupby('AaaBBbcCAAa',lambda c: c.upper()):
    print(key, list(group))


def pi(N):
    #step 1: 创建一个奇数序列 1, 3, 5, 7, 9
    step_1 = itertools.count(start=1,step=2)
    #step 2:取该序列的前N项 1,3,5,7,9...2N-1
    step_2 = itertools.takewhile(lambda x : x <= 2*N-1, step_1)
    #step 3:添加正负号符号并用4除： 4/1， -4/3.4/5，-4/7， 4/9
    sum = 0
    dividend = 4.0
    for n in step_2:
        sum += dividend / n
        dividend = dividend * (-1)

    return sum

