'''
Write a Python program to find the occurrences of 10 most common words in a given text.
'''
from collections import Counter
t='abhsjxcmnfejogvojvoweriipetyjbnmvxvnz,cn;kaepwifjprgmvvxmlcnvojcnuiegfvnsjsdnfjogf'
print(Counter(t).most_common(10))