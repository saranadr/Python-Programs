class Myclass():
    a = 100 # class variable

    def add(self, x, y):
        print("Given args: ", x, y)
        print("Addition: ", x + y)

print(Myclass.a)
Myclass.a=300

m1 = Myclass()
print(m1.a)
m1.a=200
print(m1.a)
#m1.add(10, 20)

m2 = Myclass()
print(m2.a)
#m1.add(10, 20)
