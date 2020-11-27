import numpy as np

x = np.array([-1.0, 1.0, 2.0])
print(x)

y = x > 0
print(y)

#可以用astype()方法转换NumPy数组的类型。astype()方法通过参数指定期望的类型，
z = y.astype(np.int)
print(z)