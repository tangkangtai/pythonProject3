#list


L = ['Adam','Lisa','Bart']


#----------append方法添加----
L.append('Paul')
print(L)

#------insert()插入方法---
L.insert(0,'Paul_plus')
print(L)

#按索引访问
print(L[0])
print(L[1])

L = []
for x in range(1,11):
    L.append(x*x)
print(L)

#列表生成式
def toUppers(L):
    return [i.upper() for i in L if isinstance(i,str)]

print(toUppers(['Hello','world',101]))


