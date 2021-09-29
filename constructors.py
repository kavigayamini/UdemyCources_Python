    
class Dog:
    age = 10

    #override the constructor
    def __init__(self,name,age,owner):
        print("A dog is born")
        self.name=owner
        self.age=age
        self.owner=owner

    def bark(self):
        print("woof woof",self.name)

#object
#x=list()
x = Dog("Scooby",5,"Shaggy")
#x.init()
x.bark()