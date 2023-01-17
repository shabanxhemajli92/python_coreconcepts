"""
Recursive functions in Python are functions that call themselves. They are used to solve problems that can be broken down into smaller, simpler subproblems. The function defines a base case, which is the condition that stops the recursion, and a recursive case, which calls the function again with a modified set of inputs. Recursive functions are useful for solving problems that have a recursive structure, such as tree traversal, backtracking, and divide-and-conquer algorithms.

A recursive function is like a puzzle that you have to solve. Imagine you have a box with a bunch of smaller boxes inside, and inside each of those boxes, there are even smaller boxes. Now, imagine you want to find a toy that is hidden inside one of those boxes. One way to do it would be to open each box one by one until you find the toy. This is like a recursive function.

The big box is like the main function, and each smaller box is like a smaller version of the same problem. The main function calls itself with a different smaller box each time, and it keeps doing that until it finally finds the toy (which is like the base case).

Just like how you can open the boxes in any order you want, the function can call itself in different ways depending on how it is programmed. And just like how you can use different methods to find the toy, the function can use different logic to solve the problem.

In programming, we call this 'breaking down a problem into smaller parts'. And that's what recursive functions do.
"""
#find five factorial
"""
5!= Five factorial = 1*2*3*4*5=120
"""
def getFactorial(n):
    if n < 2:
        return 1
    else:
        return n * getFactorial(n-1)
print(getFactorial(6))            

def EvenNums(num):
    if num % 2 != 0:
        print("Put a better number")
    elif num == 2:
        return num
    else:
        return EvenNums(num - 2)
print(EvenNums(7))        

def Fibonacci(index_of_number):
    if index_of_number <= 1:
        return index_of_number
    else:
        return Fibonacci(index_of_number-1)+Fibonacci(index_of_number+2) 
print(Fibonacci(3)) 

def fibonacci(idx):
    seq=[0,1]
    for i in range(idx):
        seq.append(seq[-1]+seq[-2])
        return seq[-2]
print(fibonacci(8))        
