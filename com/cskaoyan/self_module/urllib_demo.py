#urllib提供了一系列的用于操作URL的功能

#urllib的request模块可以非常方便的抓取URL内容,
# 也就是发送一个GET请求到指定的页面然后返回HTTP的响应
from urllib import request

#加入对豆瓣的一个URL进行抓取 并返回响应
# with request.urlopen('https://news.sina.com.cn/') as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' %(k,v))
#
#     print('Data:',data.decode('utf-8'))


#---------------------------
#---------------------------
#如果我们要想模拟浏览器发送get请求 就需要使用Request对象 通过往Request对象添加HTTP头
#我们就可以把请求伪装成浏览器
req = request.Request('https://news.sina.com.cn/')
req.add_header('')#添加需要的请求头
with request.urlopen(req) as f:
    print('Status:',f.status,f.reason)
    for k, v in f.getheaders():
        print('%s: %s' %(k,v))

    print('Data:',f.read().decode('utf-8'))
#这是后半会返回适合iphone的移动版网页

#==============================
#==============================

#Post请求
#如果要以POST发送一个请求 只需要把参数data以bytes形式传入
from urllib import parse
print('Login to weibo.cn...')
email =input('Email:')
passwd = input('Password:')
login_data = parse.urlencode([
    ('username',email),
    ('password',passwd),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('ec',''),
    ('pagerefer','https://passport.weibo.cn/.........')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin','https://passport.weibo.cn')
req.add_header('User-Agent','...')
req.add_header('Referer','..')

with request.urlopen(req,data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)
    for k, v in f.getheaders():
        print('%s: %s' %(k,v))

    print('Data:',f.read().decode('utf-8'))

import json

def fetch_data(url):
    with request.urlopen(url) as f:
        data = f.read().decode('utf-8')
        return json.loads(data)