print("Program started")


# Func with args and no return value
def add(x, y):
    print("Given args: ", x, y)
    print("Addition: ", x + y)


#Func with args and return value
def mul(a, b):
    return a * b
    
add(10, 20)
print("Multiplication: ", mul(10, 20))

x=5
y=10
z = mul(x,y)
print("The multiply of {0} and {1} is {2}".format(x,y,z))

#print(len('python'))

print("Program completed")
