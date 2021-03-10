import sys, os

sys.path.append(os.pardir)
import numpy as np


#   求梯度
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)  # 生成和x形状相同的数组(全0)

    for idx in range(x.size):
        tmp_val = x[idx]

        # f(x+h)的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2 * h)
        x[idx] = tmp_val  # 还原值
    return grad


#   2.交叉熵误差
#   log表示以e为底数的自然对数（log e ）。y k 是神经网络的输出，t k 是
#   正确解标签。并且，t k 中只有正确解标签的索引为1，其他均为0（one-hot表示）
def cross_entropy_error(y, t):
    delta = 1e-7
    return -np.sum(t * np.log(y + delta))


#   softmax函数
def softmax(x):
    c = np.max(x)
    exp_a = np.exp(x - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y


class simpleNet:

    def __init__(self):
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss


net = simpleNet()
print(net.W)

x = np.array([0.6, 0.9])
p = net.predict(x)

print(p)

print(np.argmax(p))  # 最大索引值

t = np.array([0, 0, 1])  # 正确解标签
print(net.loss(x, t))


def f(W):
    return net.loss(x, t)
#   f = lambda w: net.loss(x, t)
#   dW = numerical_gradient(f, net.W)

dW = numerical_gradient(f, net.W)
print(dW)
