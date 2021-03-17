
import numpy as np

class Dropout:
    def __init__(self, dropout_ratio=0.5):
        self.dropout_ratio = dropout_ratio
        self.mask = None


# 每次正向传播时， self.mask 中都会以 False 的形式保
# 存要删除的神经元。 self.mask 会随机生成和 x 形状相同的数组，并将值比
# dropout_ratio 大的元素设为 True 。反向传播时的行为和ReLU相同。也就是说，
# 正向传播时传递了信号的神经元，反向传播时按原样传递信号；
    # 正向传播时,没有传递信号的神经元，反向传播时信号将停在那里
    def forward(self,x,train_flg = True):
        if train_flg:
            self.mask = np.random.rand(*x.shape) > self.dropout_ratio
            return x * self.mask
        else:
            return x * (1.0 - self.dropout_ratio)

    def backward(self, dout):
        return dout * self.mask