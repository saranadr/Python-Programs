class Student():
    def __init__(self, regno, name):
        self.regno = regno
        self.name = name
        self.college = 'ABC College'
        location = 'Chennai'

    def printInfo(self):
        print("Student Details".center(30, "*"))
        print("Regno: ", self.regno)
        print("Name: ", self.name)
        print("College: ", self.college)

s1 = Student(1001, 'Manoj')
s1.printInfo()

s2 = Student(1002, 'Saranya')
s2.printInfo()

