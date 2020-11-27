import numpy as np

#----zip()函数------

a = [1,2,3,4,5]
b = (1,2,3,4,5)
c = np.arange(5)
d = 'zhang'
zz = zip(a,b,c,d) #返回zip对象
print(list(zz))

#无参zip
zz = zip()
print(list(zz))

#只有一个参数
a = [1,2,3]
zz = zip(a)
print(list(zz))

#多参数 长度不一
a = [1,2,3]
b = [1,2,3,4]
c = [1,2,3,4,5]
zz = zip(a,b,c)
print(list(zz))


#------zip()与*操作符---unzip一个列表-----
a = [1,2,3]
b = [4,5,6]
c = [7,8,9]
zz = zip(a,b,c)
print(list(zz))

x,y,z = zip(* zip(a,b,c))
print(x)
print(y)
print(z)




