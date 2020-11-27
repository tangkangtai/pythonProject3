
d = dict(name = 'Bob', age = 20, score = 88)
#这些变量数据存储在内存上

#我们把变量从内存中变成可存储或传输的过程称之为序列化

#尝试把一个对象序列化写入文件
import pickle
d = dict(name = 'Bob', age = 20,score = 88)
#pickle.dumps()方法把任意对象序列化成一个bytes
#然后就可以把这个bytes写入文件
pickle.dumps(d)
#-----------------------------
#或者用pickle.dump()直接把对象序列化后写入一个file-like Object:
f = open('e:/pytest.txt','wb')
pickle.dump(d, f)
f.close()

#当我们要把对象从磁盘读到内存时 可以先把内容读到一个bytes 然后用pickle.loads()方法
#反序列化出对象  ，也可以直接用 pickle.load()方法从一个file-like Object中直接反序列化出对象

f = open('e:/pytest.txt','rb')
d = pickle.load(f)
f.close()
print(d)




