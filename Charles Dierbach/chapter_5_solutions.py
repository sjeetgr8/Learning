# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
P1. Write a Python function named zeroCheck that is given three integers, 
and returns true if any of the integers is 0, otherwise it returns false.

"""

def zeroCheck(a,b,c):
    if (a==0 or b==0 or c==0):      
        return True
    else: 
        return False
    
print("Enter the values of a, b, and c")
a= int(input("Enyter the value of a "))
b= int(input("Enyter the value of b "))
c= int(input("Enyter the value of c "))
zeroCheck(a,b,c)

zeroCheck(4,6,0)


"""
P2. Write a Python function named ordered3 that is passed three integers, and 
returns true if the three integers
are in order from smallest to largest, otherwise it returns false.

"""
def ordered3(a,b,c):
    if(a>b and a>c and b>c):
        return True
    else:
        return False

print("Enter the values of a, b, and c")
a= int(input("Enyter the value of a "))
b= int(input("Enyter the value of b "))
c= int(input("Enyter the value of c "))
ordered3(a,b,c)




