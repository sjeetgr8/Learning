# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 13:46:31 2022

@author: Satya
"""
print('Hello world')

%run chapter_2.py

import numpy as np
data = {i : np.random.randn() for i in range(7)} #newly created Python dictionary
data

from numpy.random import randn
data = {i : randn() for i in range(7)}
print(data)
data


# data = {i : numpy.random.randn() for i in range(7)} #newly created Python dictionary

b = [1, 2, 3]
b?
b[0]
b[1]
b[2]
b[3]


""" 2.3 Python Language Basics
    Language Semantics
    * Indentation, not braces
    * A colon denotes the start of an indented code block after which all of the code must
      be indented by the same amount until the end of the block]
    * I strongly recommend using four spaces as your default indentation
     and replacing tabs with four spaces
     * 
"""
a = [1, 2, 3]
a.append(4)
a


def append_element(some_list, element):
    some_list.append(element)
data = [1, 2, 3]
append_element(data, 4)
data

a = 5
isinstance(a, int)

a = 5; b = 4.5
isinstance(a, (int, float))


## obj.attribute_name:


5<=2

a=None
a is None 

""" Mutable and immutable objects 

Most objects in Python, such as lists, dicts, NumPy arrays, and most user-defined
types (classes), are mutable. This means that the object or values that they contain can
be modified:
    
"""

a_list = ['foo', 2, [4, 5]]
a_list[2] = (3, 4)
a_list

a_tuple = (3, 5, (4, 5))
a_tuple[1] = 'four' ##'tuple' object does not support item assignment

a = 'this is a string'
a[10] = 'f'
a[5]
b = a.replace('string', 'longer string')
b

s = 'python'
list(s)
s[:3]

a = 'this is the first half '
b = 'and this is the second half'
a+b

## Bytes and Unicode

""" Type casting
The str, bool, int, and float types are also functions that can be used to cast values
to those types:
    
"""

from datetime import datetime, date, time
dt = datetime(2011, 10, 29, 20, 30, 21)
dt.day
dt.minute

if x < 0:
    print('It's negative')
elif x == 0:
    print('Equal to zero')
elif 0 < x < 5:
    print('Positive but smaller than 5')
else:
    print('Positive and larger than or equal to 5')

range(10)
list(range(0, 20, 2))





