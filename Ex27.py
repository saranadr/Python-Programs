'''Write a program with try-except to get
two numbers as input from the user and do division operation.
 - Use try block to get input from the user and
 do the division of numbers.
 - Declare except handler for ZeroDivisionError and
 generate NameError with "ZERO DIVISON ERROR" message inside it.
 - Declare default exception handler and
 print the error message "ERROR CAUGHT !!!" and exit the program.
 - The program should always print "Program completed..." message
 at last irrespective of any errors.
 
 Scenario 1:
  Input:  
   Enter the number1: 100
   Enter the number2: 5
  Output:
   The division of 100 and 5 is 20
   Program completed...
   
 Scenario 2:
  Input:
   Enter the number1: 100
   Enter the number2: 0
  Output:
   Program completed...
   Traceback (most recent call last):
   File "C:/Users/Test/Desktop/exception.py", line 8, in <module>
    raise NameError("ZERO DIVISION ERROR")
    NameError: ZERO DIVISION ERROR
	
 Scenario 3:
  Input:
   Enter the number1: welcome
  Output:
   ERROR CAUGHT !!! (<class 'ValueError'>, ValueError("invalid literal
   for int() with base 10: 'asdfg'",), <traceback object at 0x05336DA0>)
   program completed...
'''
import sys
try:
    a=int(input('Enter the number1: '))
    b=int(input('Enter the number2: '))
    print('The division of {0} and {1} is {2}'.format(a,b,a/b))
except ZeroDivisionError as msg1:
    #print('Zero Division Error is found ->',msg1)
    raise NameError('Zero Division Error is found')
except:
    print('Error is found')
    sys.exit(0)
finally:
    print('Program Completed...')
    
