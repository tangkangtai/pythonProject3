
#----------列表切片---
L = ['Adam','Lisa','Bart','Paul']

print(L[0])


r = []
n = 3
for i in range(3):
    r.append(L[i])

print(r)
print('--------------')
#---取元素 0,3  但不包括3
print(L[0:3])
print(L[:3])

print('--------------')
print(L[1:3])

#----重头取到尾-
print('-------------')
print(L[:])

#----切片操作的第三参数   表示每隔几个取一个--
print(L[::2])


print('---------------------------------')
#----------倒序切片----
L = ['Adam','Lisa','Bart','Paul']


print(L[-2:])
print(L[:-2])

print(L[-3:-1])

print(L[-4:-1:2])

#--------字符串的操作也能用切片---
print('ABCDEFG'[:3])
print('ABCDEFG'[-3:])
print('ABCDEFG'[::2])

