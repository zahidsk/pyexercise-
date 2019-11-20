# dc = 3
# disk_l = (1, 3, 2)
dc = 6
# disk_l = (3, 4, 2, 5, 6, 1)
disk_l = (5,1,2,3,4,6)
# disk_l = (4,2,3,5,1,6)


# ##########  40 marks only for this
if dc > 1000:                                       # if disk count more than 1000
    print(-1)
    exit()
exp_list = range(1, dc+1)
if all(i == j for i, j in zip(disk_l, exp_list)):   # If both list same
    print(-1)
    exit()

if disk_l[0] == exp_list[0]:
    print(dc-1)
    exit()
move_cnt = flag_cnt = 0
lv = 0
lv2 = 1

while True:
    if disk_l[lv] == disk_l[lv2]-1:
        lv2 += 1
        lv += 1
        if flag_cnt != move_cnt:
            lv += move_cnt-flag_cnt
            flag_cnt = move_cnt
    else:
        move_cnt += 1
        lv2 += 1
    if lv2 >= dc or lv >= dc:
        break
print(move_cnt)

