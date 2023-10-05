'''Documentation:
Write a module named "calc.py" with below declaration and
do below operations.
 Declare two variables: x=100, y=200
 Declare two functions: addition(a,b),  multiply(a,b,c)
 Print the declared variables and call functions
 [Ex: addition(50, 60) & multiply(2, 3, 5)] in main namespace
 Declare documentation for calc module
'''
x=100
y=200
#z=300

def addition(a,b):
    print('Addition function called')
    print('The addition of {0} and {1} is {2}'.format(a,b,a+b))

def multiply(a,b,c):
    print('Multiplication function called')
    print('The Multiplication of {0}, {1} and {2} is {3}'.format(a,b,c,a*b*c))

#addition(x,y)
#multiply(x,y,z)

if __name__=='__main__':
    addition(50,60)
    multiply(2,3,5)
