'''
Write a Python program to find the most common element of a given list.
'''
from collections import Counter
c=[1,2,3,4,2,2,2,2,1,1]
print(Counter(c).most_common(1))