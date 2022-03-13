# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:49:19 2022

@author: USER
"""
#METHOD OVERRIDING

class Person():
        
    def __init__(self, height):
        self.height = height
        
    def display(self):
        print('calling from Person class')
        
        
class Student (Person):
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
    
    def display(self):
        print('calling from Student class')
            


class Graduate(Student):
    pass
        
s1 = Student('juan', 16)
s1.display()
