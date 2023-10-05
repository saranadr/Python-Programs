'''Write a program to get document from the user and do the find and replace operation.
    Input:
     Enter the content:
      welcome to python
      This is first line
      This is
      my second line
     Enter the search string :  is
     Enter the replace string:  IISS
     
   Output:
    Given Content: <the-given-input-message>
    Search string: is
    Replace string: IISS
    Result:
     ThIISS IISS first line
     ThIISS IISS
'''

import sys
print('Enter the content:')
content=sys.stdin.readlines()
search=input('Enter the search string : ')
repl=input('Enter the replace string : ')
print('Given Content:\n',' '.join(content))
print('Search string:',search)
print('Replace string:',repl)
#result=[]
print('Result:')
for i in content:
    if search in i:
        print(i.replace(search,repl), end='')
#print('Result:\n',' '.join(result))
