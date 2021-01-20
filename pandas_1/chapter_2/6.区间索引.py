import pandas as pd


# 此处介绍的并不是只能单级索引中使用区间索引，只是作为一种特殊类型的索引方式，在此处先行介绍

#   a.利用 interval_range方法
#   closed参数可选  'left'  'right' 'both' 'neither' 默认左开右闭
print(pd.interval_range(start=0,end=5))
