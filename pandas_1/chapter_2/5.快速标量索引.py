import timeit

import numpy as np
import pandas as pd

# iloc与loc不同，切片右端点不包含
#  注意: loc 靠标签进行索引， iloc靠行号进行索引

# iloc中接收的参数只能为整数或者整数列表或布尔列表，不能使用布尔series,如果要用就必须如下把values拿出来
from IPython.core.display import display

df = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')

print(df.head())
print('------------------------------------------')


#   当需要取一个元素时, at和iat方法能够提供更快的实现
display(df.at[1101,'School'])
display(df.loc[1101,'School'])
display(df.iat[0,0])
display(df.iloc[0,0])

# timeit(df.at[1101,'School'])

print(timeit.Timer('x=range(1000)').timeit())
# print(timeit.Timer('df.at[1001,"School"]').timeit())