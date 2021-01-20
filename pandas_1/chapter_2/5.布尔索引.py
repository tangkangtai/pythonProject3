import numpy as np
import pandas as pd

# iloc与loc不同，切片右端点不包含
#  注意: loc 靠标签进行索引， iloc靠行号进行索引

# iloc中接收的参数只能为整数或者整数列表或布尔列表，不能使用布尔series,如果要用就必须如下把values拿出来

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')

print(df.head())
print('------------------------------------------')


#   布尔符号: '&','|','~' 分别代表  和 and，或 or, 取反 not
# print(df[(df['Gender'] == 'F') & (df['Address'] == 'street_2')].head())

# print(df[(df['Math'] > 85) | (df['Address'] == 'street_7')].head())


# print(df[~((df['Math']>75) | (df['Address'] == 'street_1'))].head())


#   loc和[]中相应位置都能使用布尔列表选择:

# print(df.loc[df['Math']>60,df.columns == 'Physics'].head())

# isin方法
# print(df[df['Address'].isin(['street_1','street_4']) & df['Physics'].isin(['A','A+'])])

#   上面的也可以用字典表示
print(df[df[['Address','Physics']].isin({'Address':['street_1','street_4'],'Physics':['A','A+']}).all(1)])