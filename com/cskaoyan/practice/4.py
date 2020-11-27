d = {'Adam' : 95,'Lisa' : 85,'Bart' : 59}

print(d['Adam'])

#print(d['Paul'])

if 'Paul' in d:
    print(d['Paul'])

print(d.get('Bart'))

print(d.get('Paul')) #没有则返回None

#dict的第一个特点是查找速度快，无论dict有10个元素还是10万个元素，
#查找速度都一样。而list的查找速度随着元素增加而逐渐下降


#key不能重复

#而且为无序
print(d)
#key的元素必须不可变
e = {
    '123' : [1,2,3],
    123: '123',
    ('a','b') : True  #tuple对象每个元素是不可变对象 ，即可做key
}

print(e)

#-------------------------------
#添加内容
d['Paul'] = 72
print(d)

d['Bart'] = 60
print(d)
#-------------------------
f = {'Adam':95,'Lisa':85,'Bart':59}
for key in d:
    print(key)

#-----------------set--自动去重------------------
s = set(['A','B','C','C'])
print(s)
length = len(s)
print(length)

#-----------无法通过索引访问-----------------------------
s = set(['Adam','Lisa','Bart','Paul'])
print(s)

print('Bart' in s)
print('Bill' in s)
#----------set存储的元素和dict的key类似 必须是 不变的对象------------------------------
weekdays = set(['MON','TUE','WED','THU','FRI','SAT','SUN'])
x = '???'
if x in weekdays:
    print('input ok')
else:
    print('input error')


#-----------遍历set集合---------------------------
s = set(['Adam','Lisa','Bart'])
for name in s:
    print(name)

#-----更新list------------
s = set([1,2,3])
print(s)
s.add(4)
print(s)

#-------add--------------
s = set([1,2,3])
s.add(3)
print(s)

#------------remove----------
s = set([1,2,3,4])
s.remove(4)
print(s)
#--------删除不存在的元素会报错-----
#----remove前需要判断------
s.remove(4)
