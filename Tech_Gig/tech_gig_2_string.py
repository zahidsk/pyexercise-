"""Input:

abcd
dbacef
output:4
explanation:
step 1: replace a with d (dbcd)
step 2: place a between bc (dbacd)
step 3: replace d with e
step 4: place f in end of the string"""

# objective : minimum number of insertion

def foo(x):
    x[0]=['abc']
    x[1]=['def']
    return id(x)
q = ['abc', 'def']
print (id(q)==foo(q))

# def writer():
#     t = 'Sir'
#     n = (lambda x:t+' '+x)
#     return n
#
# v = writer()
# print v('zahid')

#
# def count_insertion(ip,op):
#     fop = ''
#     for i, ch in enumerate(ip):
#         print op.index(ip[i])
#
#
# a = 'abcd'
# b = 'dbacef'
# count_insertion(a, b)
