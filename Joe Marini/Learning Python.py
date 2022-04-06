# -*- coding: utf-8 -*-
"""
Created on Sat Feb 26 14:36:56 2022

@author: Satya
"""

# basic data types in Python: Numbers, strings, booleans, sequences and dictionaries

myint=5
myfloat=14.5
mystr="Heelo, Welcome to my world"
mybool= False
mylist=[0,1,4,'Hello',True, 13.77]
mytuple=(0,1,2)
mydict={"one":1,
        "two":2 
        }

print(myint)
print(myfloat)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

#declaring a variable works
myint="Hello"
print(myint)

#to access a member of a sequence type, use[]

mylist[3]
  ## mylist(3)
  
# you can use slices to reverse a sequence 
print(mylist[1:2])
print(mylist[0:6])
print(mylist[1:4:2])



