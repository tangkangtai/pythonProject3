import numpy as np
import pandas as pd

# iloc与loc不同，切片右端点不包含
#  注意: loc 靠标签进行索引， iloc靠行号进行索引

# iloc中接收的参数只能为整数或者整数列表或布尔列表，不能使用布尔series,如果要用就必须如下把values拿出来

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')

print(df.head())
print('------------------------------------------')

# Series的[]操作符
# 1.单元素索引

s = pd.Series(df['Math'],index=df.index)
# print(s[1101])

#  2.多行索引
# print(s[0:4])

#   3.函数式索引:
#   注意使用lambda函数时，直接切片(如:s[lambda x:16::-6])就会报错，此时使用的不是绝对位置切片
# print(s[lambda x:x.index[16::-6]])


#   4.布尔索引
# print(s)
print(s[s>80])