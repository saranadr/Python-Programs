'''Write a program to display multiples of given number between 1 to 100.
    (2 types: using for and while loop)
    - Also print the reverse of numbers between given range
    Input:
     Enter the number: 5
    Output:
     Result: 5, 10, 15, ... 100
     Reverse: 100, 95, 90, ... 5
'''
'''
a=int(input('Enter the number: '))
b=[]
i=1
while i<=100:
    if i%a==0:
        b.append(i)
        i+=a
    else:
        i+=1
print('Result:', end=' ')
for k in range(len(b)):
    print(b[k],end=', ')
else: print( )
print('Reverse:', end=' ')
for l in range(1,len(b)+1):
    print(b[-l],end=', ')

'''
'''
a=int(input('Enter the number: '))
print('Result:', end=' ')
for k in range(1,101):
    if k%a==0:
        print(k,end=', ')
        k+=a
    else:
        k+=1
else: print( )
print('Reverse:', end=' ')
for k in reversed(range(1,101)):
    if k%a==0:
        print(k,end=', ')
        k-=a
    else:
        k-=1
'''
a=int(input('Enter the number: '))
print('Result:', end=' ')
for i in range(a,101,a):
    print(i, end=', ')
#else: print( )    
print('\nReverse:', end=' ')
for i in reversed(range(a,101,a)):
    print(i, end=', ')
    
i=1
print('\nResult:', end=' ')
while i<=100:
    if i%a==0:
        print(i, end=', ')
        i+=a
    else:
        i+=1
print('\nReverse:', end=' ')
i=100
while i>=1 :
    if i%a==0:
        print(i, end=', ')
        i-=a
    else:
        i-=1
