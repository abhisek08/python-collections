'''
Write a Python program to count the number of times a specific element presents in a deque object.
'''
from collections import deque,Counter
c=deque('abcabca')
print(c.count('a'))