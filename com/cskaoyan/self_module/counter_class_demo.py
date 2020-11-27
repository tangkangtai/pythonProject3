#Counter 类的演示
#计数器 用于追踪值得出现次数
import collections
obj = collections.Counter('aabbccc')
print(obj)


#elements()
print(sorted(obj.elements()))

for k in obj.elements():
    # 去除自动换行
    print(k, end = ' ')

print()


#most_common(指定一个参数n,列出前n个元素，不指定参数 则列出所有)
print(obj.most_common(2))

#items    (从dict类中继承的方法)
print(obj.items())
for k,v in obj.items():
    print(k,v)



#update增加元素
obj.update(['22','55'])
print(obj)

#subtract  原来的元素减去新传入的元素
obj.subtract(['22','55'])
print(obj)
