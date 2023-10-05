
'''
Write a program to match the given pattern using regular expressions.
 str1 = "My phone number is 1234567890 and email address is username@intel.com"
  - Extract phone number and email id from above string
  Output:
   Name         : USERNAME
   Company      : INTEL
   Phone number : 1234567890
   Email address: username@intel.com

 str2 = 'welcome to python program'
  - Add $ symbol before and after each vowels in above string.
  Output: 
   w$e$lc$o$m$e$ t$o$ pyth$o$n pr$o$gr$a$m
'''
import re
print('To extract phone number and email id from string')
str1='My phone number is 1234567890 and email address is username@intel.com' #input('Enter string: ')

m1=re.search('number is (\d{10}) and email address is ((\w*)@(\w*).com)',str1)

print('Name         : ',m1.group(3).upper())
print('Company      : ',m1.group(4).upper())
print('Phone number : ',m1.group(1))
print('Email address: ',m1.group(2))

print('To add $ symbol before and after each vowels in string')
str2=input('Enter string: ')
m4=re.sub('([aeiou])','$\1$',str2)
print(m4)
