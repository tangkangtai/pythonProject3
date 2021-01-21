import pandas as pd
import numpy as np

L1, L2 = ['A','B'],['a','b','c']
mul_index1 = pd.MultiIndex.from_product([L1,L2],names=('Upper','Lower'))

L3, L4 = ['D','E','F'],['d','e','f']
mul_index2 = pd.MultiIndex.from_product([L3,L4],names=('Big','Small'))

df_s = pd.DataFrame(np.random.rand(6,9), index=mul_index1, columns=mul_index2)
print(df_s)


idx = pd.IndexSlice
#   IndexSlice本质上是多个Slice对象的包装
print(idx[1:9:2,'A':'C','start':'end':2])

#   索引Slice可以与loc一起完成切片操作，主要有两种用法
#   a. loc[idx[*,*]]型