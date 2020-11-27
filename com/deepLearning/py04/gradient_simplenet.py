import sys, os

sys.path.append(os.pardir)
import numpy as np

from com.common.functions import softmax, cross_entropy_error
from com.common.gradient import numerical_gradient


class simpleNet(object):

    def __init__(self):
        # numpy.random.rand()产生从[0,1)之间的随机数，没有负值
        # numpy.random.randn()产生服从正态分布的随机数 会出现负值
        # 生成指定维度的数据 在[0,1)之间
        self.W = np.random.randn(2, 3)

    def predict(self, x):
        return np.dot(x, self.W)

    def loss(self, x, t):
        z = self.predict(x)
        y = softmax(z)
        loss = cross_entropy_error(y, t)

        return loss


# print(simpleNet)

net = simpleNet()


def f(W):
    return net.loss(x, t)


dW = numerical_gradient(f, net.W)

#----------------------------------
f1 = lambda w: net.loss(x, t)
dW = numerical_gradient(f, net.W)
#----------------------------------

print(net.W)
print('----------------')
x = np.array([0.6, 0.9])
p = net.predict(x)
print(p)

print('----------')
print(np.argmax(p))

t = np.array([0, 0, 1])
print(net.loss(x, t))
