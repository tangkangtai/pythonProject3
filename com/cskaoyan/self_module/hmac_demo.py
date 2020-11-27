#hma替代我们自己实现的salt算法
#hamc keyed-hashing for message Authentication
import hmac
message = b'hello,world!'
key = b'secret'

#需要注意的是  key和message都是bytes类型 str类型需要首先编码为bytes

h = hmac.new(key, message,digestmod='MD5')
#如果消息很长 可以多次调用h.update(msg)
print(h.hexdigest())

#使用hmac和普通hash算法非常相似  hmac输出的长度和原始哈希算法的长度一致

#将上一节的salt改为标准的hamc算法,验证用户口令
import hmac, random

def hmac_md5(key, s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),'MD5').hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.key = ''.join([chr(random.randint(48,122)) for i in range(20)])
        self.password = password

db = {
    'michael' : User('michael','123456'),
    'bob' : User('bob','abc999'),
    'alice' : User('alice','alice2008')
}

def login(username, password):
    user = db[username]
    return user.password == hmac_md5(user.key, password)

test_x = [random.randint(10,100) for i in range(10)]
print(test_x)

