#base64
#是一种用64个字符来表示任意二进制数据的方法
#对于二进制数据进行处理 每3个字节一组 一共是3*8=24bit 划分4组 每组6个bit
#根据数字索引 然后查表 获得相应的4个字符 就是编码后的字符串
# #2 * 2 * 2 * 2 * 2 * 2 = 2^6
#如果编码的二进制数据不是3的倍数 Base64用\x00字节在末尾补足后
# 再在编码的末尾加上1个或2个=号 表示补了多少字节 解码的时候 会自动去掉
import base64
print(pow(2,6))

print(base64.b64encode(b'binary\x00string'))

print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))

#标准的Base64编码后可能出现字符+和/      在url中不能直接作为参数
#所以又有一种'urlsafe'的base64编码  其实就是把字符 + 和 / 分别变成 - 和 _

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))

print(base64.urlsafe_b64decode(b'abcd--__'))
#Base64是一种通过查表的编码方法，不能用于加密，即使使用自定义的编码表也不行

#Base64是一种任意二进制到文本字符串的编码方法 常用语URL，Cookie 网页中传输少量二进制数据

#写一个能处理去掉=的base64解码函数
def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s += b'='

    return base64.b64decode(s)