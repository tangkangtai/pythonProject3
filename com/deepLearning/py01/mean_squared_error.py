import numpy as np


# 损失函数

# 均方误差函数
def mean_squared_error(y, t):
    return 0.5 * np.sum((y - t) ** 2)


# 交叉熵函数 cross_entropy
def cross_entropy_error(y, t):
    delta = 1e-7
    return - np.sum(t * np.log(y + delta))


t = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]

y = [0.1, 0.05, 0.6, 0.0, 0.05, 0.1, 0.0, 0.1, 0.0, 0.0]

mean_squared_error(np.array(y), np.array(t))

cross_entropy_error(np.array(y), np.array(t))

#从 0-100之间 随机选择 10个数字
print(np.random.choice(100, 10))
x = [1,2,3,4,5,6]
print(np.array(x))
x1 = np.array(x)
print(x1.ndim)
x2 = x1.reshape(2,3)
print(x2)
print(x2.ndim)

print(x2[0])
print('----------------')
print(x2.shape)
print(x2.shape[0])
print(x2.shape[1])