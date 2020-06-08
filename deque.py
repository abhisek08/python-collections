'''
Write a Python program to create a deque and append few elements to the left and right,
then remove some elements from the left, right sides and reverse the deque.
'''
from collections import deque
c=deque('aaaaaaa')
c.extendleft('xxx')
c.extend('yyy')
c.remove('x')
c.pop()
c.popleft()
c.reverse()
print(c)