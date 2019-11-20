# ###################
# write python program to find the occurrence of the each character in a file without using any inbuilt function
# ###################
with open("abc.txt", 'r') as fd:
    char_cnt = {}
    lins = fd.readlines()
    for line in lins:
        for char in line:
            # print(char)
            char_cnt[char] = 1 + char_cnt.get(char, 0)

# print(char_cnt)

# ###################
# write python program to find the occurrence of the each character in a file without using any inbuilt function
# ###################
with open("abc.txt", 'r') as fd:
    char_cnt = {}
    content = fd.read()
    for char in content:
        print(char)
        char_cnt[char] = 1 + char_cnt.get(char, 0)

print(char_cnt)
slice
