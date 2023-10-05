class Myclass():
    def __init__(self):
        print("This is constructor function.")

    def myfunc(self):
        print("This is myfunc function.")

    def __del__(self):
        print("This is destructor function.")

m1 = Myclass()
m1.myfunc()
del(m1)
print("Ended")
