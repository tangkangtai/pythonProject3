
import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.random.randn(1000, 100)
node_num = 100
hidden_layer_size = 5
activations = {}

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i-1]

    w = np.random.randn(node_num, node_num) * 1
    # w = np.random.randn(node_num, node_num) * 0.01 #标准差为0.01的高斯分布
    z = np.dot(x, w)

    a = sigmoid(z)
    activations[i] = a

for i, a in activations.items():
    #   i= 0,1,2,....
    # pyplot.subplot作用是把一个绘图区域分布多个小区域
    #   第一个参数 图的行数， 第二个参数 图的列数， 第三个参数，第几行第几列第几副图
    plt.subplot(1, len(activations), i+1)
    plt.title(str(i+1) + "-layer")
    #   第一个参数，数组或元祖， 第二个 为柱子， 第三个是 范围
    plt.hist(a.flatten(), 30, range=(0,1))
plt.show()