import sys, os

sys.path.append(os.pardir)
from com.common.util import im2col
import numpy as np


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
        col_W = self.W.reshpe(FN, -1).T  # 滤波器的展开
        out = np.dot(col, col_W) + self.b

        #   转换时使用了
        # NumPy的 transpose 函数。 transpose 会更改多维数组的轴的顺序
        out = out.reshape(N, out_h, out_w, -1).transpose(0, 3, 1, 2)

        return out
