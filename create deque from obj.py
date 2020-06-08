'''
Write a Python program to create a deque from an existing iterable object.
'''
from collections import deque
s=[1,2,3,4]
c=deque()
for i in s:
    c.append(i)
print(c)