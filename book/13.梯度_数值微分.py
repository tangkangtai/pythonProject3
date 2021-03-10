import numpy as np
import matplotlib.pylab as plt

#   求梯度
def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x) # 生成和x形状相同的数组(全0)

    for idx in range(x.size):
        tmp_val = x[idx]

        # f(x+h)的计算
        x[idx] = tmp_val + h
        fxh1 = f(x)

        # f(x-h)的计算
        x[idx] = tmp_val - h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val #还原值
    return grad

x = np.array([3.0,4.0])
print(x)
print(x.size)

#
# def numerical_diff(f, x):
#     h = 1e-4
#     return (f(x + h) - f(x - h)) / (2 * h)
#
#
# # 例子
# def function_1(x):
#     return 0.01*x**2 + 0.1*x
#
# def tangent_line(f, x):
#     d = numerical_diff(f,x)
#     print(d)
#     y = f(x) - d*x
#     return lambda t: d*t + y
#
# x = np.arange(0.0,20.0,0.1)
# y = function_1(x)
#
# plt.xlabel("x")
# plt.ylabel("f(x)")
#
# tf = tangent_line(function_1, 5)
# y2 = tf(x)
#
# plt.plot(x, y)
# plt.plot(x, y2)
# plt.show()