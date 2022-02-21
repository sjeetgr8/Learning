# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 11:07:16 2022

@author: Satya
"""

"""      

Syntax      
 DataFrame.astype(dtype, copy=True, errors='raise')[source]

    Cast a pandas object to a specified dtype dtype.

    Parameters

        dtypedata type, or dict of column name -> data type

            Use a numpy.dtype or Python type to cast entire pandas object to the same type. Alternatively, use {col: dtype, …}, where col is a column label and dtype is a numpy.dtype or Python type to cast one or more of the DataFrame’s columns to column-specific types.
        copybool, default True

            Return a copy when copy=True (be very careful setting copy=False as changes to values then may propagate to other pandas objects).
        errors{‘raise’, ‘ignore’}, default ‘raise’

            Control raising of exceptions on invalid data for provided dtype.

                raise : allow exceptions to be raised

                ignore : suppress exceptions. On error return original object.   """
                
# Sources 
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.astype.html
# https://medium.com/when-i-work-data/nullable-integers-4060089f92ec
                
# Important points to be noted
#  * When astype is not specified while merging two dataframes the default datatype is float

            
# Converting the datatype of a column at initialisation
# Converting the datype of a column after initialisation 
        # Case1:-
        # CAse2:- 


import pandas as pd
import numpy as np

customers = pd.DataFrame(
    data={
        'customer_id': ['1', '2', '3', '4'],
        'customerName': ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']
    }
)

orders = (
    pd.DataFrame(
        data={
            'order_id': ['100', '101', '102', '103', '104'],
            'customer_id': ['1', '1', '3', '4', '4'],
            'product': [ 'Firebolt',
                         'Pewter Cauldron',
                         'Dragon Hide Gloves',
                         'Polyjuice Potion',
                         'Weasley Is Our King Buttons',],
            'quantity': [1, 18, 10, 6, 120]
        }
    )
    .astype({'quantity': 'Int64'})
)

print(orders.to_string(), '\n')
print(orders.info(), '\n')

customer_orders = customers.merge(orders, on='customer_id', how='left')

print(customer_orders.to_string(), '\n')
print(customer_orders.info())



def load_df(): 
  return pd.DataFrame({
    'string_col': ['1','2','3','4'],
    'int_col': [1,2,3,4],
    'float_col': [1.1,1.2,1.3,4.7],
    'mix_col': ['a', 2, 3, 4],
    'missing_col': [1.0, 2, 3, np.nan],
    'money_col': ['£1,000.00', '£2,400.00', '£2,400.00', '£2,400.00'],
    'boolean_col': [True, False, True, True],
    'custom': ['Y', 'Y', 'N', 'N']
  })


df = load_df()
df
df['string_col']

df.dtypes 

df['string_col'] = df['string_col'].astype('int')
df.dtypes

df['string_col']


df['mix_col'] = pd.to_numeric(df['mix_col'], errors='coerce')
df
?pd.to_numeric
df['mix_col']
df.mix_col







