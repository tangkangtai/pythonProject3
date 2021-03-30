import numpy as np


#   ReLU(Rectified Linear Unit)修正线性函数

def relu(x):
    return np.maximum(0, x)
