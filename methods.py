    
class Dog:
    age = 10

    def init(self):
        self.name="Unknown"
        self.age=0
        self.owner="Someone"

    def bark(self):
        print("woof woof",Dog.age)

#object
#x=list()
x = Dog()
x.init()


x.bark()