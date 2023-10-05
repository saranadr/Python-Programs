'''Write a function to accept two lists as arguments. 
  It should compare each values of two list and
  return the values present in both list and in same index position.
  (no duplicates)
  Input:
   Enter the size: 8
   Enter the values for list1: 10 20 30 40 50 10 50 15
   Enter the values for list2: 10 30 20 40 60 10 50 25
  Output:
   Result: 
   *******
   [10, 40, 50]'''
list1=[]
list2=[]
common=[]
size=int(input('Enter the size: '))
list1=[int(i) for i in (input('Enter the values for list1:')).split()]
list2=[int(i) for i in (input('Enter the values for list2:')).split()]
##print('Enter the values for list1')
##for i in range(0,size):
##    value=int(input())
##    list1.append(value)
##print('Enter the values for list2')
##for i in range(0,size):
##    value=int(input())
##    list2.append(value)
print(list1)
print(list2)
##for i in range(0,size):
##    if list1[i]==list2[i]:
##        common.append(int(list1[i]))
##print('Result: ')
##print('*******')
##print(list(set(common)))
##
myset=set()
for i in range(0,size):
    if list1[i]==list2[i] and list1[i] not in common:
       # if list1[i] not in common
        common.append(list1[i])
        myset.add(list1[i])
print('Result: ')
print('*******')
print(myset)
print(common)
