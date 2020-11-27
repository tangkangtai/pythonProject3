from io import StringIO,BytesIO

f= StringIO()
print(f.write('hello')) #返回写入的字符个数
f.write(' ')
f.write('world')

#getvalue()方法用于获得写入后的str
print(f.getvalue())

f = StringIO('hello!\nHi!\nGoodbye!')
while True:

    s= f.readline()
    if s == '':
        break
    print(s.strip())

f = BytesIO()
f.write('中文'.encode('utf-8')) #写入的不是str 而是经过utf-8编码的bytes
print(f.getvalue())


f = BytesIO(b'\xe4\xb8\xad\xe6\x96\87')
print(f.read())


