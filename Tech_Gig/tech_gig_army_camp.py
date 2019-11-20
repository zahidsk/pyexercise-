r = 'C A P G A F J L D H K D M J' \
    'K D M J C A P G A F J L D H'
r1 = 'C A P G A F J L D H K D M J'
r2 = 'K D M J C A P G A F J L D H'
r2 = 'P G K D M J C A A F J L D H'


# print(r1)
# print(r2)
r = input()
rq = input()
print(r)
print(rq)
print(r.split("\n"))
r1 = r.split("\n")[0].split(' ')
r2 = r.split("\n")[1].split(' ')

lr1 = len(r1)
lr2 = len(r2)
if lr1 != lr2: print('No'); exit()
if lr1 < 1 or lr1 > 1000:
    print('No')

indices = [i for i, x in enumerate(r1) if x == r2[0]]
flag = True
lv = 0
for index in indices:
    lvr1 = index
    for in_lv in range(lr1):
        if r1[lvr1] != r2[lv]:
            flag = False
            break
        lv += 1
        lvr1 += 1
        if lvr1 == lr1: lvr1 = 0
    if not flag:
        lv = 0
if flag:
    print("Yes")
else:
    print('No')
