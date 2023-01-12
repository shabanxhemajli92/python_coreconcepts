"""
Conditional statements in Python are used to perform different actions depending on whether a certain condition is true or false. They are used to control the flow of execution in a program, allowing the program to make decisions based on the input or the current state. The most common types of conditional statements in Python are if, elif (short for "else if"), and else. These statements are used in combination to test multiple conditions and execute different code depending on the results of those tests.
"""

"""
Conditional statements in Python are like a game of "if this, then that." The computer looks at something and based on what it sees, it does one thing or another. It's like when you play with your toys and you say, "if I press this button, then this toy will make noise." That's similar to how a computer uses conditional statements to make decisions and do different things based on what it sees.
"""
####################################
Language = "Java"
if Language == "Python":
    print("Language is Python")
elif Language == "Java":
    print("Language is Java")
elif Language == "JavaScript":
    print("Language is JS")    
else:
    print("No match")    

user = "Admin"
logged_in = False

if user =="Admin" or logged_in:
    print("Admin Page")
else:
    print("Bad Creds")

a=[1,2,3]
b=[1,2,3]
print(id(a))
print(id(b))
print(a == b)
print(a is b)

condition = 10

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")    