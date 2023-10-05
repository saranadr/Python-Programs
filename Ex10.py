'''
Write a program to get a number from the user and check whether
the number is between 100 and 150
     [OR] between 200 and 250.
    Input:
     Enter the number: 125
    Output:
     The given number [125] is between 100 and 150.
'''
a=int(input('Enter the number: '))
if (a>=100 and a<=150):
 print('The given number [%d] is between 100 and 150.'%a)
elif (a>=200 and a<=250):
 print('The given number [%d] is between 200 and 250.'%a)
else:
 print('The given number [%d] is neither between 100 and 150 nor between 200 and 250.'%a)
