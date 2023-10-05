# Func with variable length args

def myfunc(x, y):
    print("Given args: ", x, y)

myfunc(10, 20)

a,b=50,60
myfunc(a, b)

mylist=[100, 200]
myfunc(mylist, 111)
myfunc(mylist[0], mylist[1])
myfunc(*mylist)

mydict = {'y': 600, 'x': 500}
myfunc(mydict, 222)
myfunc(**mydict)


print(" **** " * 10)
def myfunc1(*args):
    print("Args: ", args)

myfunc1(10, 20, 30, 40)

def myfunc2(**args):
    print("Args: ", args)

myfunc2(a=100, b=200, c=300)
