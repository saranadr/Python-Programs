a=100  # Global variable

def myfunc():
    global a
    a=150
    b=200 # Local variable
    print("The value of a is", a)
    print("The value of b is", b)

print("A BEFORE:", a)
myfunc()
#print("B vlue: ", b) # Local variable can't be accessed outside function.
print("A AFTER:", a)
