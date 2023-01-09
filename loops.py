"""
Loops are a way to repeat a set of instructions over and over again. Imagine you have a list of your favorite snacks and you want to eat each one. You can use a loop to help you do this. First, you tell the loop what snack you want to start with. Then, you tell it what to do with each snack, like saying "Yum, I love _____!" Then you tell the loop to move on to the next snack in the list and do the same thing. The loop will keep doing this until it has tried all of the snacks on your list.

Loops are a way to repeat instructions. You tell the loop what to do and it does it over and over again until it's finished.
"""

"""
There are two types of loops in Python: for loops and while loops.

for loops are used to repeat a block of code a certain number of times. For example, you might use a for loop to print out all of the elements in a list.

while loops are used to repeat a block of code as long as a certain condition is true. For example, you might use a while loop to keep asking a user for input until they enter a valid response.

Both for loops and while loops are useful when you need to perform an action multiple times and you want to automate the process. They can save you time and make your code more efficient.
"""
#for loops
my_list = ["E","A","D","G","B"] 
for letter in my_list:
    print(letter)

names=["kelly","michelle","Beyonce"]
for n in names:
    print(n + ",can you handle this?")
print("I dont think they can handle this!")

for i in range (3):
    print("Hello,hello,hello , how low")
print("Hello, hello,Hello")