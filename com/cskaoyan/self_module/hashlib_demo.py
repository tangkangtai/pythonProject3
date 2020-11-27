#hashlib

import hashlib,random
#hashlib 提供了常见的摘要算法 MD5,SHA1
#摘要算法 又称  哈希算法 散列算法

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

#如果数据量很大 可以分块调用update()最后计算的结果是一样的:

md5_1 = hashlib.md5()
md5_1.update('how to use md5 in '.encode('utf-8'))
md5_1.update('python hashlib?'.encode('utf-8'))

print(md5_1.hexdigest())


#另一种常见的摘要算法 SHA1  与MD5
#sha1更安全的算法是sha256和sha512 不过越安全的算法不仅越慢 而且摘要长度更长
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())



#设置一个验证用户登录的函数 根据用户输入的口令是否正确 返回True或者False
db = {
    'michael':'',
    'bob':'',
    'alice':''
}
def login(user,password):
    password_md5 = hashlib.md5(password.encode('utf-8')).hexdigest()

    if db[user] == password_md5:
        return True
    else:
        return False


def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        #chr函数 用一个整数做参数 返回对应的一个字符
        self.salt = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = get_md5(password + self.salt)


db = {
    'Michael': User('michael','123456'),
    'bob' : User('bob','abc999'),
    'alice':User('alice','alice2008')
}

def login(username,password):
    user = db[username] #User对象

    return user.password == get_md5(password + user.salt)
