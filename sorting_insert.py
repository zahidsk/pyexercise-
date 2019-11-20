# def insertion_sort(InputList):
#     for i in range(1, len(InputList)):
#         j = i - 1
#         nxt_element = InputList[i]
#         # Compare the current element with next one
#         print(i,j)
#         while (InputList[j] > nxt_element) and (j >= 0):
#             InputList[j + 1] = InputList[j]
#             j = j - 1
#         InputList[j + 1] = nxt_element


# class X:
#     def add(self, s, b, c):
#         return s+b+c
#
#     def add(self, s, b):
#         return s+b
#
# a = X()
# print(a.add(2,4,6))
# print(a.add(4,6))
def myinsert_sort(list):
    for i in range(len(list)):
        key = list[i+1]
        while list[i] > key:
            key = list[i]
            list[i+1] = list[i]



list = [19, 2, 31, 45, 30, 11, 121, 27]
myinsert_sort(list)
print(list)