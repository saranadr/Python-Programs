'''Write a program to display multiplication table of given number
    with specified range using loops.
    Input:
     Enter the number for table: 5
     Enter the number for table limit: 4

    Output:
     Multiplication Table of 5
     *************************
     1 * 5 = 5
     2 * 5 = 10
     3 * 5 = 15
     4 * 5 = 20
'''
table=int(input('Enter the number for table: '))
limit=int(input('Enter the number for table limit: '))
print('Multiplication Table of %d'%table)
print('*************************')
for i in range(1,limit+1):
    print('%d * %d = %d'%(i,table,i*table))


