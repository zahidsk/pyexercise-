"""
Varun is playing a very interesting game. He has some N different types of boxes.
All boxes may have different number of balls (S1, S2, ......, Sn).

Varun choose two random numbers F and K. K should be less than N. The game is that Varun wants to choose any K boxes out of N boxes such that total number of balls in these K selected boxes should be some multiple of F.

At the same time, Varun wants that sum of the balls of the selected boxes should be minimum possible.



Input Format
The first line of input consist of the number of boxes, N.
Next N lines consist of the number of balls in the respective box.
Next two lines consist of the value of F and K respectively.

"""
n = 5
ball_cnt_l = [1,2,3,4,5]
f = 5
k = 3

# #############
if n > 1000:
    print(-1)
    exit()
