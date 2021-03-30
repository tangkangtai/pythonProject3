import sys, os
from collections import OrderedDict

sys.path.append(os.pardir)
from book import Convolution_,ReLU_,Pooling_,Affine_,SoftmaxWithLoss_

import numpy as np

class SimpleConvNet:

    def __init__(self, input_dim=(1,28,28),
                 conv_param={
                    'filter_num':30,
                     'filter_size':5,
                     'pad':0,'stride':1},
                 hidden_size=100,
                 output_size=10,
                 weight_init_std=0.01):

#   这里将由初始化参数传入的卷积层的超参数从字典中取了出来（以方便后面使用），
#   然后，计算卷积层的输出大小
        filter_num = conv_param['filter_num']
        filter_size = conv_param['filter_size']
        filter_pad = conv_param['pad']
        filter_stride = conv_param['stride']

        input_size = input_dim[1]

        conv_output_size = (input_size - filter_size + 2 * filter_pad) / \
            filter_stride + 1

        pool_out_size = int(filter_num * (conv_output_size / 2) * (conv_output_size / 2))

#       权重参数的初始化部分
        self.params = {}

        self.params['W1'] = weight_init_std * \
                            np.random.randn(filter_num,input_dim[0],filter_size,filter_size)
        self.params['b1'] = np.zeros(filter_num)


        self.params['W2'] = weight_init_std * \
                            np.random.randn(pool_out_size, hidden_size)
        self.params['b2'] = np.zeros(hidden_size)


        self.params['W3'] = weight_init_std * \
                            np.random.randn(hidden_size, output_size)
        self.params['b3'] = np.zeros(output_size)



    #   生成必要的层
        self.layers = OrderedDict()
        self.layers['Conv1'] = Convolution_(self.params['W1'],
                                            self.params['b1'],
                                            conv_param['stride'],
                                            conv_param['pad'])
        self.layers['Relu1'] = ReLU_()
        self.layers['Pool1'] = Pooling_(pool_h=2, pool_w=2, stride=2)

        self.layers['Affine1'] = Affine_(self.params['W2'], self.params['b2'])
        self.layers['Relu2'] = ReLU_()

        self.layers['Affine2'] = Affine_(self.params['W3'], self.params['b3'])

        self.last_layer = SoftmaxWithLoss_()

#   参数 x 是输入数据， t 是教师标签。用于推理的 predict 方法从头
# 开始依次调用已添加的层，并将结果传递给下一层。在求损失函数的 loss
# 方法中，除了使用 predict 方法进行的 forward 处理之外，还会继续进行
# forward 处理，直到到达最后的 SoftmaxWithLoss 层。
    def predict(self, x):
        for layer in self.layers.values():
            x = layer.forward(x)

        return x

    def loss(self, x, t):
        y = self.predict(x)
        return self.last_layer.forward(y, t)

    #   基于误差反向传播法求梯度的代码实现

    def gradient(self, x, t):
        #   forward
        self.loss(x, t)

        # backward
        dout = 1
        dout = self.last_layer.backward(dout)

        layers = list(self.layers.values())
        layers.reverse()

        for layer in layers:
            dout = layer.backward(dout)

        # 设定
        grads = {}
        grads['W1'] = self.layers['Conv1'].dW
        grads['b1'] = self.layers['Conv1'].db

        grads['W2'] = self.layers['Affine1'].dW
        grads['b2'] = self.layers['Affine1'].db

        grads['W3'] = self.layers['Affine2'].dW
        grads['b3'] = self.layers['Affine2'].db

        return grads



