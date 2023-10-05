'''

Write a class named "Employee" and "Company" with below details.
 Company:
  Declare constructor and store "company_name" and "company_location" details.
  (static)
  Declare a function named "showCompany()" which will display the company details.
  
 Employee: (Inherit 'Company' class)
  Declare constructor and store "empid", "empname" and "department" details.
  (Dynamic)
  Declare a function named "showEmployee()" which will display employee details.
  
 Create an object for 'Company' class and display company details.
 Create an object for first Employee and display employee and company details.
 (1001, Manoj, IT)
 Create an object for second Employee and display employee and company details.
 (1002, Suresh, Sales)
 Change the department & company_location for second employee and
 display the details again.
 

'''
class Company():
    field='Agri'
    def __init__(self):
        self.cname='google'
        self.location='chennai'

    def showCompany(self):
        print('Company Details')
        print('company name    : ',self.cname)
        print('company location: ',self.location)
        print('Company field: ',self.field)

#c1=Company()
#c1.showCompany()

class Employee(Company):
    def __init__(self, eid, ename, edept):
        self.empid=eid
        self.empname=ename
        self.dept=edept
        Company.__init__(self)

    def showEmployee(self):
        print('Employee details')
        print('Employee id  : ',self.empid)
        print('Employee name: ',self.empname)
        print('Employee Dept: ',self.dept)
        self.showCompany()
        

e1=Employee(1001,'Manoj', 'IT')
e1.showEmployee()
#e1.showCompany()

Company.field='Pharma'
e2=Employee(1002, 'Suresh', 'Sales')
e2.showEmployee()
e2.dept='Finance'
e2.location='hyderabad'

print('*'*25)
e2.showEmployee()
e1.showEmployee()
