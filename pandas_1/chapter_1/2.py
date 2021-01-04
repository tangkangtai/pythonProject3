import pandas as pd
import numpy as np

print(pd.__version__)


# 基本数据结构
# Series 常用属性值  值values 索引index  名字 name  类型 dtype
s = pd.Series(np.random.randn(5),index=['a','b','c','d','e'],name='这是一个Series',dtype='float64')
print(s)

# 访问series属性
print(s.values)
print(s.name)
print(s.index)
print(s.dtype)

# 取出来某一个元素
print(s['a'])

# 调用方法
print(s.mean())

# 查看相关方法
print([attr for attr in dir(s) if not attr.startswith('_')])