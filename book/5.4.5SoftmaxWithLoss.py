
import numpy as np

def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

#   2.交叉熵误差
#   log表示以e为底数的自然对数（log e ）。y k 是神经网络的输出，t k 是
#   正确解标签。并且，t k 中只有正确解标签的索引为1，其他均为0（one-hot表示）
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


class SoftmaxWithLoss:
    def __init__(self):
        self.loss = None    #损失
        self.y = None       #softmax的输出
        self.t = None       #监督数据

    def forward(self,x,t):
        self.t = t
        self.y = softmax(x)
        self.loss = cross_entropy_error(self.y, self.t)

        return self.loss

    def backward(self, dout =1):
        batch_size = self.t.shape[0]
        dx = (self.y - self.t) / batch_size
