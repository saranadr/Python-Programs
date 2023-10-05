'''Write a program to print number histogram and
get the sum of all digits in a number ?
    Input:
     Enter the number for histogram: 5826
    Output:
     The given number: 5826
     Result,
     *****
     ********
     **
     ******
    The sum of digits in number: 21
'''
hnum=input('Enter the number for histogram: ')
print('The given number:',hnum)
print('Result,')
hsum=0
for i in hnum:
    print('*'*int(i))
    hsum+=int(i)
print('The sum of digits in number:',hsum)
