#xml

#在python中使用SAX解析XML非常简洁
#通常我们关心的是start_element,end_element,char_data,准备好这3个函数

#例
#当SAX解析器读到一个节点时     <a href="/">python</a>
#会产生3个事件
#1.start_element事件  在读取<a href="/">时
#2.char_data事件 在读取 python时
#3.end_element事件  在读取</a>时

from xml.parsers.expat import ParserCreate

class DefaultSaxHandler(object):
    def start_element(self,name,attrs):
        print('sax:start_element: %s, attrs: %s' % (name,str(attrs)))

    def end_element(self,name):
        print('sax:end_element:%s' % name)

    def char_data(self,text):
        print('sax:char_data: %s' % text)

xml = r'''<?xml version="1.0"?>
<ol>
    <li><a href="/python">Python</a></li>
    <li><a href="/ruby">Ruby</a></li>
</ol>
'''
#解析器负责读取xml文档 并向事件处理器发送事件，如元素开始跟元素结束事件
#而事件处理器则负责对事件作出相应 对传递的xml数据进行处理

#处理器实例
handler = DefaultSaxHandler()
#解析器实例
parser = ParserCreate()
parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data
parser.Parse(xml)