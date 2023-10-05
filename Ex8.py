'''Write a program to get a line as input from user and do below operations.
   - Check whether the string begins with 'welcome' and ends with 'python' (case-insensitive check)
   - Find the matched position of search string and return matched position if exists.
   - Replace the line with given replace string
   Input:
    Enter the line:  <WELcome to python program>
    Enter the search string:  <python>
    Enter the replace string: <PHP>

   Output:
    The given line: WELcome to python program
    Starts with 'welcome': True
    Ends with 'python'   : False
    Search string : python
    Matched position: True [Position: 11]
    Replace string: PHP
    Replaced line : WELcome to PHP program
'''

line=input('enter the line: ')
search=input('Enter the search string: ')
repl=input('Enter the replace string: ')
print('The given line:',line)
print("Starts with 'welcome':",line.lower().startswith('welcome'))
print("Ends with 'python':",line.endswith('python'))
print('Search string :',search)
position=line.find('python')

print('Matched position: True [Position: {0}]'.format(position))
print('Replace string:',repl)
print('Replaced line:',line.replace(search,repl))
