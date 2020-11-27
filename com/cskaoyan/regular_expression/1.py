#正则表达式

#      \d 可以匹配匹配一个数字
#      \w可以匹配一个字母或数字
#       .  可以匹配任意字符
#       *表示任意个字符(包括0个)
#       + 表示至少一个字符
#       ? 表示 0个或1个字符
#       {n} 表示n个字符
#       {n,m} 表示 n-m个字符
#--------------------------------
#[0-9a-zA-Z\_] 可以匹配一个数字 字母 或者下划线
#[0-9a-zA-Z\_]+表示匹配至少由一个数字 字母 或者下划线组成的字符串 'a100' '0_Z' 'Py300'
#[a-zA-Z\_][0-9a-zA-Z\_]*  可以匹配由字母或者下划线开头 后接任意个由一个数字，字母或者
#                                                  下划线组成的字符串

#[a-zA-Z\_][0-9a-zA-Z\_]{0,19}  限制了 1-20个字符  (前面一个字符  后面最多19个字符)

#   A|B  可以匹配A或者B     (p|P)ython   可以匹配'Python' 'python'
# ^表示行的开头       ^\d表示必须以数字开头
# $表示行的结束       \d$表示必须以数字结尾

#-------------------------------
#python提供的re模块  包含所有的正则表达式功能
#  注意  python的字符串本身也用\转义
import re
print(re.match(r'\d{3}\-\d{3,8}$','010-12345'))

re.match(r'\d{3}\-\d{3,8}$','010 12345')
#match()方法判断是否匹配 如果匹配成功 返回一个match对象 否则返回True
test = '用户输入的字符串'
if re.match(r'正则表达式',test):
    print('ok')
else:
    print('failed')

#------------------------
#切分字符串
print('a b    c'.split(' '))
#当无法识别连续空格
print(re.split(r'\s+','a b   c'))

print(re.split(r'[\s\,]+', 'a,b  c  d'))

print(re.split(r'[\s\,\;]+', 'a,b ;;   c  d'))


