#json
#           json            python
# --------------------------------------
#           {}              dict
#           []              list
#           "string"        str
#           123.55          int 或 float
#           true/false      True/False
#           null            None

import json
d = dict(name = 'Bob', age = 20, score = 88)
#dumps()方法返回一个str 内容是一个标准的json
#类似的dump()方法可以直接把json写入一个file-like Object

json.dumps(d)

#========================================
json_str = '{"age":20,"score":88,"name":"Bob"}'
#loads()把json的字符串反序列化
#load()从file-like Object中读取字符串并反序列化
#json标准规定json编码是utf-8
json.loads(json_str)

# #=====================================
# class Student(object):
#     def __init__(self,name,age,score):
#         self.name = name
#         self.age = age
#         self.score = score
#
# def student2dict(std):
#     return {
#         'name':std.name,
#         'age':std.age,
#         'score':std.score
#     }
#
# s = Student('Bob',20,88)
#
# #不能直接序列化
# # print(json.dumps(s))
# print(json.dumps(s,default=student2dict))
#
# #下次遇到Teacher类实例 照样无法序列化为json 我们可以偷个懒 把任意class的实例变为dict
# print(json.dumps(s, default=lambda obj : obj.__dict__))
# #因为class的实例都有一个__dict__属性   他就是dict 用来存储 实例变量 (除了定义了__slots__的class)
#
#
# #反序列化为student,loads()方法首先转换出一个dict对象 然后我们传入object_hook函数负责把dict转换为Student实例
# def dict2student(d):
#     return Student(d['name'],d['age'],d['score'])
#
# json_str = '{"age":20,"score":88,"name":"Bob"}'
# print(json.loads(json_str,object_hook=dict2student))
#
#
# #测试 json.dumps()提供的ensure_ascii参数
# obj = dict(name='小明',age=20)
# s1 = json.dumps(obj, ensure_ascii=True)
# s2 = json.dumps(obj, ensure_ascii=False)
# print(s1)
# print(s2)

