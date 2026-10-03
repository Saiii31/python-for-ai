class Dog: # Define a class named Dog
    def __init__(self, name, age): # Constructor method to initialize the object
       self.name = name # self = it tells that the variable belongs to the object, not a local variable
       self.age = age # self refers to the instance of the class, allowing access to its attributes and methods
       
    def bark(self):  # Method to make the dog bark
        return "Woof!"

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        return "Meow!"

Dog1 = Dog("Buddy", 3)  # Create an instance of Dog
Dog1.name # Access the name attribute of Dog1
Dog1.age
Dog1.bark() #Call the bark method of Dog1

Cat1 = Cat("Whiskers", 2) # Create an instance of Cat
Cat1.name
Cat1.age
Cat1.meow()
