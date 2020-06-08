'''
Write a Python program to find the most common elements and their counts of a specified text.
'''
from collections import Counter
s="this is a text"
print(Counter(s).most_common(3))
