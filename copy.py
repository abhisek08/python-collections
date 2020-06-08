'''
 Write a Python program to copy of a deque object and verify the shallow copying process.
'''
from collections import deque
c=deque(range(3))
d=c.copy()
print(c,d)