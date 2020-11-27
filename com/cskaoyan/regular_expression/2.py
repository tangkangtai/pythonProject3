#分组  除了简单的判断是否匹配之外 正则表达式 还有提取子串的强大功能
#用()表示的就是要提取的分组
#   ^(\d{3})-(\d{3,8})$  分别定义了两个组 可以直接从匹配的字符串中提取出区号和本地号码
import re
m = re.match(r'(\d{3})-(\d{3,8})$','010-12345')
print(m)
#如果正则表达式定义组 就可以在match对象上用group()方法来提取子串
#group(0) 永远是原始字符串  group(1) ..group(2)..
print(m.group(0))
print(m.group(1))
print(m.group(2))

t = '19:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:'
             r'(0[0-9]1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)

print(m.groups())

#贪婪匹配(默认)
re.match(r'^(\d+)(0*)$','102300').groups()
#非贪婪匹配
re.match(r'^(\d+?)(0*)$','102300').groups()


#如果一个正则表达式需要用到很多次 我们可以预编译
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

# re_telephone.match('0101-12345').groups()

#验证Email地址的正则表达式
# someone@gamil.com
#bill.gates@microsoft.com

def is_valid_email(addr):
    if re.match(r'[a-z\.]+@[a-z]+\.com',addr):
        return True
    else:
        return False

print(is_valid_email('someone@gmail.com'))
print(is_valid_email('bill.gates@microsoft.com'))
print(is_valid_email('bob#example.com'))
print(is_valid_email('mr-bob@example.com'))

print('--------------------------------')

def name_of_email(addr):
    m = re.match(r'<?(\w+\s?\w+)>?(\s?\w+)?@(\w+\.\w+])$',addr)
    if m:
        return m.group(1)


