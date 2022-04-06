# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 19:46:19 2022

@author: Satya


Write a short Python function, is_multiple(n, m), that takes two
integer values and returns True if n is a multiple of m, that is, n = mi
for some integer i, and False otherwise.

"""

def is_multiple(n,m):
    if m%n==0:
        return True 
    else:
        return False

is_multiple(5,10)
