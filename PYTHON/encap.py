# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 20:23:46 2022

@author: USER
"""

#class Student:
    #'class student is designed to...'
    #def __init__(self, name, age): #local vars
        #self.name = name
        #self.age = age
        
    #def displayStudent(self):
        #print("Student Name: ", self.name, "Age:", self.age)

#s1 = Student("Catherine Bautista", 21)

#print(s1.name)
#s1.level = 'freshman'
#s1.displayStudent()
#print(type(s1))
#print(hasattr(s1, 'name'))


#setattr(s1, 'level', 'sophomore')
#s2 = Student("Pedro", 20)
#print(hasattr(s2, 'level'))

#delattr(s1, 'age')
#print(s1.__dict__)
#print(s1.__doc__) 
#print(Student.__name__)

#NOTES

#ENCAPSULATION
#self.name = name // #public - accesible anywhere in class
#self._project= project // #private - accesible wthin class
#self.__salary = salary // #protected - accessible within class and subclass

class Student:
    'class student is designed to...'
    school = 'UST'
    count = 0
    
    #METHODS
    def __init__(self, name, age): #local vars #INSTANCE METHOD - modify an object
        self.__name = name
        self.__age = age
       # Student.count = Student.count + 1

    
    #GETTER - to access protected/private
    
    def get_age(self):
        return self.__age
    
    def set_age(self, age):
        self.__age = age
        
    def addStud(cls): #CLASS METHOD- can access class reference to the class. Modify class
       print("hello")
        
    def greet(message):#STATIC METHOD -can't modify class or object
        print(message)
        
        

s1=Student('cath', 20)
Student.greet("Hello World")
s1.addStud()

s2=Student('mylene', 20)
s2.addStud()

s3=Student('annie', 20)
s3.addStud()

s4=Student('nikka', 20)
s4.addStud()

#print(s1.school)
#print(s2.school)
#print(s3.school)
#print(s4.school)
#print(Student.count)
#Student.addStud()
#s1.set_age(25)
#print(s1.get_age())

#s1.__age = 22 #line 46 different object w same name
#print(s1.__age)