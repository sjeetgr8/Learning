# -*- coding: utf-8 -*-
"""
Created on Wed Apr  6 20:24:01 2022

@author: Satya
"""

Write a short Python function that takes a positive integer n and
returns the sum of the squares of all the positive integers smaller than
n.

def func(n):
    sum=0
    for i in range (0,n):
        sum=sum+ i*i
    return sum 

func(5)
