# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 23:21:11 2022

@author: USER
"""

#ABSTRACT
#from package need to import particular items 

from abc import ABC, abstractmethod

class Animal:
    @abstractmethod
    def walf(self):
        print ('Animal can walk')
        
class Dog(Animal):
    def walk(self):
        print ('Dogs walk differenly...')

class Cat(Animal):
    def walk(self):
        print ('Cats walk gracefully...')


d = Dog()
d.walk()

c = Cat()
c.walk()