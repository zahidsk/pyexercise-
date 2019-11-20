import sys
import os


def count_jump(jump, slides_d, w_hight):
    act_jump = jump - slides_d
    lst_slide = w_hight % act_jump
    j_req = w_hight/act_jump
    if lst_slide > slides_d:
        j_req += 1
    print ("wall height : %s, req jump : %s"%(w_hight, j_req))
    return j_req

def GetJumpCount(can_jump, slides_down, wall_list):

    if can_jump-slides_down < 0:
        return 'Wrong input can_jump is less than slides down'
    # can_jump = input1
    # slides_down = input2
    # wall_list = input3
    total_jump = 0
    for wall in wall_list:
        total_jump += count_jump(can_jump, slides_down, wall)

    # print "Total Required Jump to Break Bhopal Jail : ", total_jump
    return total_jump

GetJumpCount(9, 3, [50])