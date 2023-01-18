import random
from  sty import *
"""
Functions in Python are blocks of organized, reusable code that is used to perform a single, related action. They provide better modularity for your application and a high degree of code reusability. Python Functions are declared with the "def" keyword and can accept arguments and return values. Functions can be called by mentioning the argument name (keyword argument) or by passing the values directly. The return statement is used to return values from a function. Python also provides several built-in functions which can be used directly in our program.

I would say that a function is like a machine that can help us do something. We tell the machine what we want it to do, and it does it for us. For example, if we want to add two numbers together, we can tell the machine to do it for us and it will add them together. This is like a function in Python, except it can do more than just add numbers.

organize our code and split it into tasks.
reduce long blocks of code into a single command, avoiding repetition.
a function is a set of instructions to perform a specific task.
for ex:
    def eat_cookie():
        open mouth
        insert cookies 
        chew
        swallow
        return energy
    def eat_cookie():
        energy = open_mouth + insert_cookies + chew + swallow
        return energy
"""
def mulitply():
    a=2
    b=3
    return a*b
print(mulitply())

def multiply(a,b):
    return a * b
print(multiply(2,4))

def about_me(name,profession,pet):
    print("Hi my name is",name)
    print("I am a",profession)
    print("and I have a",pet)
print(about_me("Shaban","Software developer","monkey"))    


def generateRGB():
        red = random.randint(0,256)
        green = random.randint(0,256)
        blue  = random.randint(0,256)
        return red,green,blue

def generateColour(red,green,blue):
    return fg(red,green,blue)

red,green,blue = generateRGB()
colour=generateColour(red,green,blue)
print(colour,"Just some colors")
