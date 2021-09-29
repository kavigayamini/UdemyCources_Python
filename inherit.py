class Animal:
    def __init__(self)-> None:
        self.breed = "Unknown"

    def talk(self):
        print("Animals are talking")

    def move(self):
        print("Animal is moving")

class Dog(Animal):
    def bark(self):
        print("woof")

    def walk(self):
        print("Dog is walking")

class Cat(Animal):
    def meow(self):
        print("Meow")
    def walk(self):
        print("Cat is walking")
a = Animal()
a.talk()
print(a.__dict__)

x = Dog()
x.talk()
print(x.__dict__)

y = Cat()
y.talk()
print(y.__dict__)