from collections import namedtuple, deque, defaultdict, OrderedDict,\
    ChainMap, Counter
import os, argparse
#tuple可以用来表示不变的集合
#namedtuple是一个函数 它用来创建一个自定义的tuple对象
#并且规定了tuple元素的个数 并可以用属性而不是索引来引用tuple的某个元素

Point = namedtuple('Piont',['x','y'])
p = Point(1,2)
print(p)
print(p.x)
print(p.y)
print(isinstance(p,Point))
print(isinstance(p,tuple))


#--------------------------
#类似的如果要用坐标和半径表示一个圆 也可以用
#--------------------------
Circle = namedtuple('Circle',['x','y','r'])

#---------------------------------
print('----------------------')

#list存储数据 按照索引访问元素很快 但插入和删除元素就很慢
#deque  双向列表
#  deque除了实现了list的append()和pop()外 还支持appendleft()和popleft()
q = deque(['a','b','c'])
q.append('x')
q.appendleft('y')
print(q)

#-------------------
print('---------------------')
#-------------------


#defaultdict
#使用dict时 如果引用的Key不存在就会跑出KeyError异常
# 如果希望Key不存在 返回一个默认值就可以使用 defaultdict
dd = defaultdict(lambda : 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])

#====================================
print('------------------------------')
#====================================
#如果希望dict的Key是有序的
#可以用OrderedDict

d = dict([('a',1),('b',2),('c',3)])
print(d)

od = OrderedDict([('a',1),('b',2),('c',3)])
print(od)
#OrderedDict的Key会按照插入的顺序排列  不是Key本身排序
od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3

print(list(od.keys()))

#=========================
print('----------------------')
#=========================
class LastUpdateOrderedDict(OrderedDict):

    def __init__(self,capacity):
        super(LastUpdateOrderedDict,self).__init__()
        self._capacity  = capacity

    def __setitem__(self, key, value):
        containsKey = 1 if key in self else 0
        if len(self) - containsKey >= self._capacity:
    #''Remove and return a (key, value) pair from the dictionary.
    # Pairs are returned in LIFO order if last is true or FIFO order if false.

            last = self.popitem(last=False)
            print('remove',last)

        if containsKey:
            del self[key]
            print('set:', (key, value))
        else:
            print('add:', (key, value))

        OrderedDict.__setitem__(self, key, value)


#chainMap
#chainMap可以把一组dict串起来并组成一个逻辑上的dict
#chainMap本身也是一个dict 但是查找的时候 会按照顺序在内部的dict依次查找
#上方的导入 argparse
# argparse 是 Python 内置的一个用于命令项选项与参数解析的模块，通过在程序中定义好我们需要的参数，
# argparse 将会从 sys.argv 中解析出这些参数，并自动生成帮助和使用信息。
# 当然，Python 也有第三方的库可用于命令行解析，而且功能也更加强大，比如 docopt，Click。

#构建缺省参数
defaults = {
    'color':'red',
    'user':'guest'
}
#构建命令行参数
#1.创建一个解析对象
parser = argparse.ArgumentParser()
#2.向该对象中添加你要关注的命令行参数和选项
parser.add_argument('-u','--user')
parser.add_argument('-c','--color')
#3.进行解析
namespace = parser.parse_args()
#本质上建立一个字典
command_line_args = {k : v for k , v in vars(namespace).items() if v}

#组合成ChainMap
#命令行参数  比 环境变量 的优先级高
combined = ChainMap(command_line_args,os.environ,defaults)

#打印参数
print('color=%s' % combined['color'])
print('user=%s' % combined['user'])

print('-------------------------')

#Counter
#counter是一个简单的计数器
c = Counter()

#例子  统计字符出现的个数
for ch in 'programming':
    c[ch] = c[ch] + 1

print(c)
#update增加元素
c.update('hello')
print(c)


