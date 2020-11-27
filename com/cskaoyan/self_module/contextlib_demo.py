#contextlib

try:
    f = open('e:/pytest.txt','rb',)
    f.read()
finally:
    if f:
        f.close()

#-----------------------
#简化为
with open('e:/pytest.txt','rb') as f:
    f.read()

#-------------------------------
# __enter__  __exit__
#-------------------------------
class Query(object):
    def __init__(self,name):
        self.name = name

    def __enter__(self):
        print('Begin')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('End')

    def query(self):
        print('Query info about %s...' %self.name)

with Query('Bob') as q:
    q.query()

print('------------------------')
#----------------------------------
from contextlib import contextmanager
class Query_p(object):
    def __int__(self,name):
        self.name = name

    def query(self):
        print('Query info about %s...' % self.name)

#contextmanager
#contextmanager  这个decorator接受一个generator 用yield语句 把with...as var把变量输出出去
# 然后 with语句 就可以正常工作了
@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
#有时候 我们希望在某地段代码执行前后自动执行特定代码 也可以使用 @contextmanager实现
with create_query('Bob') as q:
    q.query()

#---------------------------------
print('--------------------------')
#---------------------------------

@contextmanager
def tag(name):
    print("<%s>" % name)
    yield
    print("</%s>" % name)

with tag("h1"):
    print('hello')
    print("world")

#------------------
print('---------------')
#------------------
#  @closing
#如果一个对象没有出现上下文 我们就不能把它用于with语句
#这个时候 可以用closing()来把该对象变成上下文对象
#closing的作用就是把任意对象变为上下文对象 并支持with语句

from contextlib import closing
from urllib.request import urlopen
#urllib.equest.urlopen(url,data=None,[timeout]*)函数 用于实现对目标url的访问
#url需要打开的网址
#data: Post提交的数据
#timeout设置网站的访问超时时间
#page的数据格式bytes类型  需要decode()解码 转换成str
with closing(urlopen('https://www.python.org')) as page:
    for line in page:
        print(line)

