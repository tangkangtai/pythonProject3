class Man:
    def __init__(self, name):
        self.name = name
        print("Initialized!")

    def f1(self):
        print("Hello " + self.name + "!")

    def f2(self):
        print("Good-bye " + self.name + "!")


m = Man('David')
m.hello()
m.goodbye()
