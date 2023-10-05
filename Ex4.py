''' Write a progm to get Emp Id, Employee Name and Salary from user  and display the given details.
   Input:
    Enter the Employee Id  : <12345>
    Enter the Employee Name: <Ramesh>
    Enter the Department   : <INFORMATION technology>   
   Output:
    ***** Employee Details *****
    Emp ID  : 12345
    Emp Name: RAMESH
    Reversed Name: hsemaR
    Emp Dept: information TECHNOLOGY        
    Length of Dept: 22
    ****************************
'''

empid=int(input('Enter the Employee Id\t: '))
empname=(input('Enter the Employee Name\t: '))
dept=(input('Enter the Department\t: '))
print('***** Employee Details *****')
print('Emp ID\t\t: ',empid)
print('Emp Name\t: ',empname.upper())
print('Reversed Name\t: ',empname[::-1])
print('Emp Dept\t: ',dept.swapcase())
print('Length of Dept\t: ',len(dept))
print('****************************')

