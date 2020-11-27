#object表示  Student类继承哪个类
class Student(object):
    pass

bart = Student()

print(bart)
print(Student)

bart.name = 'Bart Simpson'
print(bart.name)

#-------------------------------
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s %s' %(self.name,self.score))

    def get_grade(self):
        if self.score >= 90 :
            return 'A'
        elif self.score >= 60:
            return 'B'
        else:
            return 'C'

def print_score(std):
    print('%s %s' %(std.name,std.score))

bart = Student('Bart Simpson',59)
lisa = Student('Lisa',99)

print(bart.name,'--',bart.score)

print_score(bart)

bart.print_score()

print(lisa.name,lisa.get_grade())
print(bart.name,bart.get_grade())
