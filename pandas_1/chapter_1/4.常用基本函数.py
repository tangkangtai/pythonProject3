import pandas as pd

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv')

print(df)
# print(df.head())
# print(df.head(3))

print('----------------')

# print(df.tail())


# unique和nunique
# unique显示所有的唯一值
print(df['Physics'].unique())

print('------------------')
# nunique显示有多少个唯一值
print(df['Physics'].nunique())

print('-------------------')

# count返回非缺失值元素个数
print(df['Physics'].count())

print('----------------------')
# value_counts 返回每个元素有多少个
print(df['Physics'].value_counts())

print('-----------------------------')


# describe 和 info
# info函数返回有哪些列，有多少非缺失值，每列的类型

print(df.info())

print('--------------------')

# describe默认统计数值型数据的各个统计量

print(df.describe())

print('----------------')
# 也可以自行选择分位数
print(df.describe(percentiles=[.05,.25,.75,.95]))


print('------------------')

# 对于非数值类型的也可以使用describe函数
print(df['Physics'].describe())

print('----------------')
# idxmax 和 nlargest
# idxmax函数返回最大值所在索引，在某些情况下特别适用，idxmin功能类似
print(df['Math'].idxmax())

print(df['Math'].idxmin())
print('-----------------------')

# nlargest函数返回前几个大的元素值(可加参数)，nsmallest功能类似
print(df['Math'].nlargest())

# clip 和 replace 两类替换函数

# clip是对超过或者低于某些值的数进行截断
print(df)
print('--------------------')
print(df['Math'].head())

print('-------------------')
# replace是对某些值进行替换
print(df['Address'].head())
print('---------------------')
print(df['Address'].replace(['street_1','street_2'],['one','two']).head())


print('----------------')
# 通过字典，可以直接在表中修改
print(df.replace({'Address':{'street_1':'one','street_2':'two'}}).head())

print('-------------------')
# apply 函数
# 对于 Series,它可以迭代每一列的值操作  可以使用lamda表达式 也可以使用函数
print(df['Math'].apply(lambda x:str(x)+'!').head())

print('---------------------------')

# 对于DataFrame,它在默认axis=0下可以迭代每一个列操作  axis=1 每行
print(df.apply(lambda x:x.apply(lambda x:str(x)+'!')).head())


print('----------------------')
# 排序
#   索引排序
print(df.set_index('Math').head())  #set_index函数可以设置索引

print('-------------')

print(df.set_index('Math').sort_index().head()) # 可以设置ascending参数，默认为升序，True

print('--------------------------')

print(df)
print('----------------------')
# 值排序
print(df.sort_values(by='Class').head())

# 多个值排序，既先对第一层排，在第一层相同的情况下对第二层排序
print(df.sort_values(by=['Address','Height']).head())


