import numpy as np


# 损失函数
#   1.均方误差
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


# 例子
t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.0, 0.1, 0.0, 0.0]

y2 = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.6, 0.0, 0.0]

mean_squared_error(np.array(y), np.array(t))


#   2.交叉熵误差

def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


