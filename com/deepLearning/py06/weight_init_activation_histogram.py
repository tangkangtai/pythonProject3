import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


x = np.random.randn(1000, 100)
node_num = 100  # 隐藏层的节点
hidden_layer_size = 5  # 隐藏层
activations = {}  # 保存激活值(激活函数的输出数据)的结果

for i in range(hidden_layer_size):
    if i != 0:
        x = activations[i - 1]

    w = np.random.randn(node_num, node_num) * 1

    z = np.dot(x, w)
    a = sigmoid(z)
    activations[i] = a

# 绘制直方图
for i, a in activations.items():
    #子图   几行几列以及编号
    plt.subplot(1, len(activations), i + 1)
    plt.title(str(i + 1) + '-layer')
    #histogram直方图
    plt.hist(a.flatten(), 30, range=(0, 1))

plt.show()
