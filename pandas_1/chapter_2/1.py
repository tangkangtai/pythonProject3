import numpy as np
import pandas as pd

# index_col 用作行索引的列编号或者列名，如果给定一个序列则有多个行索引
df1 = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='ID')
df2 = pd.read_csv('C:/Users/tang/Desktop/joyful-pandas-master/data/table.csv',index_col='Weight')
print(df1.head())
print('-------------------------------------------------')
print(df2.head())