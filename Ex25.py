'''Write a program to count the number of characters(occurences)
in a string.
    Input:
     Enter the string:  welcome to python program
    Output:
        ->  3
     a  ->  1
     c  ->  1
     e  ->  2
     g  ->  1
     h  ->  1
     m  ->  2
     l  ->  1
     o  ->  4
     n  ->  1
     p  ->  2
     r  ->  2
     t  ->  2
     w  ->  1
     y  ->  1
'''
mystr=input('Enter the string: ')
mydict={}
for i in mystr.lower():
    if i in mydict.keys():
        mydict[i]+=1
    else:
        mydict[i]=1
print('Output:')
for i,k in sorted(mydict.items()):
    print(i,'->',k)
