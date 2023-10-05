'''Write a program to print numbers with decimal points (multiple level loop)
    Input:
     Enter the number: 2
     Enter the precision: 5
    Output:
     1.1 1.2 1.3 1.4 1.5 2.1 2.2 2.3 2.4 2.5
'''

n=int(input('Enter the number: '))
p=int(input('Enter the precision: '))
for i in range(1,n+1):
    for k in range(1,p+1):
        print(str(i)+'.'+str(k),end=' ')
        

        
