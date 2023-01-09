squares=[]
for i in range(1,101):
    squares.append(i**2)
print(squares)

squares2=[i**2 for i in range(1,101)]
print(squares2)    

remainder5 = [x**2 % 5 for x in range(1,101)]
print(remainder5)

"""
a list comprehension is a special way to make a new list from an old list. It looks at each number in the old list and only keeps the ones that are even, and then puts them all in the new list.
"""