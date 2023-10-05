

class myclass():
    a=100
    def myfunction(self):
        print('this is my function')
        print('self:',self)

m1=myclass()
print('m1:',m1)
print(m1.a)
m1.myfunction()

m2=myclass()
print('m2:',m2)
print(m2.a)
m2.myfunction()

m1.a=200
print(m1.a,m2.a)
