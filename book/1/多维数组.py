import numpy as np
A = np.array([1, 2, 3, 4])
print(A)

# 数组的维数可以通过 np.dim() 函数获得
print(np.ndim(A))

# 数组的形状可以通过实例变量 shape 获得
print(A.shape)
#  A.shape 的结果是个元组（tuple）
print(A.shape[0])

B = np.array([[1,2],[3,4],[5,6]])
print(B)

print(np.ndim(B))

print(B.shape)


#---------------------------------------------------
print('------------矩阵乘积-------------------')
A = np.array([[1,2],[3,4]])
print(A.shape)

B = np.array([[5,6],[7,8]])
print(B.shape)

print(np.dot(A, B))
