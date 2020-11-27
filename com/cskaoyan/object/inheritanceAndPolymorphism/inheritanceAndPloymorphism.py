
class Animal(object):

    def run(self):
        print('Animal is running')

    def eat(self):
        print('Eating meat...')

class Dog(Animal):
    def run(self):
        print('dog is running')

class Cat(Animal):
    def run(self):
        print('cat is running')

class Tortoise(Animal):

    def run(self):
        print('Tortoise is running slowly...')

def run_twice(animal):
    animal.run()
    animal.run()


dog = Dog()
print(dog.run())

cat = Cat()
print(cat.run())


print(isinstance(dog,Animal))

run_twice(Dog())
run_twice(Cat())
run_twice(Animal())


