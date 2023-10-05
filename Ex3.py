'''Declare a string and display below output.
    mystr = 'welcome to python program'
   Output:
    Given String   : welcome to python program
    Reversed string: margorp nohtyp ot emoclew
    First 7 chars  : welcome
    Last 7 chars   : program
    Skip first 8 chars : to python program
    Skip last 8 chars  : welcome to python 
    Given Language     : python
    Words in string    : ['welcome', 'to', 'python', 'program']
    Joined Words       : welcome-to-python-program
'''

'''
mystr='welcome to python program'
print('Given String\t:',mystr)
print('Reversed String\t:',mystr[::-1])
print('First 7 chars\t:',mystr[:7])
print('Last 7 chars\t:',mystr[-7:])
print('Skip first 8 chars\t:',mystr[8:])
print('Skip last 8 chars\t:',mystr[:-8])
print('Given Language\t\t:',mystr[11:17])
words=mystr.split(' ')
print('Words in string\t: ',words)
print('Joined Words\t: ','-'.join(words))
'''

mystr='welcome to python program'
print('''Given String   : {0}
Reversed string: {1}
First 7 chars  : {2}
Last 7 chars   : {3}
Skip first 8 chars : {4}
Skip last 8 chars  : {5}
Given Language     : {6}
Words in string    : {7}
Joined Words       : {8}'''.format(mystr,mystr[::-1],mystr[:7],mystr[-7:],
mystr[8:],mystr[:-8],mystr[11:17],mystr.split(' '),'-'.join(mystr.split(' '))                                   )
)
