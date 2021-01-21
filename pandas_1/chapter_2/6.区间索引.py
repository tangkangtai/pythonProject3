import pandas as pd

import numpy as np


# iloc与loc不同，切片右端点不包含
#  注意: loc 靠标签进行索引， iloc靠行号进行索引

# iloc中接收的参数只能为整数或者整数列表或布尔列表，不能使用布尔series,如果要用就必须如下把values拿出来

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')

print(df.head())
print('------------------------------------------')

# 此处介绍的并不是只能单级索引中使用区间索引，只是作为一种特殊类型的索引方式，在此处先行介绍

#   a.利用 interval_range方法
#   closed参数可选  'left'  'right' 'both' 'neither' 默认左开右闭
# print(pd.interval_range(start=0,end=5))


#   periods参数控制区间个数，freq控制步长
# print(pd.interval_range(start=0,periods=8,freq=5))


#   b.利用cut将数值转为区间为元素的分类变量，例如统计数学成绩的区间情况
math_interval = pd.cut(df['Math'],bins=[0,40,60,80,100])
#   注意，如果没有类型转换，此时并不是区间类型，而是category类型
print(math_interval.head())

print('----------------------------------------------------')

#   区间索引的选取
#   reset_index() 重新排序
df_i = df.join(math_interval,rsuffix='_interval')[['Math','Math_interval']]\
    .reset_index().set_index('Math_interval')
                            # 用于(左侧lsuffix)右侧侧数据框的重复列,把重复列重新命名，原来的列名+字符串
# df_i = df.join(math_interval,rsuffix='_interval')
print(df_i.head())

print('-----------------------------')
#   包含该值就会被选中
# print(df_i.loc[65].head())

print('----------------------------------')
# print(df_i.loc[[65,90]].head())

#   如果想要选取某个区间，先要把分类变量转为区间变量，再使用overlap方法

#   只要索引与(70,85]这个区间有交集就会被选中，注意pd.Interval默认构造区间都是左开右闭，可选
#   closed参数right,left,both,neither
print(df_i[df_i.index.astype('interval').overlaps(pd.Interval(70,85))].head())