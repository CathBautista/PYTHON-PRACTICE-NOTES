# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:48:18 2022

@author: USER
"""

class Employee:
    'Common base class for all employees'
    empCount=0
    
    def __init__(self, name, salary): #var belongs to the object
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print ("Total Employee %d" % Employee.empCount)
        
    def displayEmployee(self):
        print ("Name:  ", self.name, ", Salary: ", self.salary)
        
"This would create first object of Employee class"
emp1= Employee("Zara", 2000)

"This would create second object of Employee class"
emp2= Employee("Manni", 5000)

emp3= Employee("Cath",8000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print ("Total Employee %d" % Employee.empCount)