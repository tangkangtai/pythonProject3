
#-----------迭代-----
#----有序元素 确实有索引----
L = ['Adam', 'Lisa', 'Bart', 'Paul']
#---enumerate 迭代--
#enumerate()函数把['Adam','Lisa','Bart','Paul'] 变为 [(0,'Adam'),()....]


#索引迭代也不是真的按索引访问，而是由 enumerate()函数自动把每个元素变成 (index, element) 这样的tuple，
# 再迭代，就同时获得了索引和元素本身
for index ,name in enumerate(L):
    print(index, '-' ,name)


L = ['Adam', 'Lisa', 'Bart', 'Paul']

for index, name in enumerate(L):
    print(index+1, '-', name)

print('----------------')

for index, name in zip(range(1, len(L) + 1), L):
    print(index, '-', name)


#dict的迭代
d = {'Adam':95,'Lisa':85,'Bart':59}
print(d.values())

for i in d.values():
    print(i)
#itervalues()方法迭代
d = {'Adam':95, 'Lisa':85, 'Bart':59}
print(d.items())

for key, value in d.items():
    print(key, ':', value)



print(d.items())


L = ['Adam','Lisa','Bart']
L[2] = 'Paul'
print(L)

L[-1] = 'Paul'
print(L)


L = ['Adam','Lisa','Bart','Paul']
x = L.pop()
print(x)
print(L)

print(L.pop(1))
print(L)
