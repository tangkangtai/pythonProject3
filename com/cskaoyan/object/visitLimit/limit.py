
#-----------访问限制--------------
class Student(object):
    def __init__(self, name, score):
        #  __变量名  实例变量  这样外部代码就不能随意修改对象内部的状态 访问限制保护
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s %s' % (self.__name,self.__score))

    # def set_score(self,score):
        # self.__score = score

    def set_score(self,score):
        if 0 <= score <= 100:
            self.__score = score
        else:#参数检验 避免无效参数
            raise ValueError('bad score')

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


bart = Student('Bart Simpson', 59)

#实例变量无法访问 报错
# print(bart.score)
# bart.score = 99
#
# print(bart.score)
# print(bart.get_score())
# print(bart.get_name())
