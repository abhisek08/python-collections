'''
Write a Python program to rotate a Deque Object specified number (positive) of times.
'''
from collections import deque
c=deque(range(4))
c.rotate(2)
print(c)