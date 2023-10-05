'''Write program to print command line arguments along with filename.
    - The script should contain 2 command line args.
    - The two args should be valid numbers. (use exceptions)
    - Do the addition of two numbers and display the output.

   cmd> python  myscript.py  100 200
   Output:
    Filename: myscript.py
    Number of args: 3
    The addition value of 100 and 200 is 300
'''

import os
import sys
if len(sys.argv)!=3:
    print('Usage: {0} num1 num2'.format(sys.argv[0]))
    sys.exit(0)
    
print("Filename:",(sys.argv[0])) #os.path.basename(__file__)
print("Number of args:", len(sys.argv))
#print("Command line args:",sys.argv)

def add(x, y):
    print("The addition value of %d and %d is %d"%(x,y,x+y))
try:
    add(int(sys.argv[1]), int(sys.argv[2]))
except:
    print('Error in adding values')
    print('Usage: {0} num1 num2'.format(sys.argv[0]))
