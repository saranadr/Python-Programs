# Func with default args
def add(x=50, y=60):
    print("Args: ", x, y)
    print("Addition: ", x + y)

add(10, 20)
add(10)
add()


# Func with keyword args
def myfunc(x, y):
    print("Given args: ", x, y)

myfunc(100, 200)
myfunc(y=100, x=200)

add(y=100)
