'''Write a program to get two lines as input from the user and display the concatenated output.
   - Remove first 3 chars in str-1 and remove last 4 chars in str-2
   Input:
    Enter the string1 : Welcome to Python
    Enter the string2 : This is my first program
   Output:
    come to Python. This is my first pro
'''
'''
String1=input('Enter the String1 : ')
String2=input('Enter the String2 : ')
print(String1[3:]+'. '+String2[:-4])
'''

import sys
print('Enter the String1 : ')
String1=sys.stdin.readline()
print('Enter the String2 : ')
String2=sys.stdin.readline()
print(String1[3:-1]+'. '+String2[:-4])
