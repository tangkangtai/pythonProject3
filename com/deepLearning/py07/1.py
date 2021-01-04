import sys, os
import numpy as np

sys.path.append(os.pardir)
from com.common.util import im2col

# im2col(input_data, filter_h, filter_w, stride=1, pad =0)
#   input_data  由(数据量，通道，高，长)的4维数组构成的输入数据
#   filter_h    滤波器的高
#   filter_w    滤波器的长
#   stride      步幅
#   pad         填充

#           批的大小为1，通道大小为3的 7 * 7 的数据
x1 = np.random.rand(1, 3, 7, 7)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1.shape)  # (9,75)

#
x2 = np.random.rand(10, 3, 7, 7)
col2 = im2col(x2, 5, 5, stride=1, pad=0)
print(col2.shape)  # (90, 75)
