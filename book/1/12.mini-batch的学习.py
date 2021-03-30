import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist

(x_train,t_train),(x_test, t_test) = load_mnist(normalize=True,one_hot_label=True)

print(x_train.shape)    # (60000,784)
print(t_train.shape)    # (60000, 10)
print(x_train.shape[0]) # 60000


#读入上面的MNIST数据后，训练数据有60000个，输入数据是784维（28 × 28）的图像数据，
# 监督数据是10维的数据。因此，
# 上面的 x_train 、 t_train 的形状分别是 (60000, 784) 和 (60000, 10)



#------------------------------------------
#   随机抽取10笔数据
#   使用 np.random.choice() 可以从指定的数字中随机选择想要的数字。比如，
#   np.random.choice(60000, 10) 会从0到59999之间随机选择10个数字
train_size = x_train.shape[0]
batch_size = 10
batch_mask = np.random.choice(train_size,batch_size)
x_batch = x_train[batch_mask]
t_batch = t_train[batch_mask]
#----------------------------------------
print(np.random.choice(60000,10))


#--------------------------------------------
#   mini-batch版交叉熵误差的实现
#   普通版本
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


#   单个数据和批量数据同时处理的mini-batch交叉熵函数
#   one-hot形式
def cross_entropy_error(y, t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)
    batch_size1 = y.shape[0]
    return -np.sum(t * np.log(y + 1e-7)) / batch_size1

#   监督数据为标签形式时
def cross_entropy_error(y ,t):
    if y.ndim == 1:
        t = t.reshape(1, t.size)
        y = y.reshape(1, y.size)

    batch_size2 = y.shape[0]
    return -np.sum(np.log(y[np.arange(batch_size2),t] + 1e-7)) / batch_size2

#   -----------------------------------------
print('----------------')

