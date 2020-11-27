
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print("Flying...")

class Animal(object):
    pass

class Mammal(object):
    pass

class Dog(Animal,Runnable):
    pass

class Bat(Mammal, Flyable):
    pass

