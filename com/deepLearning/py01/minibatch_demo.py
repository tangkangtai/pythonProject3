import numpy as np

# 训练数据维度
x_train = (60000, 784)
# 监督数据
t_train = (60000, 10)
# 第一维度  600000
train_size = x_train.shape[0]

# print(train_size)

batch_size_1 = 10

batch_mask = np.random.choice(train_size, batch_size_1)

x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]


def cross_entropy_error_1(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size


# 当监督数据是标签形式时
def cross_entropy_error_2(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size), t] + 1e-7)) / batch_size
