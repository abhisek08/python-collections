'''
Write a Python program to rotate a Deque Object specified number (negative) of times.
'''
from collections import deque
c=deque(range(4))
c.rotate(-1)
print(c)