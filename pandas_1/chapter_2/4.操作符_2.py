import numpy as np
import pandas as pd

# iloc与loc不同，切片右端点不包含
#  注意: loc 靠标签进行索引， iloc靠行号进行索引

# iloc中接收的参数只能为整数或者整数列表或布尔列表，不能使用布尔series,如果要用就必须如下把values拿出来

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')

print(df.head())
print('------------------------------------------')

#   DataFrame的[]操作
#   1.单行索引
#   如果写成df['label']会报错，同Series使用了绝对位置切片,
#   如果想要获得某一个元素,可用如下get_loc方法
# print(df[1:2])


# row = df.index.get_loc(1102)
# print(df[row:row+1])

#   2.多行索引
#   用切片，如果是选取指定的某几行，推荐使用loc 否则很可能报错
# print(df[3:5])
# print(df.loc[[1102,1105]])
# print(df.loc[1102:1105])
# print(df.iloc[1:3])


#-------------------------------------------------------------------
#   单列索引
# print(df['School'].head())

#   多列索引
# print(df[['School','Math']].head())

#   函数式索引
print(df[lambda x:['Math','Physics']].head())

#   布尔索引
print(df[df['Gender']=='F'].head())

#   一般来说，[]操作符常用来列选择或者布尔选择，尽量避免行的选择
