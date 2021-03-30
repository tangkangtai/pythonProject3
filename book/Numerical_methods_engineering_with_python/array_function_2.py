
import numpy as np
#   点乘，内积，外积
#   区分 numpy.dot, numpy.inner, numpy.outter

x = np.array([7,3])
y = np.array([2,1])
A = np.array([[1,2],[3,2]])
B = np.array([[1,1],[2,2]])


print(np.dot(x,y))
print(np.dot(A,x))
print(np.dot(A,B))

print('----------------------------')

print(np.inner(x,y))
print(np.inner(A,x))
print(np.inner(A,B))

print('------------------------------')

print(np.outer(x,y))
print(np.outer(A,x))
print(np.outer(A,B))

