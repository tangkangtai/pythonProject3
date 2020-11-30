import numpy as np


class Dropout:
    def __init__(self, dropout_ratio=0.5):
        self.dropout_ratio = dropout_ratio
        self.mask = None

    def forward(self, x, train_flg=True):
        # 每次正向传播时， self.mask 中都会以 False 的形式保
        # 存要删除的神经元。 self.mask 会随机生成和 x 形状相同的数组，并将值比
        # dropout_ratio 大的元素设为 True

        #反向传播时的行为和ReLU相同
        if train_flg:
            self.mask = np.random.rand(*x.shape) > self.dropout_ratio
            return x * self.mask
        else:
            return x * (1.0 - self.dropout_ratio)

    def backward(self, dout):
        return dout * self.mask
