"""
Write a Python program to calculate the length of a string.
"""
def string_length(str):
    count = 0
    for char in str:
        count += 1
    return count
print(string_length("hello"))  
"""
Write a Python program to sum all the items in a list
"""
def sum_list(items):
  sum = 0
  for item in items:
    sum += item
  return sum
print(sum_list([1, 2, 3, 4]))
"""
Write a Python program to multiplies all the items in a list
"""
def multiply_items(items):
  product = 1
  for item in items:
    product *= item
  return product
print(multiply_items([1, 2, 3, 4]))  