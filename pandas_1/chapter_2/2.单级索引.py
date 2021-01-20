import numpy as np
import pandas as pd

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')

print(df.head())
print('------------------------------------------')
# 常用的索引方法可能就是这三类，其中iloc表示位置索引，loc表示标签索引，[]也具有很大的便利性
#   本质上说，loc中能传入的只有布尔列表和索引子集构成的列表，只要把握这个原则就很容易理解下面这些操作

# 1.    loc方法
# print(df.loc[1103])


# 2. 多行索引
# print(df.loc[[1102,2304]])

#   索引切片(左右都是闭集合)
# print(df.loc[1304:2103].head())
# print(df.loc[2402::-1].head())


# 3. 单列索引
# print(df.loc[:,'Height'].head())

# 4. 多列索引
#   1. 多列
# print(df.loc[:,['Height','Math']].head())

#   2. 多列切片
# print(df.loc[:,'Height':'Math'].head())


# 5.联合索引
# print(df.loc[1102:2401:3,'Height':'Math'].head())

# 6.函数式索引
#   loc中使用的函数，传入参数就是前面的df
# print(df.loc[lambda x:x['Gender'] == 'M'].head())


#   loc中可以传入函数，并且函数的输入值是整张表，输出为标量，切片，合法列表
# def f(x):
#     return [1101,1103]
#
# print(df.loc[f])


# 6.布尔索引
print(df.loc[df['Address'].isin(['street_7','street_4'])].head())

print(df.loc[[True if i[-1]=='4' or i[-1] =='7' else False for i in df['Address'].values]].head())