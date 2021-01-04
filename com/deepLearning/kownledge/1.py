
import numpy as np
#随机打乱顺序
x = np.arange(0,9)
np.random.shuffle(x)
print(x)

#从一个均匀分布[-8,-4)随机采样
weight_decay = 10 ** np.random.uniform(-8,-4)
lr = 10 ** np.random.uniform(-6 , -2)