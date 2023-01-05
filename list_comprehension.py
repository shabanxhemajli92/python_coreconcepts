squares=[]
for i in range(1,101):
    squares.append(i**2)
print(squares)

squares2=[i**2 for i in range(1,101)]
print(squares2)    

remainder5 = [x**2 % 5 for x in range(1,101)]
print(remainder5)