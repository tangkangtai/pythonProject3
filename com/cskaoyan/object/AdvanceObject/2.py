class Student(object):

    def get_score(self):
        return self._score

    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an integer')

        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')

        self._score = value

s = Student()
s.set_score(60)
score = s.get_score()
print(score)

# s.set_score(999)

#---------------------
print('-----------------------')
#---------------------


#   @property装饰器  负责把一个方法 变成 属性调用
class Student_1(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self,value):

        if not isinstance(value,int):
            raise ValueError('score must be an integer')

        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100')

        self._score= value

s1 = Student_1()
s1.score = 60
print(s1.score)  #实际转化为s.get_score()

#-------------------------
print('---------------')
#-------------------------

class Student(object):
#birth是可读写属性
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self,value):
        self._birth = value

#age是一个只读属性
    @property
    def age(self):
        return 2020 - self._birth

