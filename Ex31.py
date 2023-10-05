'''Write a program to get a sentence as input from the user and display the number of digits, alphabets and special characters.
 Input:
  Enter the sentence: Welcome to PYTHON. My number is 1234567890. END!!!
 Output:
  Given sentence: Welcome to PYTHON. My number is 1234567890. END!!!
  Character  Count
  ---------  -----
   DIGITS     10
   UPPER      11
   LOWER      17
   SPECIAL    12
'''
sentence=input('Enter the sentence: ')
print('Given sentence:',sentence)
digits=0
upper=0
lower=0
special=0
for i in sentence:
    if i.isdigit():
        digits+=1
    elif i.isupper():
        upper+=1
    elif i.islower():
        lower+=1
    else:
        special+=1
print('Character  Count')
print('---------  -----')
print('DIGITS     ',digits)
print('UPPER      ',upper)
print('LOWER      ',lower)
print('SPECIAL    ',special)
