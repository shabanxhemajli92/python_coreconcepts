"""
A lambda function is an anonymous function (i.e., defined without a name) that can take any number of arguments but, unlike normal functions, evaluates and returns only one expression. A lambda function in Python has the following syntax: lambda parameters: expression.

Lambda functions are intended as a shorthand for defining functions that can come in handy to write concise code without wasting multiple lines defining a function. They are also known as anonymous functions, since they do not have a name unless assigned one.

One of the foremost common use cases for lambdas is in functional programming as Python supports a paradigm (or style) of programming referred to as functional programming. It allows you to supply a function as a parameter to a different function (for example, in map, filter, etc.).
Lambda functions take infinite amount of parameters.
"""
#normal function
def function(x):
    return x+5
print(function(5)) 
#lambda
func2=lambda x:x+5 
print(func2(3))  
func3=lambda x:x//2
print(func3(10))
#using lambda within another function
def add(x):
    funct= lambda x:x+1
    return funct(x)+1
print(add(4))    
#map functions
a=[1,23,36,55,99,77]
new_list=list(map(lambda x:x+4,a))
a_new_list=list(filter(lambda x:x%2==0,a))
print(new_list)
print(a_new_list)