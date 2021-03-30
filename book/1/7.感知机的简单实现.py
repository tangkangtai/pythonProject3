import numpy as np
x = np.array([0,1])
w = np.array([0.5, 0.5])
b = -0.7

print(x * w)

print(np.sum(x * w) + b)


def AND(x1, x2):
    w1, w2, theta = 0.5, 0.5, 0.7
    tmp = x1 * w1 + x2 * w2
    if tmp <= theta:
        return 0
    elif tmp > theta:
        return 1


# 异或门的实现
