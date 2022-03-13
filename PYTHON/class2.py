# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 21:22:27 2022

@author: USER
"""
#INHERITANCE
class Student:
    'class student is designed to...'
    school = 'UST'
    count = 0
    
    #METHODS
    def __init__(self, name, age):
        self.__name = name
        self.__age = age


    
    #GETTER - to access protected/private
    
    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_age(self, age):
        self.__age = age
        
    def addStud(cls): 
       print("hello")
        
    def greet(message):
        print(message)
        
    def __add__(self, other):
        other = Student(other)
        return(self.__age + other.__age)
        
class Person():
        
    def __init__(self, height):
        self.height = height
        
    def display(self):
        print('calling from Person class')
        
        
        
class Graduate(Student, Person):
    pass

#g1 = Graduate('catho', 25)
#print(g1.get_name())
#print(g1.get_age())
#print(Graduate.school)
#g1.display()
    
s1 = Student('juan', 16)
s2 = Student('Pedro', 17)
print(s1.get_age() + s2.get_age())



#str1 = 'hello'
#str2 = ' world'
#print(str1.__add__(str2))
