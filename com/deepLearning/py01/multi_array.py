import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
#恒等函数
def identity_function(x):
    return x

#softmax函数
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

A = np.array([1, 2, 3, 4])
print(A)

#获取数组维度
print(np.ndim(A))

#获取数组形状
print(A.shape)

print(A.shape[0])

#======================
print('---------------')
B = np.array([[1,2],[3,4],[5,6]])
print(B)

print(np.ndim(B))

print(B.shape)

#=========================
print('-----------------')

A = np.array([[1,2],[3,4]])
print(A.shape)

B = np.array([[5,6],[7,8]])
print(B.shape)

print(np.dot(A,B))
#=====================
print('------------')
A = np.array([[1,2],[3,4],[5,6]])
print(A.shape)

B = np.array([7,8])
print(B.shape)
print(np.dot(A,B))

#==============================
X = np.array([1.0,0.5])
W1 = np.array([[0.1,0.3,0.5],[0.2,0.4,0.6]])
B1 = np.array([0.1,0.2,0.3])

A1 = np.dot(X , W1) + B1
print(A1)
Z1 = sigmoid(A1)
print(Z1)

