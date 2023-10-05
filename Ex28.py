'''Write a module named "calc.py" with below declaration and
do below operations.
 Declare two variables: x=100, y=200
 Declare two functions: addition(a,b),  multiply(a,b,c)
 Print the declared variables and call functions
 [Ex: addition(50, 60) & multiply(2, 3, 5)] in main namespace
 Declare documentation for calc module
 
 - Import calc module and call addition() function
 with x and y values from module
 - Import x variable and multiply() function from calc module and
 call multiply() function with x,2,3 as arguments
 - Print the documentation for calc module
'''
import calc
calc.addition(calc.x,calc.y)
calc.multiply(calc.x,2,3)
print(calc.__doc__)
