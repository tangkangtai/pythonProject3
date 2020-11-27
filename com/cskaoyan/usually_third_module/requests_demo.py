#相比python内置的urllib模块 用来访问网络资源
#更好的方案是使用requests 它是一个python第三方库 处理URL资源特别方便
#   $pip install requests  若失败，可加上sudo重试
import requests
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}
r = requests.get('https://www.douban.com/',headers=headers)
#需要设置请求头 不然返回418
#貌似反扒程序？

print(r.status_code) #418
print(r.text)

#--------------------------
print('--------------------------')
#--------------------------
r1 = requests.get('https://www.douban.com/search',params={'q':'python','cat':'1001'})
print(r1.url) #实际请求的url

print(r.encoding)#自动监测编码

print(r.content) #无论响应是文本还是二进制内容 我们可以用content属性获得bytes对象

#requests的方便之处还在于 对于特定类型的响应 例如json可以直接获取
# r.json()


#需要发送post请求  把get改为post即可 data参数作为post请求的数据
r3 = requests.post('https://',data={'form_email':'abc@example.com','form_password':'123456'})

#requests默认使用application/x-www-form-urlencodeed对post数据编码，如果要传递json数据 可以直接传入json参数
params = {'key':'value'}
url = 'https://www.douban.com'
r = requests.post(url,json=params)


#上传文件需要更加复杂的编码格式  requests把它简化成files参数
upload_files = {'file':open('report.xls','rb')}
r = requests.post(url,files=upload_files) #注意务必使用'rb'读取 这样获得的bytes才是文件的长度


r.headers
r.headers['Content-Type']
r.cookies['ts']#轻松获取指定cookie

#传入cookie  只需要准备一个dict传入cookie参数
cs = {'token':'12345','status':'working'}
r5 = requests.get(url,cookie=cs,timeout=1.0)

r =requests.get(url,timeout=2.5)