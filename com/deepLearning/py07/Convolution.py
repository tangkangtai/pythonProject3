import numpy as np
from com.common.util import im2col


class Convolution:

    def __init__(self, W, b, stride=1, pad=0):
        self.W = W
        self.b = b
        self.stride = stride
        self.pad = pad

    def forward(self, x):
        FN, C, FH, FW = self.W.shape
        N, C, H, W = x.shape
        out_h = int(1 + (H + 2 * self.pad - FH) / self.stride)
        out_w = int(1 + (W + 2 * self.pad - FW) / self.stride)

        col = im2col(x, FH, FW, self.stride, self.pad)
#这里通过 reshape(FN,-1) 将参数指定为 -1 ，这是
# reshape 的一个便利的功能。通过在reshape 时指定为 -1,reshape 函数会自
# 动计算 -1 维度上的元素个数，以使多维数组的元素个数前后一致。比如，
# (10, 3, 5, 5)形状的数组的元素个数共有750个,指定 reshape(10,-1)后，就
# 会转换成(10, 75)形状的数组。
        col_W = self.W.reshape(FN, -1).T  # 滤波器的展开
        out = np.dot(col, col_W) + self.b
        # 转换时使用了 NumPy的 transpose 函数。 transpose 会更改多维数组的轴的顺序
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        return out
