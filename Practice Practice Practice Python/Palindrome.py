# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 22:44:22 2022

@author: Satya
"""
example=input("Enter any word and check its type")
type(example)
example 

the_string= str(input("Enter a word which you want to reverse: "))
the_string 
type(the_string)


x=len(the_string)


while x > 0:
    print(the_string[x-1], end ="")
    x-=1
    
    
the_string[4]

i = 1
while i < 6:
  print(i)
  i += 1