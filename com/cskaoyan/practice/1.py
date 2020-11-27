
t = ('Adam','Lisa','Bart')
#tuple 对象不支持修改
#t[0] = 'Paul'
# print(t)

#-------可变的tuple-----------
t = ('a','b',['A','B'])
L = t[2]
print(L)
L[0] = 'X'
L[1] = 'Y'
print(t)

#---------空的tuple--
t = ()
print(t)

#t = (1) #括号可能代表优先级  可能被python解释器计算为1
print(t)

t = (1,)
print(t)


t = (1,2,3,)
print(t)


