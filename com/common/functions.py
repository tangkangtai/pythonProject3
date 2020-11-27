import numpy as np

# 损失函数

# 均方误差函数
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


# 交叉熵函数 cross_entropy
def cross_entropy_error(y, t):
    delta = 1e-7
    return - np.sum(t * np.log(y + delta))

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
#恒等函数
def identity_function(x):
    return x

#softmax函数
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
