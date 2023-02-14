'''
Object-Oriented Programming (OOP) is a programming paradigm that is based on the concept of "objects". An object is a collection of data and associated behaviors (methods) that can be manipulated and interacted with by other parts of a program.

In Python, you can define a class to create a blueprint for an object. A class is a user-defined data type that contains data and code to work with that data. Once you define a class, you can create one or more instances of that class, which are called objects. Each object has its own state (data) and behavior (methods).

For example, you can define a class called "Person" with attributes such as "name", "age", and "gender". You can then create objects (instances) of this class, each with their own unique values for these attributes. You can also define methods in the class, such as "speak" or "walk", which can be used to manipulate the object's state.

Encapsulation is a key concept in OOP, and it refers to the practice of bundling data and methods together within a class to hide the implementation details from the outside world. This provides a level of abstraction and helps to keep the code organized and easier to maintain.

Inheritance is another important concept in OOP that allows you to create a new class that is a modified version of an existing class. The new class inherits all the attributes and methods of the original class, and can also add or override them as needed. This allows you to reuse code and create more specialized classes.

Polymorphism is a third concept in OOP that refers to the ability of objects of different classes to be used interchangeably. This is achieved through the use of inheritance and method overriding, which allows different objects to respond to the same method in different ways.

In summary, OOP is a powerful programming paradigm that allows you to create complex, organized, and reusable code through the use of objects, classes, encapsulation, inheritance, and polymorphism.

'''
#example
class Human():
    def __init__(self,name,age,profession):
        self.name=name
        self.age=age
        self.profession=profession

    def process(self):
        return f"{self.name} is still not the version of him/her self"

    def maturity(self):
        return f"at {self.age} he/she is not mature"

    def achievement(self):
        return f"{self.profession} makes them an asset "

    def overall(self):
        return f"we can conclude that {self.name}, is a{self.profession} but for the {self.age} is not at the optimum"

                  

