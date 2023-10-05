'''Write a program to find the factorial of given number.
(Recursive function)
    Input:
     Enter the number: 5
    Output:
     The factorial of given number 5 is 120
'''
'''
def factorial(x):
    result=1
    for i in range (1,x+1): result*=i
    print('The factorial of given number {0} is {1}'.format(x,result))

number=int(input('Enter the number: '))
factorial(number)
'''
def factorial1(x):
    if x<=1:
        return 1
    else:
        return x * factorial1(x-1)

number=int(input('Enter the number: '))
print('The factorial of given number {0} is {1}'.format(number,factorial1(number)))
