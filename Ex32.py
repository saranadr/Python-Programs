'''Write a program to print the ASCII value of characters in given string.
 Input:
  Enter the string: Welcome Python!
 Output:
  Given string: 
  ASCII Characters:
   W -> 87
   e -> 101
   l -> 108
   c -> 99
   o -> 111
   m -> 109
   e -> 101
     -> 32
   P -> 80
   y -> 121
   t -> 116
   h -> 104
   o -> 111
   n -> 110
   ! -> 33
'''
mystr=input('Enter the string: ')
print('Given string:',mystr)
print('ASCII Characters:')
for i in mystr:
    print('{0} -> {1}'.format(i,ord(i)))
