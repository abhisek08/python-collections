'''
Write a Python program to add more number of elements to a deque object from an iterable object.
'''
from collections import deque
s=[1,2,3]
c=deque('a')
c.extend(s)
print(c)