import numpy as np

A = np.array([[4,-2,1],[-2,4,-2],[1,-2,3]],float)
b = np.array([1,4,3],float)


print(A)
#   输出对角线元素
print(np.diagonal(A))

print(np.diagonal(A,1))

#   主对角线的和
print(np.trace(A))

print(np.argmax(b))

print(np.argmin(A, axis=0))


print('------------------------')
#   单位矩阵
print(np.identity(3))