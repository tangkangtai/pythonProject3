import pandas as pd


# DataFrame

#   列中行的数量需要相等
df = pd.DataFrame({'col1':list('abcde'),'col2':range(5,10),'col3':[1.3,2.5,3.6,4.6,5.8]},
                  index=list('一二三四五'))
print(df)

print('-------------------------')
# 从DataFrame取出一列为Series
print(df['col1'])

print('---------------')

print(type(df))

print('-----------')

print(type(df['col1']))

print('-----------------------')

# 修改行 或 列名   修改不会改变原有的DataFrame
print(df.rename(index={'一':'one'},columns={'col1':'new_col1'}))


# 调用属性和方法
print(df.index)

print('----------')

print(df.columns)

print('----------------')

print(df.values)

print('-----------')
##############################################
print(df.shape)  # 5*3
##############################################
print('----------------')

print(df.mean())

# 索引对齐特性
df1 = pd.DataFrame({'A':[1,2,3]},index=[1,2,3])
df2 = pd.DataFrame({'A':[1,2,3]},index=[3,1,2])

print(df1 - df2)


# 列的删除和添加
# 对于删除而言，可以使用drop函数或pop或del
print(df.drop(index='五',columns='col1'))
print('-------------------------')

print(df)


# 2
df['col1'] = [1,2,3,4,5]
del df['col1']
print(df)

print('-------------------')

# pop方法直接在原来的DataFrame上操作，且返回被删除的列
df['col1'] = [1,2,3,4,5]  # 不定义则报错
print(df.pop('col1'))
print('----------------------')
print(df)


# 增加列 或者使用assign方法
df1['B'] = list('abc')

print(df1)

print('------------------')


# assign方法不会对原DataFrame做修改
print(df1.assign(C=pd.Series(list('def')))) # 由于索引对齐

print('-------------')

print(df1)
print('------------')

# print(list('abc')[0])

# 根据类型选择列
print(df)
print('----------------')
#   head返回前5行
print(df.select_dtypes(include=['number']).head())
print('---------------')
print(df.select_dtypes(include=['float']).head())

print('-------------')


# 将Series转换成DataFrame
s = df.mean()
s.name = 'to_DataFrame'
print(s)
print('------')
print(s.to_frame())

print('----------------')
# T符号转置
print(s.to_frame().T)




