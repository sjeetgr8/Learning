# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 19:17:14 2022

@author: Satya
"""

"""
3.1 What Is a Control Structure?

Control flow is the order that instructions are executed in a program. A control statement is a statement
that determines the control fl ow of a set of instructions. 
There are three fundamental forms of control that programming languages provide— sequential control , selection control , and iterative control.

Sequential control is an implicit form of control in which instructions are executed in the
order that they are written

A selection control statement is a control statement providing selective execution of instructions.
A selection control structure is a given set of instructions and the selection control statement(s)
controlling their execution

3.2 Boolean Expressions (Conditions)

"""
10==20
10!=20
10>=20
'2'<9
'12'<'9'
'12'>'9'
'Hello'=="Hello"
'hello'=='Hello'
'hello'<'ZEBRA'
'hello'>'ZEBRA'


## 3.2.2 Membership Operators
10 in (10,20,30)

color='red'
color in ('red','green','blue')

10 not in (10,20,30)

city ='Houston'
city in ('NY', 'Baltimore', 'LA')

## 3.2.3 Boolean Operators
num=15
1<=num<=15

## 3.2.4 Operator Precedence and Boolean Expressions
print ('This program will convert temperature F/C')
print('Enter(F) to convert Farahenheit to Celsius')
print('Enter (C) to convert Celsius to Farhenheit')

which=input('Enter selection:')
temp=(int(input('Enter temperature to convert:')))
if which == 'F':
    converted_temp=(temp-32)*5/9
    print (temp,'degrees fahrenheit equals',
           converted_temp,'degrees fahrenheit')
else:
    converted_temp=(9/5*temp)+32
    print(temp, 'degree celsius equals',
          converted_temp,'degree fahrenheit')
    

# Nested if statements
grade=int(input('Enter your marks to know your grade '))

if grade>=90:
    print('Grade of A')
else:
    if grade>=80:
        print('Grade of B')
    else:
        if grade>=70:
            print('Grade of C')
        else:
            if grade>=60:
                print('Grade of D')
            else:
                print('grade of E')
                
if grade>=90:
    print('Grade of A')
elif grade>=80:
    print('Grade of B')




        































