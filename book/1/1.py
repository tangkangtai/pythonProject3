
# 列表既数组 ， 可修改
a = [1,2,3,4,5]
print(a)

print(len(a))

print(a[0])
print(a[4])
a[4] = 99
print(a)


# 列表的切片操作
#   获取索引为0到2(不包括2)的元素
print(a[0:2])
#   获取 索引1到最后一个元素
print(a[1:])

#
print(a[:3])

print(a[:-1])

# 获取从第一个元素到最后一个元素的前二个元素之间的元素
print(a[:-2])