import numpy as np
import pandas as pd

# iloc与loc不同，切片右端点不包含
#  注意: loc 靠标签进行索引， iloc靠行号进行索引

# iloc中接收的参数只能为整数或者整数列表或布尔列表，不能使用布尔series,如果要用就必须如下把values拿出来

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')

print(df.head())
print('------------------------------------------')

# 1.单行索引
# print(df.iloc[3])

# 2.多行索引
# print(df.iloc[3:5])

# 3.单列索引
# print(df.iloc[:,3].head())

# 4.多列索引
# [::] 每隔多少个XX
# print(df.iloc[:,7::-2].head())

# 5.混合索引
# print(df.loc[3::4,5::-2].head())  #报错  loc 靠标签进行索引， iloc靠行号进行索引
print('------------------------------------')
# print(df.iloc[3::4,7::-2].head())

#   6.函数式索引
# print(df.iloc[lambda x:[3]].head())

## iloc中接收的参数只能为整数或者整数列表或布尔列表，不能使用布尔series,如果要用就必须如下把values拿出来
print(df.iloc[(df['School'] == 'S_1').values].head())

