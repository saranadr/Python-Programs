'''Write a program to find the given number is odd or even number ?
    Input:
     Enter the number: 15
    Output:
     The given number(15) is odd number.
'''

a=int(input('Enter the number: '))
if a%2==0:
    print('The given number(%d) is even number.'%a)
else:
    print('The given number(%d) is odd number.'%a)
