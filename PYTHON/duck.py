# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 22:46:35 2022

@author: USER
"""

#DUCK TYPING - attributes haveing same name

class Bird:
    def fly(self):
        print("fly with wings")
        
class Airplane:
    def fly(self):
        print("fly with fuel")
        
class Fish: #code won't work if repeated here
    def swim(self):
        print("fish swim in sea")
        