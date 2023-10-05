'''Write a program to design a calculator.
It should ask for inputs from user until user exit the program.
    - 2 types (using nested-if and functions)
    Input:
     ***** Welcome to Calculator ******
     Please enter the numbers and select operation:
     1. Addition
     2. Subtraction
     3. Multiplication
     4. Division
     Choose the option [1-4] : 1
     Enter the number1 : 10
     Enter the number2 : 20

    Output:
     The addition of given two numbers (10, 20) are: 30
'''

while True:
    print('''***** Welcome to Calculator ******
    Please enter the numbers and select operation:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division''')
    op=int(input('Choose the option [1-4] : '))
    if op not in range(1,5):
        print('Option not valid')
        break
    a=int(input('Enter the number1 : '))
    b=int(input('Enter the number2 : '))
'''
    if op==1:
        print('The addition of given two numbers (%d, %d) are: %d'%(a,b,a+b))
    elif op==2:
        print('The subtraction of given two numbers (%d, %d) are: %d'%(a,b,a-b))
    elif op==3:
        print('The multiplication of given two numbers (%d, %d) are: %d'%(a,b,a*b))
    else:
        print('The division of given two numbers (%d, %d) are: %.2f'%(a,b,a/b)) 
'''
#using function
def add(a,b):
    print('The addition of given two numbers (%d, %d) are: %d'%(a,b,a+b))
def add(a,b):
    print('The addition of given two numbers (%d, %d) are: %d'%(a,b,a+b))
def add(a,b):
    print('The addition of given two numbers (%d, %d) are: %d'%(a,b,a+b))
def add(a,b):
    print('The addition of given two numbers (%d, %d) are: %d'%(a,b,a+b))
