'''Write a program to check whether the given string is a palindrome ?
    Input:
     Enter the string: racecar
    Output:
     The given string 'racecar' is a palindrome.
'''
a=input('Enter the string: ')
if a!=a[::-1]:
    print("The given string '%s' is not a palindrome."%a)
else:
    print("The given string '%s' is a palindrome."%a)


    
for i in range(len(mystr)):
    if mystr[i]!=mystr[len(mystr)-(i+1)]:
        palindrome=False
