import numpy as np


class Momentum:

    def __init__(self, lr=0.01, momentum=0.9):
        self.lr = lr
        self.momentum = momentum
        self.v = None

    #字典的 keys() 和 values() 和items()方法
    #       键           值       键-值对

    #params 保存权重和偏置
    def update(self, params, grads):

        if self.v is None:
            # 初始化时，v中什么都不保存，但当第一次调用update()时，
            # v会以字典型变量的形式保存与参数结构相同的数据
            self.v = {}
            for key, val in params.items():
                self.v[key] = np.zeros_like(val)

        for key in params.keys():
            self.v[key] = self.momentum * self.v[key] - self.lr * grads[key]
            params[key] += self.v[key]


class AdaGrad:
    def __init__(self, lr=0.01):
        self.lr = lr
        self.h = None

    def update(self, params, grads):
        if self.h is None:
            self.h = {}
            for key, val in params.items():
                self.h[key] = np.zeros_like(val)

        for key in params.keys():
            self.h[key] += grads[key] * grads[key]
            params[key] -= self.lr * grads[key] / (np.sqrt(self.h[key]) + 1e-7)


#Adam设置3个超参数，一个学习率，另外两个是一次momentum系数  和二次momentum系数
#根据论文设定值 0.9  0.999
