'''Write a program to calculate the sum of given numbers?
    Input:
     Enter the limit/count for numbers: 3
     Enter the number 1: 10
     Enter the number 2: 20
     Enter the number 3: 30
    Output:
     The sum of given numbers [10 20 30] is: 60
     '''

limit=int(input('Enter the limit/count for numbers: '))
numbers=[]
for i in range(1,limit+1):
    #k=int(input('Enter the number '+str(i+1)+': '))
    k=int(input('Enter the number {0}: '.format(i)))
    numbers.append(k)
print('The sum of given numbers {0} is: {1}'.format(numbers,sum(numbers)))

