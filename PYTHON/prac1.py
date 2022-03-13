# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 17:50:36 2022

@author: USER
"""

#x = 1 #global variable

#def foo(): #local var
   # x = 10
   # y = 20

#for i in range(1,2): #local var
    #x = 100
   # y = 200

#STRING

#str = "hello"

#print (str[0])
#print (str[2])
#print (str[2:5])
#print (str * 2)
#print (str + "world")

#FORMATIING
#print("{0:8.2f}".format(45.73456))

#number = 45;

#print(type(number))

#LIST

#list = ['abcd', 786, 2.23, 'john', 70.2]
#tinylist = [123, 'john']

#print (list)
#print (list[0])
#print (list[1:3])
#print (list[2:])

#TUPLE

#list1 = [0, 1, 2, 3]
#list1[0] = 10
#print(list1)

#list2 = (0, 1, 2, 3) #Tuple cant be changed
#list2[0] = 10
#print(list2)

#DICTIONARY

#list3 = {"one":"freshman", "two":2, "three":True}

#print (list3["two"])
#print(list3)
#print (list3.keys())
#print (list3.values())

#SETS
#list4 = {"freshman", 2, True}
#print(list4)

#CONVERTING
#number = "1"

#number2 = int(number)

#print(type(number2))

#if True:
    #print ("Answer")
#else:
    #print("False")
    
#def add(num1, num2):
    #return num1 + num2

#POSITIONAL
#print(add(1, 2))

#KEYWORD
#print(add(num2=2, num1=3))


#def add(num1, num2=5):
    #return num1 + num2
    
    
#print(add(2))

#CHEKING ERRORS
#try: #lets you test a block of code for errors (required)
   # x = int(input("Enter a number: "))
#except: #lets you handle the error (required, can be one or more)
    #print("Something went wrong....")
#else: #let's you execute code when there is no error (optional)
    #print(x)
#finally: #let's you execute code regardless
    #print("finally block..")
    
#EXCEPTION

#try: #lets you test a block of code for errors (required)
    #x = 6/0;
#except(ArithmeticError): 
    #print("Division by zero not allowed")
#except(Exception):
    #print("invalid input...")
#else: #let's you execute code when there is no error (optional)
    #print(x)
#finally: #let's you execute code regardless
    #print("finally block..")