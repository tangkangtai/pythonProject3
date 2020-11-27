import json

d = dict(name='Bob',age = 20, score = 86)

#把一个python对象变为一个json，dumps()方法返回一个str 内容就是标准的json ,
# dump()方法可以直接把json写入一个file-like object
#------------------------------
#把json对象反序列化为python对象  用loads()或者对应的load()方法
#前者把json的字符串反序列化 后者从file-like Object中读取字符串反序列化
print(json.dumps(d))

json_str = ' {"age":20,"score":88,"name":"Bob"} '
#json标准规定json编码是utf-8
json.loads(json_str)


class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score
    #
    # def __str__(self):
    #     return 'student object'

def student2dict(std):
    return {
        'name':std.name,
        'age': std.age,
        'score':std.score
    }

s = Student('Bob',20,88)
#默认情况 dumps()方法不知如何将student实例变为一个json的{}对象
#可选参数default 就是把任意一个对象变成一个可序列化为json的对象
print(json.dumps(s, default=student2dict))

#通常class的实例都有一个__dict__属性  他就是一个dict 用来存储实例变量
# (少数例外，比如定义了__slots__的class)
print(json.dumps(s,default=lambda  obj : obj.__dict__))


#同样道理，把json反序列化为一个student对象实力 loads()方法首先转换出一个dict对象
#通过传入object_hook函数负责把dict转换为Student实例
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age":20,"score":88,"name":"Bob"}'
print(json.loads(json_str, object_hook=dict2student)) #返回一个student对象

#json.dumps()提供一个ensure_ascii参数

obj = dict(name = '小明', age =20)
s1 = json.dumps(obj, ensure_ascii=False)
s2 = json.dumps(obj, ensure_ascii=True)
print(s1)
print(s2)



