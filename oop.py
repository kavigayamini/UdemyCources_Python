
class Dog:
    name = ""
    breed = ""
    owner = ""
    serial_number =10
    

#object
#x=list()
x = Dog()
x.name = "Scooby"
x.breed = "Unknown"
x.owner = "Shaggy"
x.serial_number=100



print(Dog.__dict__)
print(x.__dict__)

y = Dog()
y.name = "Dripple"

print(y.breed)
print(y.__dict__)