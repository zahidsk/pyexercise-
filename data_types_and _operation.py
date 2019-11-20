"""
There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered and unindexed. No duplicate members.
Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
"""

# List
l1 = list(("apple", "mobile", "screen"))
print(l1)
l1.insert(2, "pen")
print(l1)
print(l1.index('pen'))
print(l1.pop(2))
print(l1)

l1.remove('apple')
print(l1)
l1.append('cable')
print(l1)
del l1[1]
print(l1)
l2 = [1, 3, 5]
l2.extend(l1)
print(l2)
l1.extend(l2)
print(l1)
print(l1.count('pen'))
