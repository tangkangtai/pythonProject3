import pandas as pd
import numpy as np

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')

print(df.head())
print('------------------------------------------')
#   创建多级索引

#   a. 通过from_tuple或from_arrays

# tuples = [('A','a'),('A','b'),('B','a'),('B','b')]
# mul_index = pd.MultiIndex.from_tuples(tuples, names=('Upper','Lower'))
# print(mul_index)

print('-------------------------')
############## ??????????????????????????????????
# print(pd.DataFrame({'Score':['perfect','good','fair','bad']},index=mul_index))

#   b.利用zip创建元组
# L1 = list('AABB')
# L2 = list('abab')
# tuples = list(zip(L1,L2))
# mul_index = pd.MultiIndex.from_tuples(tuples,names=('Upper','Lower'))
# print(pd.DataFrame({'Score':['perfect','good','fair','bad']},index=mul_index))


#   c.通过Array创建
# arrays = [['A','a'],['A','b'],['B','a'],['B','b']]
# mul_index = pd.MultiIndex.from_tuples(arrays, names=('Upper','Lower'))
# print(pd.DataFrame({'Score':['perfect','good','fair','bad']},index=mul_index))

# print('--------------')
#   由此看出内部自动转成元祖
# print(mul_index)


#   d.通过from_product
# L1 = ['A','B']
# L2 = ['a','b']
#两两相乘，类似笛卡尔积
# print(pd.MultiIndex.from_product([L1,L2],names=('Upper','Lower')))


#   e. 指定df中的列创建(set_index方法)
#   多层索引切片
df_using_mul = df.set_index(['Class','Address'])
print(df_using_mul)

#   一般切片
#   当索引不排序时，单个索引会报出性能警告
#   df_using_mul.loc['C_2','street_5']

#   该函数检查是否排序
#   df_using_mul.index.is_lexsorted()
print(df_using_mul.sort_index().index.is_lexsorted())

# print(df_using_mul.sort_index().loc['C_2','street_5'])


#   df_using_mul.loc[('C_2','street_5'):]   报错
#   当不排序时，不能使用多层切片
# print(df_using_mul.sort_index().loc[('C_2','street_6'):('C_3','street_4')])


#   非元组也是合法的，表示选中该层所有元素
# print(df_using_mul.sort_index().loc[('C_2','street_7'):'C_3'].head())


#   特殊情况
#   1.由元组构成列表
#   表示选出某几个元素，精确到最内层索引
print(df_using_mul.sort_index().loc[[('C_2','street_7'),('C_3','street_2')]])

#   2.由列表构成的元组
#   选出第一层在'C_2'和'C_3'中且第二层在'street_4'和'street_7'中行
print(df_using_mul.sort_index().loc[(['C_2','C_3'],['street_4','street_7']),:])
