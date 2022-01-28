# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 14:50:52 2022

@author: Satya
"""

"""
3.1 Data Structures and Sequences
Tuple
A tuple is a fixed-length, immutable sequence of Python objects. The easiest way to
create one is with a comma-separated sequence of values

While the objects stored in a tuple may be mutable themselves, once the tuple is created
it’s not possible to modify which object is stored in each slot

"""

tup = 4, 5, 6
tup

b=tuple([4, 0, 2]) ##You can convert any sequence or iterator to a tuple by invoking tuple
type(b)

tup = tuple(['foo', [1, 2], True])
tup[1].append(3)
tup 

a = (1, 2, 2, 2, 3, 4, 2)
a.count(2)


"""
List
In contrast with tuples, lists are variable-length and their contents can be modified
in-place. You can define them using square brackets [] or using the list type function:
    
"""
a_list = [2, 3, 7, None]
tup = ('foo', 'bar', 'baz')
b_list = list(tup)
b_list
b_list[1] = 'peekaboo'
b_list 
b_list.append('dwarf')
b_list.insert(1, 'red')

b_list.pop(2)

x = [4, None, 'foo']
x.extend([7, 8, (2, 3)])
x


a = [7, 2, 5, 1, 3]
a.sort()
a

import bisect

c = [1, 2, 2, 2, 3, 4, 7]
bisect.bisect(c, 2)


## bisect.bisect finds the location where an element should be inserted to keep it sorted,
##  while bisect.insort actually inserts the element into that location

seq = [7, 2, 3, 7, 5, 6, 0, 1]
seq[1:5]
"""
Slicing
You can select sections of most sequence types by using slice notation, which in its
basic form consists of start:stop passed to the indexing operator []:
"""

seq[:5]
seq[3:]
seq[-4:]
seq[-6:-2]


sorted([7, 1, 2, 6, 0, 3, 2])

seq1 = ['foo', 'bar', 'baz']
seq2 = ['one', 'two', 'three']
zipped = zip(seq1, seq2)    ## zip “pairs” up the elements of a number of lists, tuples, or other sequences to create a list of tuples
list(zipped)

"""
dict
dict is likely the most important built-in Python data structure. A more common
name for it is hash map or associative array. It is a flexibly sized collection of key-value
pairs, where key and value are Python objects. One approach for creating one is to use
curly braces {} and colons to separate keys and values

"""



"""

set
A set is an unordered collection of unique elements. You can think of them like dicts,
but keys only, no values. A set can be created in two ways: via the set function or via
a set literal with curly braces

"""

"""
a.add(x) N/A Add element x to the set a
a.clear() N/A Reset the set a to an empty state, discarding all of
its elements
a.remove(x) N/A Remove element x from the set a
a.pop() N/A Remove an arbitrary element from the set a, raising
KeyError if the set is empty
a.union(b) a | b All of the unique elements in a and b
a.update(b) a |= b Set the contents of a to be the union of the
elements in a and b
a.intersection(b) a & b All of the elements in both a and b
a.intersection_update(b) a &= b Set the contents of a to be the intersection of the
elements in a and b
a.difference(b) a - b The elements in a that are not in b
a.difference_update(b) a -= b Set a to the elements in a that are not in b
a.symmetric_difference(b) a ^ b All of the elements in either a or b but not both
a.symmetric_difference_update(b) a ^= b Set a to contain the elements in either a or b but
not both
a.issubset(b) N/A True if the elements of a are all contained in b
a.issuperset(b) N/A True if the elements of b are all contained in a
a.isdisjoint(b) N/A True if a and b have no elements in common

"""


 ## Functions 








































