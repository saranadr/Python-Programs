'''
 Write a program to do below operations on list.
   mylist = [10, 20, 30]
   Output:
    Given List             : [10, 20, 30]
    Elements in the list   :  3
    Add value at last      : [10, 20, 30, 40]
    Added 2 values at last : [10, 20, 30, 40, 50, 60]
    Add value at 2nd index :  [10, 20, 100, 30, 40, 50, 60]
    Remove 2 values at last: [10, 20, 100, 30, 40]
    Remove 2nd element     : [10, 20, 30, 40]
    Remove first 2 elements: [30, 40]
    Empty the list         : []
    Remove the list variable from memory:  <ERROR-MESSAGE>
'''

mylist=[10, 20, 30]
print('Given List             :',mylist)
print('Elements in the list   :',len(mylist))
mylist.append(40)
print('Add value at last      :',mylist)
mylist.extend([50,60])
print('Added 2 values at last :',mylist)
mylist.insert(2,100)
print('Add value at 2nd index :',mylist)
mylist=mylist[0:-2]
print('Remove 2 values at last:',mylist)
mylist.pop(2)
print('Remove 2nd element     :',mylist)
mylist=mylist[2:]
print('Remove first 2 elements:',mylist)
mylist.clear()
print('Empty the list         :',mylist)
del(mylist)
print('Remove the list variable from memory:',mylist)
