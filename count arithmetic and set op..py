'''
Write a Python program to perform Counter arithmetic and set operations for aggregating results.
'''
import collections
c1 = collections.Counter([1, 2, 3, 4, 5])
c2 = collections.Counter([4, 5, 6, 7, 8])
print('C1:', c1)
print('C2:', c2)
print('\nCombined counts:')
print(c1 + c2)
print('\nSubtraction:')
print(c1 - c2)
print('\nIntersection (taking positive minimums):')
print(c1 & c2)
print('\nUnion (taking maximums):')
print(c1 | c2)