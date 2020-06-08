'''
Write a Python program that accept some words and count the number of distinct words.
Print the number of distinct words and number of occurrences for each distinct word according to their appearance.
'''
from collections import Counter
s=['asd','asd','bcd','bcd','cb','cb','cb']
print(Counter(s).most_common())