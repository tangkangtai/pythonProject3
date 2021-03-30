from numpy import array
from numpy.linalg import inv,solve

A = array([[4.0,-2.0,1.0],[-2.0,4.0,-2.0],[1.0,-2.0,3.0]])

b = array([1.0,4.0,2.0])


#   求逆  Matrix inverse
print(inv(A))

# 求解 Ax = b
print(solve(A,b))