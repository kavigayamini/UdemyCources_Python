class Animal:
    def __init__(self):
        self.breed = "Unknown"

    def talk(sel,message):
        print("Animals are talking")

    def move(self):
        print("Animal is moving")

class Dog(Animal):
    def __init__(self):
        super(Dog,self).__init__()
        print("Dog is born")

    def talk(self,message):
        super(Dog,self).talk(message)
        print("Dog is barking",message)  
x = Dog()
x.talk("Hello")
