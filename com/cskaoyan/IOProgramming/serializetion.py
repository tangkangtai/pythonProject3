import codecs
#序列化
#我们把变量从内存中变成可存储或传输的过程称之为  序列化
import pickle

d = dict(name = 'Bob',age = 20, score = 88)

print(d)
 #pickle.dumps(s) 把任意对象序列化成bytes
#或者这届通过pickle.dump()直接把对象序列化后写入 file-like Object
print(pickle.dumps(d))

# f = open('e:/pytest.txt','wb')
# pickle.dump(d, f)
# f.close()
#
# f = open('e:/pytest.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

with codecs.open('e:/pytest.txt','rb') as f:
    d = pickle.load(f)
#当然这个变量和原来的变量是完全不相干的对象 他们只是内容相同而已
print(d)
