class Grandparent():
    def mygrandparent(self):
        print("This is mygrandparent function")

class Parent():
    def myparent(self):
        print("This is myparent function.")

class Child(Parent, Grandparent):
    def mychild(self):
        print("This is mychild function.")

print(" Grandparent ".center(25, "*"))
g1 = Grandparent()
g1.mygrandparent()

print(" Parent ".center(25, "*"))
p1=Parent()
#p1.mygrandparent()
p1.myparent()


print(" Child ".center(25, "*"))
c1=Child()
c1.mygrandparent()
c1.myparent()
c1.mychild()
