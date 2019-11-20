
def bubblesort(list):
    count = 0
    for j in range(len(list)-1):
        for i in range(len(list)-(j+1)):
            count += 1
            if list[i] > list[i+1]:
                temp = list[i]
                list[i] = list[i+1]
                list[i+1] = temp
    print(count)


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)
