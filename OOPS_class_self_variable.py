class Myclass():
    a = 100 # class variable

    def myfunc():
        print("This is myfunc function")

    def add(self, x, y):
        print("Given args: ", x, y)
        print("Addition: ", x + y)
        #Myclass.myfunc()

    def mul(self, a, b):
        self.result = a*b # Object/Instance variasble

        
print(Myclass.a)

m1 = Myclass()
print(m1.a)
m1.add(10, 20)

m1.mul(10, 20)
print(m1.result)
#print(Myclass.result) #Object variable can't be accessed from class name.

#m1.myfunc() # Not working. Error
#Myclass.myfunc() # will work
