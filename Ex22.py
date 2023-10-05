''' Write a program to find the longest line in the given string ?
    Input:
     Enter the lines:
      welcome to python
      this is the longest line
      this is my first line
      this is second line
      short line here
      this is the end line
    Output:
     Given lines: [above lines here]
     Longest line: this is the longest line [Length: 24]
'''
import sys
print('Enter the lines:')
lines=sys.stdin.readlines()
print('Given lines:',''.join(lines),end='')
k=0
for i in lines:
    if len(i)>=k:
        k=len(i)
        longline=i.replace('\n',' ')
print('Longest line: %s [Length: %d]'%(longline,k))

