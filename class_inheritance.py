class Parent():
    def myparent(self):
        print("This is myparent function.")

class Child(Parent):
    def mychild(self):
        print("This is mychild function.")

p1=Parent()
p1.myparent()

c1=Child()
c1.mychild()
c1.myparent()
