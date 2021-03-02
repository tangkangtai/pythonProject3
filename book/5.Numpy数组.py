import numpy as np

# 要生成Numpy数组，需要使用np.array()方法
# np.array()接收Python列表作为参数,生成Numpy数组
x = np.array([1.0,2.0,3.0])
print(x)

print(type(x))

# Numpy的算术运算
x = np.array([1.0,2.0,3.0])
y = np.array([2.0,4.0,6.0])

print(x + y)

print(x - y)
#   element-wise product
print(x * y)

print(x / y)

#   单一标量运算
x = np.array([1.0,2.0,3.0])
print(x / 2.0)

A = np.array([[1,2],[3,4]])
print(A)

print(A.shape)

print(A.dtype)

B = np.array([[3,0],[0,6]])
print(A + B)

print(A * B)
#   标量乘法
print(A * 10)

#   广播
A = np.array([[1,2],[3,4]])
B = np.array([10,20])
print(A * B)
print('---------------')
#   元素访问
X = np.array([[51,55],[14,19],[0,4]])
print(X)

print(X[0])

print(X[0][1])

print('----------------')
X = X.flatten() # 将X转换为一维数组
# print(X)
# print(np.array([0,2,4]))
# print(X[np.array([0,2,4])])
# print(X[[0,2,4]])

print(X > 15)
print(X[X > 15])
