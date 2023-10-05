'''
 Write a program to get lines from the user and display below output.
   Input:
    Enter the lines:
     This is my first line
     This is my
     second line
    ^D
   Output:
    Lines: This is my first line\nThis is my\nsecond line\n
    Number of lines: 3
    Number of words: 10
    Number of chars: 45
    Joining Words:
     This-is-my-first-line
     This-is-my
     second-line
    '''
import sys
print('Enter the lines:')
lines=sys.stdin.readlines()
print('Lines:',lines)
print('Number of lines: ',len(lines))
#print(' '.join(lines))
#print(' '.join(lines).split())
print('Number of words: ',len(' '.join(lines).split()))
n=0
for i in lines:
    n+=len(i)
print('Number of chars: ',n)
print('Joining Words:\n',end='')
for k in lines:
    print(k.replace(' ','-'), end='')
